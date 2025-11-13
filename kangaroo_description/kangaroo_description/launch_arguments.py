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
from launch.actions import DeclareLaunchArgument as DLA
from launch_pal.arg_utils import parse_launch_args_from_yaml
from ament_index_python.packages import get_package_share_directory


@dataclass(frozen=True)
class KangarooArgs:
    """This dataclass contains launch arguments for Kangaroo."""

    __robot_name = "kangaroo"
    __pkg_dir = get_package_share_directory(f"{__robot_name}_description")
    __arg_creator = parse_launch_args_from_yaml(
        f"{__pkg_dir}/config/{__robot_name}_configuration.yaml"
    )

    legs_type: DLA = __arg_creator.get_argument("legs_type")
    has_pelvis: DLA = __arg_creator.get_argument("has_pelvis")
    has_head: DLA = __arg_creator.get_argument("has_head")
    arm_type: DLA = __arg_creator.get_argument("arm_type")
    end_effector_type: DLA = __arg_creator.get_argument("end_effector_type")
    fixation_type: DLA = __arg_creator.get_argument("fixation_type")
    collision_type: DLA = __arg_creator.get_argument("collision_type")
    use_mimic: DLA = __arg_creator.get_argument("use_mimic")
    sim_type: DLA = __arg_creator.get_argument("sim_type")
