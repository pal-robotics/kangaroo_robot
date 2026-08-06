^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package kangaroo_bringup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.14.1 (2026-08-06)
-------------------
* Remove unused dependency kangaroo_moveit_config
* Contributors: Noel Jimenez

2.14.0 (2026-07-30)
-------------------

2.13.2 (2026-07-06)
-------------------

2.13.1 (2026-07-06)
-------------------

2.13.0 (2026-07-05)
-------------------

2.12.1 (2026-07-05)
-------------------

2.12.0 (2026-07-04)
-------------------

2.11.2 (2026-07-03)
-------------------

2.11.1 (2026-07-03)
-------------------

2.11.0 (2026-07-03)
-------------------

2.10.0 (2026-07-01)
-------------------
* Add joystick analyzers
  See merge request robots/kangaroo_robot!155
* Add joystick analyzers
* Contributors: Noel Jimenez

2.9.0 (2026-06-26)
------------------
* Simplify controllers regeneration by dropping leg configuration variants
* Contributors: Isaac Acevedo

2.8.0 (2026-06-25)
------------------
* Change fakeforearm to 4dof with no end effector
* Contributors: Aina

2.7.0 (2026-06-23)
------------------
* Merge branch 'fix/imu_simulation' into 'humble-devel'
  Fix imu simulation
  See merge request robots/kangaroo_robot!143
* Add imu broadcaster arguments for simulation
* Merge branch 'feat/motion/homing' into 'humble-devel'
  Standardize homing motions
  See merge request robots/kangaroo_robot!140
* Rename full_homing motions to homing
* Add homing motion for lower body
* Contributors: Aina, Aina Irisarri, Noel Jimenez, Sai Kishor Kothakota

2.6.1 (2026-06-21)
------------------

2.6.0 (2026-06-18)
------------------
* Add motions for lower body
* Add joystick_teleop module
* Add joy teleop configuration
* Contributors: Noel Jimenez, Sai Kishor Kothakota

2.5.2 (2026-06-12)
------------------

2.5.1 (2026-06-09)
------------------

2.5.0 (2026-06-09)
------------------
* Merge branch 'feat/add_feet_type' into 'humble-devel'
  Add feet type
  See merge request robots/kangaroo_robot!108
* Use same string for pelvis than leg
* No feet_type need it in play_motion2
* Fix argument
* Comment feet_type until using it
* Fix flake8 tests
* Remove legs_type
* Contributors: Aina, Aina Irisarri

2.4.5 (2026-06-04)
------------------

2.4.4 (2026-06-03)
------------------

2.4.3 (2026-05-31)
------------------

2.4.2 (2026-05-29)
------------------

2.4.1 (2026-05-28)
------------------

2.4.0 (2026-05-27)
------------------

2.3.2 (2026-05-19)
------------------

2.3.1 (2026-05-14)
------------------
* Merge branch 'fix/end_effector/arg_parsing' into 'humble-devel'
  Fix end effector arg parsing
  See merge request robots/kangaroo_robot!107
* parse arguments to play_motion2 module
* Fix kangaroo play_motion2 parsing
* Contributors: Sai Kishor Kothakota

2.3.0 (2026-05-12)
------------------
* Merge branch 'feat/rm_cover_ee' into 'humble-devel'
  Remove cover as ee option and just check ee when has_arms is True
  See merge request robots/kangaroo_robot!101
* Fix comments RA8D to RH8D
* Remove cover as ee option and just check ee when has_arms is True
* Merge branch 'feat/add_tests' into 'humble-devel'
  Add tests on bringup pkg
  See merge request robots/kangaroo_robot!100
* Fix pep257 tests
* Add tests and solve flake8
* Merge branch 'fix/kangaroo_description' into 'humble-devel'
  Fix/kangaroo description
  See merge request robots/kangaroo_robot!98
* Add ft sensors
* Merge branch 'feat/move_arm' into 'humble-devel'
  Move arm to pal_sea_arm_description
  See merge request robots/kangaroo_robot!97
* Split end effectors into sides
* Merge branch 'fix/remove-prints' into 'humble-devel'
  Remove leftover prints
  See merge request robots/kangaroo_robot!96
* Remove leftover prints
* Contributors: Aina, Noel Jimenez

2.2.0 (2026-04-14)
------------------

2.1.2 (2026-03-06)
------------------

2.1.1 (2026-03-05)
------------------

2.1.0 (2026-02-25)
------------------
* added kangaroo moveit config dependency
* Contributors: sergiacosta

2.0.1 (2026-02-10)
------------------

2.0.0 (2026-02-04)
------------------
* set last ros1 version
* updated version and metadeta
* renamed default broadcasters launchfile
* added playmotion2 module
* fix files bad naming
* added generation script
* added playmotion launchfile
* change file structure to inherit motions
* created bringup package
* updated packages to ros2
* removed old files
* Contributors: sergiacosta

0.3.0 (2025-11-04)
------------------
* Update Changelog
* added gripper arg to robot launchfile
* added gripper configuration parameters
* updated motions for 7dof arm
* added arm_type argument
* added arm_type and robot_type argument logic
* updated config files for 7dof arm
* Contributors: Sai Kishor Kothakota, sergiacosta

0.2.3 (2025-09-25)
------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.2.2 (2025-09-24)
------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.2.1 (2025-09-23)
------------------
* Update Changelog
* Add demos_mode argument defaulting to true
* define and parse robot_type argument downstream
* Add meta information for the new motions
* Propagate changes from VIVE teleoperation + Automatica + RL
* Contributors: Adria Roig, Sai Kishor Kothakota

0.2.0 (2025-09-15)
------------------
* Update Changelog
* Add run pose and sumo pose of the photoshoot
* first draft
* Contributors: Luca Marchionni, Sai Kishor Kothakota

