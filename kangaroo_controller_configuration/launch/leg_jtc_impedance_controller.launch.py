# Copyright (c) 2026 PAL Robotics S.L. All rights reserved.
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
import logging
import os

from ament_index_python.packages import get_package_share_directory

from controller_manager.launch_utils import generate_load_controller_launch_description
from launch import LaunchContext, LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction, OpaqueFunction
from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch_pal.param_utils import parse_parametric_yaml


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    side: DeclareLaunchArgument = DeclareLaunchArgument(
        name='side',
        choices=['left', 'right'],
        description='side of the leg')

    activate: DeclareLaunchArgument = DeclareLaunchArgument(
        name='activate',
        default_value='True',
        choices=['True', 'False'],
        description='Argument to choose whether to activate the controllers or '
                    'leave them configured and in inactive state')

    unload_on_kill: DeclareLaunchArgument = DeclareLaunchArgument(
        name='unload_on_kill',
        default_value='True',
        choices=['True', 'False'],
        description='Argument to choose whether to deactivate and unload the '
                    'controllers when killing the launch process')

    interface_level: DeclareLaunchArgument = DeclareLaunchArgument(
        name='interface_level',
        default_value='joint',
        choices=['joint', 'actuator'],
        description='level of control for the leg')


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    launch_description.add_action(OpaqueFunction(
        function=setup_controller_configuration))

    return


def setup_controller_configuration(context: LaunchContext):

    side = read_launch_argument('side', context)
    activate = read_launch_argument('activate', context)
    unload_on_kill = read_launch_argument('unload_on_kill', context)
    interface_level = read_launch_argument('interface_level', context)

    if unload_on_kill == 'True' and activate == 'False':
        logging.getLogger(__name__).warning(
            '`unload_on_kill` is set to True but `activate` is set to False: '
            '`unload_on_kill` is ignored and the controllers will be configured and exited.'
        )

    extra_spawner_args = []
    if activate == 'False':
        extra_spawner_args = ['--inactive']
    elif unload_on_kill == 'True':
        extra_spawner_args = ['--unload-on-kill']

    leg_prefix = 'leg'
    if side:
        leg_prefix = f'leg_{side}'

    controller_name = f'{leg_prefix}_jtc_impedance_{interface_level}_controller'
    remappings = {'LEG_SIDE_PREFIX': leg_prefix, 'INTERFACE_LEVEL': interface_level}

    param_file = os.path.join(
        get_package_share_directory('kangaroo_controller_configuration'),
        'config', 'leg_jtc_impedance_controller.yaml')

    parsed_yaml = parse_parametric_yaml(source_files=[param_file], param_rewrites=remappings)

    launch_controller = GroupAction([generate_load_controller_launch_description(
        controller_name=controller_name,
        controller_params_file=parsed_yaml,
        extra_spawner_args=extra_spawner_args)])

    return [launch_controller]


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
