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

from kangaroo_description.launch_arguments import KangarooArgs
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_pal.arg_utils import LaunchArgumentsBase
from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.robot_arguments import CommonArgs


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

    # ["no-end-effector", "gripper", "RH8D"]
    end_effector_right: DeclareLaunchArgument = KangarooArgs.end_effector_right
    end_effector_left: DeclareLaunchArgument = KangarooArgs.end_effector_left

    # Fixation type ["crane", "fixed", "floating"]
    fixation_type: DeclareLaunchArgument = KangarooArgs.fixation_type

    # FT sensor type ["no-ft-sensor", "ati"]
    ft_sensor_right: DeclareLaunchArgument = KangarooArgs.ft_sensor_right
    ft_sensor_left: DeclareLaunchArgument = KangarooArgs.ft_sensor_left
    ankle_ft_right: DeclareLaunchArgument = KangarooArgs.ankle_ft_right
    ankle_ft_left: DeclareLaunchArgument = KangarooArgs.ankle_ft_left

    # IMUs
    torso_imu_model: DeclareLaunchArgument = KangarooArgs.torso_imu_model
    base_imu_model: DeclareLaunchArgument = KangarooArgs.base_imu_model


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    # Playmotion2
    play_motion2 = include_scoped_launch_py_description(
        pkg_name='kangaroo_bringup',
        paths=['launch', 'kangaroo_playmotion2.launch.py'],
        launch_arguments={
            'use_sim_time': launch_args.use_sim_time,
            'collision_type': launch_args.collision_type,
            'sim_type': launch_args.sim_type,
            'mj_control': launch_args.mj_control,
            'has_head': launch_args.has_head,
            'has_pelvis': launch_args.has_pelvis,
            'arm_type': launch_args.arm_type,
            'feet_type': launch_args.feet_type,
            'end_effector_right': launch_args.end_effector_right,
            'end_effector_left': launch_args.end_effector_left,
            'fixation_type': launch_args.fixation_type,
            'ft_sensor_right': launch_args.ft_sensor_right,
            'ft_sensor_left': launch_args.ft_sensor_left,
        })

    launch_description.add_action(play_motion2)

    # Robot State Publisher
    robot_state_publisher = include_scoped_launch_py_description(
        pkg_name='kangaroo_description',
        paths=['launch', 'robot_state_publisher.launch.py'],
        launch_arguments={
            'use_sim_time': launch_args.use_sim_time,
            'collision_type': launch_args.collision_type,
            'sim_type': launch_args.sim_type,
            'mj_control': launch_args.mj_control,
            'has_head': launch_args.has_head,
            'has_pelvis': launch_args.has_pelvis,
            'arm_type': launch_args.arm_type,
            'ankle_ft_right': launch_args.ankle_ft_right,
            'ankle_ft_left': launch_args.ankle_ft_left,
            'feet_type': launch_args.feet_type,
            'end_effector_right': launch_args.end_effector_right,
            'end_effector_left': launch_args.end_effector_left,
            'fixation_type': launch_args.fixation_type,
            'ft_sensor_right': launch_args.ft_sensor_right,
            'ft_sensor_left': launch_args.ft_sensor_left,
            'torso_imu_model': launch_args.torso_imu_model,
            'base_imu_model': launch_args.base_imu_model,
            'use_mimic': launch_args.use_mimic
        })

    launch_description.add_action(robot_state_publisher)

    # Broadcaster Controllers
    broadcaster_controllers = include_scoped_launch_py_description(
        pkg_name='kangaroo_controller_configuration',
        paths=['launch', 'default_broadcasters.launch.py'],
        launch_arguments={
            'use_sim_time': launch_args.use_sim_time,
            'arm_type': launch_args.arm_type,
            'ankle_ft_right': launch_args.ankle_ft_right,
            'ankle_ft_left': launch_args.ankle_ft_left,
            'end_effector_right': launch_args.end_effector_right,
            'end_effector_left': launch_args.end_effector_left,
            'ft_sensor_right': launch_args.ft_sensor_right,
            'ft_sensor_left': launch_args.ft_sensor_left,
            'torso_imu_model': launch_args.torso_imu_model,
            'base_imu_model': launch_args.base_imu_model
        })

    launch_description.add_action(broadcaster_controllers)

    return


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
