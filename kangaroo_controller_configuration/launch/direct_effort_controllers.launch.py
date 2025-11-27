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
from launch import LaunchDescription
from launch.actions import GroupAction
from launch.substitutions import LaunchConfiguration
from launch.actions import OpaqueFunction
from controller_manager.launch_utils import generate_load_controller_launch_description
from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument

from kangaroo_description.kangaroo_launch_utils import GetParametersFromBlackboard

from dataclasses import dataclass


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    pass
   

def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    # Add controller of right arm, end-effector and ft-sensor
    get_params_from_blackboard = GetParametersFromBlackboard(
        blackboard_node_name='parameter_blackboard', 
        parameter_names=["legs_type", "has_pelvis", "arm_type", "end_effector_type"]
        )
    launch_description.add_action(get_params_from_blackboard)

    start_controllers_action = OpaqueFunction(function=start_controllers)
    launch_description.add_action(start_controllers_action)

    return

def start_controllers(context, *args, **kwargs):
    pkg_share_folder = get_package_share_directory('kangaroo_controller_configuration')
    
    ld = []

    # Pelvis controller
    
    # Arm controllers
    
    # End-effector controllers
    

    # Leg controllers
    if read_launch_argument("legs_type", context) != "no-legs":
        leg_left_controller = include_scoped_launch_py_description(
            pkg_name='kangaroo_controller_configuration',
            paths=['launch', 'leg_controller.launch.py'],
            launch_arguments={"side": "left", "control_type": "effort"})
        ld.append(leg_left_controller)

        leg_right_controller = include_scoped_launch_py_description(
            pkg_name='kangaroo_controller_configuration',
            paths=['launch', 'leg_controller.launch.py'],
            launch_arguments={"side": "right", "control_type": "effort"})
        ld.append(leg_right_controller)

    return ld


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
