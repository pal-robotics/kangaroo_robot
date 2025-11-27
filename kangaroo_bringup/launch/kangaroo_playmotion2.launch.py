# Copyright (c) 2025 PAL Robotics S.L. All rights reserved.
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

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch.actions import DeclareLaunchArgument, SetLaunchConfiguration, OpaqueFunction

from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch_pal.robot_arguments import CommonArgs
from launch_pal.param_utils import merge_param_files

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
    
    launch_description.add_action(OpaqueFunction(
        function=create_play_motion_filename))
    
    play_motion2 = include_scoped_launch_py_description(
        pkg_name='play_motion2',
        paths=['launch', 'play_motion2.launch.py'],
        launch_arguments={
            "use_sim_time":  launch_args.use_sim_time,
            "motions_file": LaunchConfiguration('motions_file'),
            'motion_planner_config': LaunchConfiguration('motion_planner_config')
        })

    launch_description.add_action(play_motion2)

    return


def create_play_motion_filename(context):

    pkg_name = 'kangaroo_bringup'
    pkg_share_dir = get_package_share_directory(pkg_name)
    end_effector_type = read_launch_argument('end_effector_type', context)
    arm_type = read_launch_argument('arm_type', context)
    legs_type = read_launch_argument('legs_type', context)
    has_pelvis = read_launch_argument('has_pelvis', context)
    
    motions_files = []
    # Create hardware suffix ex. kangaroo_motions_5dof_RH8D_with-pelvis_leg.yaml
    if legs_type != 'no-leg':
        motions_files.append(PathJoinSubstitution(
                        [pkg_share_dir, "config", "motions", "lower_body", "kangaroo_motions_legs_only.yaml"]
                    ))

    if has_pelvis:
        motions_files.append(PathJoinSubstitution(
                        [pkg_share_dir, "config", "motions", "lower_body", "kangaroo_motions_pelvis_only.yaml"]
                    ))
    
    if arm_type != 'no-arm':
        arm_hw_suffix = '_' + f'{arm_type}_' + f'{end_effector_type}'
        motions_files.append(PathJoinSubstitution(
                    [pkg_share_dir, "config", "motions", "upper_body", f"kangaroo_motions{arm_hw_suffix}.yaml"]
                ))
        if end_effector_type != 'no-end-effector' and arm_type !='4dof':
            arm_hw_suffix = '_' + f'{arm_type}_' + 'no-end-effector'
            motions_files.append(PathJoinSubstitution(
                            [pkg_share_dir, "config", "motions", "upper_body", f"kangaroo_motions{arm_hw_suffix}.yaml"]
                        ))
            
    # Add full No-End-Effector + No/with pelvis
    if arm_type in ['5dof', '7dof']:
        # No-end-effector + No pelvis
        full_hw_suffix = '_' + f'{arm_type}_' + 'no-end-effector_'+ 'no-pelvis_' + f"{'leg' if legs_type!='no-leg' else 'no-leg'}"
        motions_files.append(PathJoinSubstitution(
                                [pkg_share_dir, "config", "motions", f"{arm_type}_specifics", f"kangaroo_motions{full_hw_suffix}.yaml"]
                            ))
        # No-end-effector + With pelvis
        if has_pelvis:
            full_hw_suffix = '_' + f'{arm_type}_' + f'{end_effector_type}_'+ 'with-pelvis_' + f"{'leg' if legs_type!='no-leg' else 'no-leg'}"
            motions_files.append(PathJoinSubstitution(
                            [pkg_share_dir, "config", "motions", f"{arm_type}_specifics", f"kangaroo_motions{full_hw_suffix}.yaml"]
                        ))
            
        # Specifically add End-Effector versions
        if end_effector_type != 'no-end-effector':
            # No pelvis
            full_hw_suffix = '_' + f'{arm_type}_' + f'{end_effector_type}_'+ 'no-pelvis_' + f"{'leg' if legs_type!='no-leg' else 'no-leg'}"
            motions_files.append(PathJoinSubstitution(
                    [pkg_share_dir, "config", "motions", f"{arm_type}_specifics", f"kangaroo_motions{full_hw_suffix}.yaml"]
                ))
            # With pelvis
            if has_pelvis:
                full_hw_suffix = '_' + f'{arm_type}_' + f'{end_effector_type}_'+ 'with-pelvis_' + f"{'leg' if legs_type!='no-leg' else 'no-leg'}"
                motions_files.append(PathJoinSubstitution(
                        [pkg_share_dir, "config", "motions", f"{arm_type}_specifics", f"kangaroo_motions{full_hw_suffix}.yaml"]
                    ))
    if arm_type == '4dof':
        # No pelvis
        full_hw_suffix = '_' + f'{arm_type}_' + f'{end_effector_type}_'+ 'no-pelvis_' + f"{'leg' if legs_type!='no-leg' else 'no-leg'}"
        motions_files.append(PathJoinSubstitution(
                [pkg_share_dir, "config", "motions", f"{arm_type}_specifics", f"kangaroo_motions{full_hw_suffix}.yaml"]
            ))
        # With pelvis
        if has_pelvis:
            full_hw_suffix = '_' + f'{arm_type}_' + f'{end_effector_type}_'+ 'with-pelvis_' + f"{'leg' if legs_type!='no-leg' else 'no-leg'}"
            motions_files.append(PathJoinSubstitution(
                    [pkg_share_dir, "config", "motions", f"{arm_type}_specifics", f"kangaroo_motions{full_hw_suffix}.yaml"]
                ))

    
    # Generate a combined motions file
    print([motions_yaml.perform(context) for motions_yaml in motions_files])
    merged_yaml = merge_param_files([motions_yaml.perform(context) for motions_yaml in motions_files])

    # Determine planner
    full_hw_suffix = '_' + f'{arm_type}_' + f'{end_effector_type}_'+ f"{'with-pelvis' if has_pelvis else 'no-pelvis'}_" + f"{'leg' if legs_type!='no-leg' else 'no-leg'}"
    motion_planner_config = PathJoinSubstitution(
                                [pkg_share_dir, 'config', 'motion_planner', f"{arm_type}_specifics", f"motion_planner{full_hw_suffix}.yaml"]
                            )
    print("Motion planner config:", motion_planner_config.perform(context))
    return [SetLaunchConfiguration("motions_file", merged_yaml),
            SetLaunchConfiguration("motion_planner_config", motion_planner_config)]


def generate_launch_description():
    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
