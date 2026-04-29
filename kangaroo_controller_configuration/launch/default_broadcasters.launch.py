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

import os
from ament_index_python.packages import get_package_share_directory
from kangaroo_description.kangaroo_description.launch_arguments import KangarooArgs
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction, OpaqueFunction
from launch.conditions import IfCondition, IfLaunchConfigurationNotEquals, LaunchConfigurationNotEquals
from launch.substitutions import PythonExpression
from controller_manager.launch_utils import generate_load_controller_launch_description
from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch_pal.include_utils import include_scoped_launch_py_description

from typing import List

from dataclasses import dataclass


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    arm_type: DeclareLaunchArgument = KangarooArgs.arm_type
    ft_sensor_right: DeclareLaunchArgument = KangarooArgs.ft_sensor_right
    ft_sensor_left: DeclareLaunchArgument = KangarooArgs.ft_sensor_left

   

def concatenate_strings(strings: List[str], delimiter: str = '', skip_empty: bool = False):

    concatenated_string = ''

    if skip_empty:
        concatenated_string = delimiter.join(filter(None, strings))
    else:
        concatenated_string = delimiter.join(strings)

    return concatenated_string


def configure_side_controllers(context, end_effector_side='right', *args, **kwargs):
    
    ft_sensor_arg_name = concatenate_strings(
        strings=['ft_sensor', end_effector_side],
        delimiter='_',
        skip_empty=True)


    # Setup ft-sensor controller
    ft_sensor = read_launch_argument(ft_sensor_arg_name, context)

    ft_pkg_name = 'pal_sea_arm_controller_configuration'
    ft_launch_file = 'ft_sensor_controller.launch.py'

    ft_sensor_controller = include_scoped_launch_py_description(
        pkg_name=ft_pkg_name,
        paths=['launch', ft_launch_file],
        launch_arguments={"side": end_effector_side,
                          "ft_sensor": ft_sensor},
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

    # IMU sensor broadcaster
    imu_sensor_broadcaster = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='imu_sensor_broadcaster',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'sensors_broadcaster.yaml'))
         ],
        forwarding=False)

    launch_description.add_action(imu_sensor_broadcaster)

    # Add controller of right ft-sensor
    launch_description.add_action(OpaqueFunction(
        function=configure_side_controllers, args=['right'],
        condition=IfCondition(
            PythonExpression([
                "(", IfLaunchConfigurationNotEquals("arm_type", "no-arm"), ") and  ('",
                IfLaunchConfigurationNotEquals("arm_type", "4dof"), "')"])
        ))

    # Add controller of left ft-sensor
    launch_description.add_action(OpaqueFunction(
        function=configure_side_controllers, args=['left'],
        condition=IfCondition(
            PythonExpression([
                "(", IfLaunchConfigurationNotEquals("arm_type", "no-arm"), ") and  ('",
                IfLaunchConfigurationNotEquals("arm_type", "4dof"), "')"])
        )))

def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
