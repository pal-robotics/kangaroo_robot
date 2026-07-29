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
import logging
import os

from ament_index_python.packages import get_package_share_directory

from controller_manager.launch_utils import generate_load_controller_launch_description
from kangaroo_description.kangaroo_launch_utils import GetParametersFromBlackboard
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch_pal.include_utils import include_scoped_launch_py_description


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):

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


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    # Add controller of right arm, end-effector and ft-sensor
    get_params_from_blackboard = GetParametersFromBlackboard(
        blackboard_node_name='parameter_blackboard',
        parameter_names=['has_pelvis', 'arm_type', 'end_effector_right', 'end_effector_left']
        )
    launch_description.add_action(get_params_from_blackboard)

    start_controllers_action = OpaqueFunction(function=start_controllers)
    launch_description.add_action(start_controllers_action)

    return


def start_controllers(context, *args, **kwargs):
    unload_on_kill = LaunchConfiguration('unload_on_kill').perform(context)
    activate = LaunchConfiguration('activate').perform(context)
    pkg_share_folder = get_package_share_directory('kangaroo_controller_configuration')

    ld = []

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

    # Pelvis controller
    if read_launch_argument('has_pelvis', context) == 'True':
        pelvis_controller = GroupAction(
            [generate_load_controller_launch_description(
                controller_name='pelvis_controller',
                controller_params_file=os.path.join(
                    pkg_share_folder,
                    'config', 'pelvis_controller.yaml'),
                extra_spawner_args=extra_spawner_args
                )],
            forwarding=False
        )

        ld.append(pelvis_controller)

    # Arm controllers
    if read_launch_argument('arm_type', context) != 'no-arm':
        arm_left_controller = include_scoped_launch_py_description(
            pkg_name='kangaroo_controller_configuration',
            paths=['launch', 'arm_controller.launch.py'],
            launch_arguments={
                'side': 'left',
                'arm_type': LaunchConfiguration('arm_type'),
                'activate': activate,
                'unload_on_kill': unload_on_kill,
            })
        ld.append(arm_left_controller)

        arm_right_controller = include_scoped_launch_py_description(
            pkg_name='kangaroo_controller_configuration',
            paths=['launch', 'arm_controller.launch.py'],
            launch_arguments={
                'side': 'right',
                'arm_type': LaunchConfiguration('arm_type'),
                'activate': activate,
                'unload_on_kill': unload_on_kill,
            })
        ld.append(arm_right_controller)

    # End-effector controllers
    if read_launch_argument('end_effector_right', context) == 'gripper':
        end_effector_right_controller = include_scoped_launch_py_description(
            pkg_name='pal_pro_gripper_controller_configuration',
            paths=['launch', 'pal_pro_gripper_controller.launch.py'],
            launch_arguments={'side': 'right'})
        ld.append(end_effector_right_controller)
    elif read_launch_argument('end_effector_right', context) == 'RH8D':
        end_effector_right_controller = include_scoped_launch_py_description(
            pkg_name='rh8d_controller_configuration',
            paths=['launch', 'rh8d_hand_controller.launch.py'],
            launch_arguments={'side': 'right'})
        ld.append(end_effector_right_controller)

    if read_launch_argument('end_effector_left', context) == 'gripper':
        end_effector_left_controller = include_scoped_launch_py_description(
            pkg_name='pal_pro_gripper_controller_configuration',
            paths=['launch', 'pal_pro_gripper_controller.launch.py'],
            launch_arguments={'side': 'left'})
        ld.append(end_effector_left_controller)
    elif read_launch_argument('end_effector_left', context) == 'RH8D':
        end_effector_left_controller = include_scoped_launch_py_description(
            pkg_name='rh8d_controller_configuration',
            paths=['launch', 'rh8d_hand_controller.launch.py'],
            launch_arguments={'side': 'left'})
        ld.append(end_effector_left_controller)

    # Leg controllers
    leg_left_controller = include_scoped_launch_py_description(
        pkg_name='kangaroo_controller_configuration',
        paths=['launch', 'leg_controller.launch.py'],
        launch_arguments={
            'side': 'left',
            'control_type': 'position',
            'activate': activate,
            'unload_on_kill': unload_on_kill,
        })
    ld.append(leg_left_controller)

    leg_right_controller = include_scoped_launch_py_description(
        pkg_name='kangaroo_controller_configuration',
        paths=['launch', 'leg_controller.launch.py'],
        launch_arguments={
            'side': 'right',
            'control_type': 'position',
            'activate': activate,
            'unload_on_kill': unload_on_kill,
        })
    ld.append(leg_right_controller)

    return ld


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
