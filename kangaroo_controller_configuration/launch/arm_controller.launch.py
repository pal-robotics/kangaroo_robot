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

from dataclasses import dataclass

from ament_index_python.packages import get_package_share_directory
from controller_manager.launch_utils import generate_load_controller_launch_description
from launch_pal.param_utils import parse_parametric_yaml
from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch.actions import DeclareLaunchArgument, SetLaunchConfiguration
from launch.actions import OpaqueFunction, GroupAction
from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription, LaunchContext
from kangaroo_description.launch_arguments import KangarooArgs

@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    side: DeclareLaunchArgument = DeclareLaunchArgument(
        name='side',
        default_value='',
        description='side of the ft sensor')
    
    arm_type: DeclareLaunchArgument = KangarooArgs.arm_type


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    launch_description.add_action(OpaqueFunction(
        function=setup_controller_configuration))

    launch_controller = GroupAction([generate_load_controller_launch_description(
        controller_name=LaunchConfiguration("controller_name"),
        controller_params_file=LaunchConfiguration("controller_config"))])

    launch_description.add_action(launch_controller)

    return


def setup_controller_configuration(context: LaunchContext):

    side = read_launch_argument('side', context)
    arm_type = read_launch_argument('arm_type', context)

    arm_prefix = "arm"
    if side:
        arm_prefix = f"arm_{side}"

    controller_name = f"{arm_prefix}_controller"
    remappings = {"ARM_SIDE_PREFIX": arm_prefix}

    param_file = os.path.join(
        get_package_share_directory('kangaroo_controller_configuration'),
        'config', "arm_controllers", f'arm_{arm_type}_controller.yaml')

    parsed_yaml = parse_parametric_yaml(source_files=[param_file], param_rewrites=remappings)

    return [SetLaunchConfiguration('controller_name', controller_name),
            SetLaunchConfiguration('controller_config', parsed_yaml)]


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
