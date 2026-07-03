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
from typing import List

from ament_index_python.packages import get_package_share_directory

from controller_manager.launch_utils import generate_load_controller_launch_description
from kangaroo_description.launch_arguments import KangarooArgs
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction, OpaqueFunction
from launch.conditions import IfCondition, LaunchConfigurationNotEquals
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.param_utils import parse_parametric_yaml


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    arm_type: DeclareLaunchArgument = KangarooArgs.arm_type
    base_imu_model: DeclareLaunchArgument = KangarooArgs.base_imu_model
    ft_sensor_right: DeclareLaunchArgument = KangarooArgs.ft_sensor_right
    ft_sensor_left: DeclareLaunchArgument = KangarooArgs.ft_sensor_left
    ankle_ft_right: DeclareLaunchArgument = KangarooArgs.ankle_ft_right
    ankle_ft_left: DeclareLaunchArgument = KangarooArgs.ankle_ft_left
    torso_imu_model: DeclareLaunchArgument = KangarooArgs.torso_imu_model


def concatenate_strings(strings: List[str], delimiter: str = '', skip_empty: bool = False):

    concatenated_string = ''

    if skip_empty:
        concatenated_string = delimiter.join(filter(None, strings))
    else:
        concatenated_string = delimiter.join(strings)

    return concatenated_string


def configure_imu_broadcaster(context, sensor_name, frame_id, *args, **kwargs):

    pkg_share_folder = get_package_share_directory('kangaroo_controller_configuration')
    parsed_yaml = parse_parametric_yaml(
        source_files=[os.path.join(pkg_share_folder, 'config', 'sensors_broadcaster.yaml')],
        param_rewrites={'IMU_SENSOR_NAME': sensor_name, 'IMU_FRAME_ID': frame_id}
    )

    return [GroupAction(
        [generate_load_controller_launch_description(
            controller_name=f'{sensor_name}_broadcaster',
            controller_params_file=parsed_yaml)],
        forwarding=False)]


def configure_side_controllers(context, side='right', sensor_prefix='ft_sensor',
                               is_ankle=False, *args, **kwargs):

    ft_sensor_arg_name = concatenate_strings(
        strings=[sensor_prefix, side],
        delimiter='_',
        skip_empty=True)

    # Setup ft-sensor controller
    ft_sensor = read_launch_argument(ft_sensor_arg_name, context)

    ft_pkg_name = 'pal_sea_arm_controller_configuration'
    ft_launch_file = 'ft_sensor_broadcaster.launch.py'
    ft_sensor_controller = include_scoped_launch_py_description(
        pkg_name=ft_pkg_name,
        paths=['launch', ft_launch_file],
        launch_arguments={'side': side,
                          'ft_sensor': ft_sensor,
                          'location': 'ankle' if sensor_prefix == 'ankle_ft' else 'wrist'},
        condition=LaunchConfigurationNotEquals(
            ft_sensor_arg_name, 'no-ft-sensor')
    )

    return [ft_sensor_controller]


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    pkg_share_folder = get_package_share_directory('kangaroo_controller_configuration')
    # Joint state broadcaster
    joint_state_broadcaster = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='joint_state_broadcaster',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'joint_state_broadcaster.yaml'))
         ],
        forwarding=False)

    launch_description.add_action(joint_state_broadcaster)

    # IMU torso sensor broadcaster
    launch_description.add_action(OpaqueFunction(
        function=configure_imu_broadcaster,
        kwargs={'sensor_name': 'torso_imu_sensor', 'frame_id': 'torso_imu_link'},
        condition=LaunchConfigurationNotEquals('torso_imu_model', 'no-imu')))

    # IMU base sensor broadcaster
    launch_description.add_action(OpaqueFunction(
        function=configure_imu_broadcaster,
        kwargs={'sensor_name': 'base_imu_sensor', 'frame_id': 'base_imu_sensor_link'},
        condition=LaunchConfigurationNotEquals('base_imu_model', 'no-imu')))

    # Add controller of right ft-sensor
    launch_description.add_action(OpaqueFunction(
        function=configure_side_controllers, kwargs={'side': 'right',
                                                     'sensor_prefix': 'ft_sensor'},
        condition=IfCondition(
            PythonExpression(["'", LaunchConfiguration('arm_type'),
                              "' not in ['no-arm', '4dof']"])
                              ))
    )

    # Add controller of left ft-sensor
    launch_description.add_action(OpaqueFunction(
        function=configure_side_controllers, kwargs={'side': 'left',
                                                     'sensor_prefix': 'ft_sensor'},
        condition=IfCondition(
            PythonExpression(["'", LaunchConfiguration('arm_type'),
                              "' not in ['no-arm', '4dof']"])
                            ))
    )

    # Add controller of right ankle ft-sensor
    launch_description.add_action(
        OpaqueFunction(
            function=configure_side_controllers,
            kwargs={'side': 'right', 'sensor_prefix': 'ankle_ft', 'location': 'ankle'},
        )
    )

    # Add controller of left ankle ft-sensor
    launch_description.add_action(
        OpaqueFunction(
            function=configure_side_controllers,
            kwargs={'side': 'left', 'sensor_prefix': 'ankle_ft', 'location': 'ankle'}
        )
    )


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
