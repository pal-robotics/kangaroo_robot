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


from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument

from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import LaunchArgumentsBase
from launch_pal.robot_arguments import CommonArgs
from kangaroo_description.launch_arguments import KangarooArgs

from dataclasses import dataclass


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    ## Common

    # ["True", "False"]
    use_sim_time: DeclareLaunchArgument = CommonArgs.use_sim_time

    # ["false", "position", "motor"]
    mj_control: DeclareLaunchArgument = CommonArgs.mj_control
    
    ## Kangaroo specific

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
    
    # ["ft-leg", "leg", "no-leg"]
    legs_type: DeclareLaunchArgument = KangarooArgs.legs_type
    
    # ["cover", "fake-forearm", "ft-gripper", "gripper", "RA8D"]
    end_effector_type: DeclareLaunchArgument = KangarooArgs.end_effector_type

    # Fixation type ["crane", "fixed", "floating"]
    fixation_type: DeclareLaunchArgument = KangarooArgs.fixation_type


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    #Playmotion2    
    play_motion2 = include_scoped_launch_py_description(
        pkg_name='kangaroo_bringup',
        paths=['launch', 'kangaroo_playmotion2.launch.py'],
        launch_arguments={
            "use_sim_time": launch_args.use_sim_time,
            "collision_type": launch_args.collision_type,
            "sim_type": launch_args.sim_type,
            "mj_control": launch_args.mj_control,
            "has_head": launch_args.has_head,
            "has_pelvis": launch_args.has_pelvis,
            "arm_type": launch_args.arm_type,
            "legs_type": launch_args.legs_type,
            "end_effector_type": launch_args.end_effector_type,
            "fixation_type": launch_args.fixation_type,
            })

    launch_description.add_action(play_motion2)

    # Robot State Publisher
    robot_state_publisher = include_scoped_launch_py_description(
        pkg_name='kangaroo_description',
        paths=['launch', 'robot_state_publisher.launch.py'],
        launch_arguments={
            "use_sim_time": launch_args.use_sim_time,
            "collision_type": launch_args.collision_type,
            "sim_type": launch_args.sim_type,
            "mj_control": launch_args.mj_control,
            "has_head": launch_args.has_head,
            "has_pelvis": launch_args.has_pelvis,
            "arm_type": launch_args.arm_type,
            "legs_type": launch_args.legs_type,
            "end_effector_type": launch_args.end_effector_type,
            "fixation_type": launch_args.fixation_type,
            })

    launch_description.add_action(robot_state_publisher)

    # Broadcaster Controllers
    broadcaster_controllers = include_scoped_launch_py_description(
        pkg_name='kangaroo_controller_configuration',
        paths=['launch', 'broadcasters.launch.py'],
        )

    launch_description.add_action(broadcaster_controllers)

    return


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
