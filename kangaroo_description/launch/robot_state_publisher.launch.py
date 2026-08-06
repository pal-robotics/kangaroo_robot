# Copyright (c) 2024 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass
import os
from pathlib import Path

from ament_index_python.packages import get_package_share_directory

from kangaroo_description.kangaroo_launch_utils import SetParametersToBlackboard
from kangaroo_description.launch_arguments import KangarooArgs
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction, SetLaunchConfiguration
from launch.actions import LogInfo, RegisterEventHandler
from launch.event_handlers import OnProcessStart
from launch.substitutions import LaunchConfiguration
from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch_pal.robot_arguments import CommonArgs
from launch_param_builder import load_xacro
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):

    # Common

    # ["True", "False"]
    use_sim_time: DeclareLaunchArgument = CommonArgs.use_sim_time

    # ["false", "position", "motor"]
    mj_control: DeclareLaunchArgument = CommonArgs.mj_control

    # Kangaroo specific

    # ["mujoco-ros2-control", "mujoco", "no-simulation"]
    sim_type: DeclareLaunchArgument = KangarooArgs.sim_type

    # ["True", "False"]
    use_mimic: DeclareLaunchArgument = KangarooArgs.use_mimic

    # ["mesh", "capsule"]
    collision_type: DeclareLaunchArgument = KangarooArgs.collision_type

    # [True, False]
    has_head: DeclareLaunchArgument = KangarooArgs.has_head

    # [True, False]
    has_pelvis: DeclareLaunchArgument = KangarooArgs.has_pelvis

    # ["no-arm", "4dof", "5dof", "7dof"]
    arm_type: DeclareLaunchArgument = KangarooArgs.arm_type

    # ["fixed", "detachable"]
    feet_type: DeclareLaunchArgument = KangarooArgs.feet_type

    # ["no-end-effector", "ft-gripper", "gripper", "RH8D"]
    end_effector_right: DeclareLaunchArgument = KangarooArgs.end_effector_right
    end_effector_left: DeclareLaunchArgument = KangarooArgs.end_effector_left

    # Fixation type ["crane", "fixed", "floating"]
    fixation_type: DeclareLaunchArgument = KangarooArgs.fixation_type

    # FT sensor type ["no-ft-sensor", "ati"]
    ft_sensor_right: DeclareLaunchArgument = KangarooArgs.ft_sensor_right
    ft_sensor_left: DeclareLaunchArgument = KangarooArgs.ft_sensor_left

    ankle_ft_right: DeclareLaunchArgument = KangarooArgs.ankle_ft_right
    ankle_ft_left: DeclareLaunchArgument = KangarooArgs.ankle_ft_left

    # ["orientus", "microstrain", "no-imu"]
    torso_imu_model: DeclareLaunchArgument = KangarooArgs.torso_imu_model
    base_imu_model: DeclareLaunchArgument = KangarooArgs.base_imu_model


def generate_launch_description():

    # Create the launch description and populate
    ld = LaunchDescription()
    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)
    return ld


def declare_actions(
    launch_description: LaunchDescription, launch_args: LaunchArguments
):
    parameter_blackboard_node = Node(
        package='kangaroo_description',
        executable='parameter_blackboard',
        name='parameter_blackboard',
        output='screen'
    )
    launch_description.add_action(parameter_blackboard_node)

    # Define Robot Specific Parameters
    set_params_on_blackboard = SetParametersToBlackboard(
        blackboard_node_name='parameter_blackboard',
        parameters={
            'robot_model': LaunchConfiguration('robot_model'),
            'use_sim_time': LaunchConfiguration('use_sim_time'),
            'use_mimic': LaunchConfiguration('use_mimic'),
            'sim_type': LaunchConfiguration('sim_type'),
            'mj_control': LaunchConfiguration('mj_control'),
            'collision_type': LaunchConfiguration('collision_type'),
            'has_head': LaunchConfiguration('has_head'),
            'has_pelvis': LaunchConfiguration('has_pelvis'),
            'arm_type': LaunchConfiguration('arm_type'),
            'end_effector_right': LaunchConfiguration('end_effector_right'),
            'end_effector_left': LaunchConfiguration('end_effector_left'),
            'ft_sensor_right': LaunchConfiguration('ft_sensor_right'),
            'ft_sensor_left': LaunchConfiguration('ft_sensor_left'),
            'ankle_ft_right': LaunchConfiguration('ankle_ft_right'),
            'ankle_ft_left': LaunchConfiguration('ankle_ft_left'),
            'feet_type': LaunchConfiguration('feet_type'),
            'fixation_type': LaunchConfiguration('fixation_type'),
            'torso_imu_model': LaunchConfiguration('torso_imu_model'),
            'base_imu_model': LaunchConfiguration('base_imu_model')
        }
    )

    robot_state_publisher_event_handler = RegisterEventHandler(
        OnProcessStart(
            # Target the specific node we want to wait for
            target_action=parameter_blackboard_node,
            # When that node starts, execute our custom action
            on_start=[
                LogInfo(msg='Parameter blackboard started'),
                SetLaunchConfiguration('robot_model', 'kangaroo'),
                set_params_on_blackboard
            ]
        )
    )
    launch_description.add_action(robot_state_publisher_event_handler)

    launch_description.add_action(
        OpaqueFunction(function=create_robot_description_param)
    )

    # Using ParameterValue is needed so ROS knows the parameter type
    # Otherwise https://github.com/ros2/launch_ros/issues/136
    rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='both',
        parameters=[
            {
                'robot_description': ParameterValue(
                    LaunchConfiguration('robot_description'), value_type=str
                ),
            },
            {'use_sim_time': LaunchConfiguration('use_sim_time')},
            {'publish_frequency': 100.0},
        ],
    )

    launch_description.add_action(rsp)

    return


def create_robot_description_param(context, *args, **kwargs):

    xacro_file_path = Path(
        os.path.join(
            get_package_share_directory('kangaroo_description'),
            'robots',
            'kangaroo.urdf.xacro',
        )
    )

    xacro_input_args = {
        'use_sim_time': read_launch_argument('use_sim_time', context),
        'collision_type': read_launch_argument('collision_type', context),
        'sim_type': read_launch_argument('sim_type', context),
        'mj_control': read_launch_argument('mj_control', context),
        'fixation_type': read_launch_argument('fixation_type', context),
        'feet_type': read_launch_argument('feet_type', context),
        'arm_type': read_launch_argument('arm_type', context),
        'end_effector_right': read_launch_argument('end_effector_right', context),
        'end_effector_left': read_launch_argument('end_effector_left', context),
        'ft_sensor_right': read_launch_argument('ft_sensor_right', context),
        'ft_sensor_left': read_launch_argument('ft_sensor_left', context),
        'ankle_ft_right': read_launch_argument('ankle_ft_right', context),
        'ankle_ft_left': read_launch_argument('ankle_ft_left', context),
        'has_head': read_launch_argument('has_head', context),
        'has_pelvis': read_launch_argument('has_pelvis', context),
        'torso_imu_model': read_launch_argument('torso_imu_model', context),
        'base_imu_model': read_launch_argument('base_imu_model', context),
        'use_mimic': read_launch_argument('use_mimic', context)
    }
    robot_description = load_xacro(xacro_file_path, xacro_input_args)

    return [SetLaunchConfiguration('robot_description', robot_description)]