0.1.18 (2025-05-22)
-------------------
* Update Changelog
* update the robot_type arg
* optimize the bringup with the launch argument robot_type
* Set arguments and launch files for different robot configurations
* 0.1.17
* Update Changelog
* Add pelvis and full_homing play_motion configurations
* adding parameters for pelvis and legs
* remove duplicated motions
* tested motions on the robot for standing up from ground
* Testing on the robot
* Contributors: Adrià Roig, Luca Marchionni, Sai Kishor Kothakota, ileniaperrella

0.1.17 (2025-03-05)
-------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.1.16 (2025-02-03)
-------------------
* Update Changelog
* Contributors: Adrià Roig

0.1.15 (2024-09-30)
-------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.1.14 (2024-09-16)
-------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.1.13 (2024-09-10 12:56)
-------------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.1.12 (2024-09-10 12:17)
-------------------------
* Update Changelog
* Contributors: Adrià Roig

0.1.11 (2024-08-01)
-------------------
* Update Changelog
* Contributors: Adrià Roig

0.1.10 (2024-07-25)
-------------------
* Update Changelog
* Contributors: Adria Roig

0.1.9 (2024-07-16)
------------------
* Update Changelog
* Contributors: Adrià Roig

0.1.8 (2024-07-12)
------------------
* Update Changelog
* Contributors: Adria Roig

0.1.7 (2024-07-11 14:56)
------------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.1.6 (2024-07-11 10:30)
------------------------
* Update Changelog
* Contributors: Adria Roig

0.1.5 (2024-07-09 18:08)
------------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.1.4 (2024-07-09 18:03)
------------------------
* Update Changelog
* Add fake_walking and fake_walking2 play_motion motions
* Open ref_velocity port and change IMU Hw transformation
* Fix the enu transformation of the imu
* fix play_motion range for leg_exploration
* Contributors: Adria Roig, Sai Kishor Kothakota

0.1.3 (2024-04-30)
------------------
* Update Changelog
* Contributors: Adria Roig

0.1.2 (2024-04-19)
------------------
* Update Changelog
* Contributors: Adria Roig

0.1.1 (2024-04-18)
------------------
* Update Changelog
* add version argument to all launch files using upload.launch
* Contributors: Adria Roig, Sai Kishor Kothakota

0.1.0 (2024-04-04)
------------------
* Update Changelog
* Contributors: Adria Roig

0.0.30 (2024-01-10)
-------------------
* Update Changelog
* Contributors: Adria Roig

0.0.29 (2023-11-08)
-------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.0.28 (2023-07-04)
-------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.0.27 (2023-02-07)
-------------------
* Update Changelog
* added the proper configuration of the bota FTs
* add new bringup controllers and use common hardware file based on ft_sensors argument
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.26 (2023-01-17)
-------------------
* Update Changelog
* Remove fixed from sole & ft_sensor joints
* Fix ft sensor transformations
* Update homing and launch force_torque_sensor_controller when ft_sensors is true
* Contributors: Adria Roig, Adrià Roig, Sai Kishor Kothakota

0.0.25 (2023-01-12)
-------------------
* Update Changelog
* added joy_teleop and twist_mux files to kangaroo_bringup
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.24 (2022-12-22)
-------------------
* Update Changelog
* Added use_case argument to the kangaroo.urdf.xacro and other files
* Contributors: Sai Kishor Kothakota

0.0.23 (2022-10-03)
-------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.0.22 (2022-09-30 14:21)
-------------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.0.21 (2022-09-30 10:25)
-------------------------
* Update Changelog
* Add F/T sensors in Gazebo for simplicity in the experiments
* 0.0.20
* Update Changelog
* 0.0.19
* Update Changelog
* added more package dependencies to the packages
* Adapt motion home to real robot limits
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.18 (2022-03-25)
-------------------
* Update changelogs
* Contributors: Narcis Miguel

0.0.17 (2022-03-14)
-------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.0.16 (2022-03-11 12:01)
-------------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.0.15 (2022-03-11 10:24)
-------------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.0.14 (2022-03-11 09:10)
-------------------------
* Update Changelog
* Contributors: Adria Roig

0.0.13 (2022-01-26)
-------------------
* Update Changelog
* Contributors: Adria Roig

0.0.12 (2022-01-10)
-------------------
* Update Changelog
* Contributors: Adria Roig

0.0.11 (2021-12-28)
-------------------
* Update Changelog
* Fix IMU wrong orientation
* Solved issue #1 regarding improving homing procedure. Still something
  more can be done in order to use it as a service everytime is needed.
* Contributors: Adria Roig, enricomingo

0.0.10 (2021-11-22)
-------------------
* Update Changelog
* Mv homing motion to kangaroo motions
* Added files for play_motion homing
* Contributors: Adria Roig, enricomingo

0.0.9 (2021-11-18)
------------------
* Update Changelog
* added kangaroo initial motions
* added the both legs configuration
* added play_motion setup without motions
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.8 (2021-09-10)
------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.0.7 (2021-09-07)
------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.0.6 (2021-09-06)
------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.0.5 (2021-09-03)
------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.0.4 (2021-09-02)
------------------
* Update Changelog
* remove the force torque sensors information
* add the IMU hardware configuration
* Contributors: Sai Kishor Kothakota

0.0.3 (2021-08-30 10:51)
------------------------
* Updated Changelog
* Contributors: Victor Lopez

0.0.2 (2021-08-30 09:26)
------------------------
* Add changelog
* Fix package version
* Adding new pids and ff term ports
* Add F/T sensor
* Fix primatic model. Add IMU. Tune PIDS
* First commit
* Contributors: Adria Roig, Jordan Palacios, Luca Marchionni, Victor Lopez
