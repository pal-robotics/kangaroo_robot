^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package kangaroo_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.14.1 (2026-08-06)
-------------------

2.14.0 (2026-07-30)
-------------------
* Remove default empty option on the side argument
  See merge request robots/kangaroo_robot!169
* Remove default empty option on the side argument
* Contributors: Sai Kishor Kothakota

2.13.2 (2026-07-06)
-------------------
* Change the imu sensor broadcaster to 100 Hz
  See merge request robots/kangaroo_robot!166
* Change the imu sensor broadcaster to 100 Hz
* Contributors: Sai Kishor Kothakota

2.13.1 (2026-07-06)
-------------------

2.13.0 (2026-07-05)
-------------------
* Fix gravity compensation frames and launch
  See merge request robots/kangaroo_robot!164
* Add interface type as an argument for the gravity compensation
* Fix the tip link of the foot
* Contributors: Sai Kishor Kothakota

2.12.1 (2026-07-05)
-------------------

2.12.0 (2026-07-04)
-------------------
* Adding pid gains for force and impedance-current + force interface added
  See merge request robots/kangaroo_robot!160
* Remove commented lines of gains
* Changed to stiffness and dumping
* Adding pid gains for force and impedance-current + force interface added
* Contributors: Sai Kishor Kothakota, antoniomartinez

2.11.2 (2026-07-03)
-------------------
* Add pal_local_joint_control dependency
  See merge request robots/kangaroo_robot!162
* Add pal_local_joint_control dependency
* Contributors: Sai Kishor Kothakota

2.11.1 (2026-07-03)
-------------------

2.11.0 (2026-07-03)
-------------------
* Add force torque sensor related changes
  See merge request robots/kangaroo_robot!157
* Use ft_sensor_broadcaster instead of ft_sensor_controller
* Impedance local joint control for leg length
  See merge request robots/kangaroo_robot!147
* Adding impedance local joint control params
* Contributors: Sai Kishor Kothakota, Óscar Martínez

2.10.0 (2026-07-01)
-------------------
* Kinematic WBC ROS 2 position control parameters
  See merge request robots/kangaroo_robot!119
* Kinematic WBC ROS 2 position control parameters
* gravity compensation controller config
  See merge request robots/kangaroo_robot!154
* Add condition to gravity compensation dependency
* Fix the parameters to the new namespaced changes
* fixed CL frames names
* Add new parameters
* gravity controller - DOES NOT WORK because our controller does not take into account the weight of femur and knee
* Add impedance JTC controllers for legs and pelvis
  See merge request robots/kangaroo_robot!151
* Add impedance JTC controllers for legs and pelvis
* Actuator level leg controller
  See merge request robots/kangaroo_robot!135
* leg controller now accepts arg to define interface level, actuator or joint
* Update JTC goal tolerances + pelvis JTC effort controller
  See merge request robots/kangaroo_robot!153
* add config for pelvis jtc effort controller
* add tolerance for leg length in jtc controllers
* Contributors: Daniel Costanzi, Luca Marchionni, Noel Jimenez, Sai Kishor Kothakota, danielcostanzi, oscarmartinez

2.9.0 (2026-06-26)
------------------
* When parsed activate to False, ignore unload_on_kill option
* Add unload_on_kill and activate argument to default_controllers launch
* Contributors: Sai Kishor Kothakota

2.8.0 (2026-06-25)
------------------
* reverted changes since they are now in a different branch
* leg controller now accepts arg to define interface level, actuator or joint
* Contributors: danielcostanzi

2.7.0 (2026-06-23)
------------------

2.6.1 (2026-06-21)
------------------

2.6.0 (2026-06-18)
------------------
* Add condition no-imu for torso imu
* Add arguments on sensor yaml to add 2 different imus
* Add base_imu on the broadcaster module
* Add broadcaster for the base imu if exists
* Add leg JTC effort base controller
* Contributors: Aina, Sai Kishor Kothakota

2.5.2 (2026-06-12)
------------------

2.5.1 (2026-06-09)
------------------
* Merge branch 'rename/pid_controller/module' into 'humble-devel'
  Rename pid_controllers module to actuators_pid_controller module
  See merge request robots/kangaroo_robot!125
* Rename pid_controllers module to actuators_pid_controller module
* Contributors: Noel Jimenez, Sai Kishor Kothakota

2.5.0 (2026-06-09)
------------------
* Merge branch 'feat/add_ankle_ft' into 'humble-devel'
  Add ankle ft
  See merge request robots/kangaroo_robot!110
* Change is_ankle to location to better scalability
* Fix flake8
* Add ft ankle broadcasters
* Merge branch 'feat/add_feet_type' into 'humble-devel'
  Add feet type
  See merge request robots/kangaroo_robot!108
* Remove feet_type argument on the controllers
* Fix flake8 tests
* Remove legs_type
* Contributors: Aina, Aina Irisarri

2.4.5 (2026-06-04)
------------------

2.4.4 (2026-06-03)
------------------
* Add default_controllers module
* Contributors: Noel Jimenez

2.4.3 (2026-05-31)
------------------
* Merge branch 'fix/pid_controllers' into 'humble-devel'
  PID Controllers
  See merge request robots/kangaroo_robot!117
* Add missing actuator_pid_controllers dependency
* Fix module
* Fix flake8
* Adding PID controllers
* Contributors: Sai Kishor Kothakota, Óscar Martínez

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
* Fix the default controllers launch file
* Contributors: Sai Kishor Kothakota

2.3.0 (2026-05-12)
------------------
* Merge branch 'fix/import' into 'humble-devel'
  Fix LaunchConfiguration import
  See merge request robots/kangaroo_robot!105
* Fix LaunchConfiguration import
* Merge branch 'fix/remove-duplicated' into 'humble-devel'
  Remove duplication from import
  See merge request robots/kangaroo_robot!104
* Remove duplication from import
* Merge branch 'feat/add_tests' into 'humble-devel'
  Feat/add tests
  See merge request robots/kangaroo_robot!99
* Add tests on controller_config
* Merge branch 'fix/kangaroo_description' into 'humble-devel'
  Fix/kangaroo description
  See merge request robots/kangaroo_robot!98
* Change condition for the launch description
* Rename end_effector_side to side
* Use ft_sensor parameter for launch arguments
* Update module arguments
* Add arm configuration and condition for no arm and 4dof
* Add ft sensors
* Merge branch 'feat/move_arm' into 'humble-devel'
  Move arm to pal_sea_arm_description
  See merge request robots/kangaroo_robot!97
* Split end effectors into sides
* Merge branch 'fix/remove-prints' into 'humble-devel'
  Remove leftover prints
  See merge request robots/kangaroo_robot!96
* Remove leftover prints
* Contributors: Aina, Aina Irisarri, Noel Jimenez

2.2.0 (2026-04-14)
------------------

2.1.2 (2026-03-06)
------------------

2.1.1 (2026-03-05)
------------------

2.1.0 (2026-02-25)
------------------
* reduce broadcaster update rate and uncomment the meshes
* test to make inference work
* Contributors: Sai Kishor Kothakota, sergiacosta

2.0.1 (2026-02-10)
------------------

2.0.0 (2026-02-04)
------------------
* set last ros1 version
* updated version and metadeta
* added default broadcasters module
* renamed default broadcasters launchfile
* created logic for leg direct effort controllers
* created default position controllers
* created laucnh files for ros2 controllers
* added controllers config files
* updated packages to ros2
* removed old files
* Contributors: sergiacosta

0.3.0 (2025-11-04)
------------------
* Update Changelog
* Add no control configuration for the gripper joints
* add support for arms_7dof_gripper_no_pelvis in the launcher
* updated actuator_pids
* Add missing full_7dof_gripper condition in the launcher.launch
* fixed robot_type logic for pelvis controller
* updated actuator PID gains
* added controller parameters for gripper finger joint
* added gripper configuration parameters
* Remove the commented args
* Change the motor torque constant
* set test bench gains for leg motors
* updated possible robot configurations
* added local joint for 7dof arm
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
* Fix the arm_right launch local joint control launch file
* Add missing pelvis joints impedance control parameters
* Contributors: Sai Kishor Kothakota

0.2.1 (2025-09-23)
------------------
* Update Changelog
* Change the rate limiter of the leg 1 joints
* Change the  impedance gains of the leg length
* Use the default stiffness and damping used for the walking
* Add demos_mode argument defaulting to true
* Fix the spacing
* Apply 1 suggestion(s) to 1 file(s)
* Try to find the robot_type with path checking
* define and parse robot_type argument downstream
* Propagate changes from VIVE teleoperation + Automatica + RL
* Add ef frames for the WBC
* Contributors: Adria Roig, Sai Kishor Kothakota, ileniaperrella

0.2.0 (2025-09-15)
------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.1.18 (2025-05-22)
-------------------
* Update Changelog
* Simplify the default_controllers launch file
* Remove ft_sensor_estimator from the bringup controller
* Set old impedance gains
* Set arguments and launch files for different robot configurations
* 0.1.17
* Update Changelog
* add parameters of kangaroo-4 tests
* adding parameters for pelvis and legs
* Add torso.launch
* Testing on the robot
* tested with pal_physics_simulator
* Contributors: Adria Roig, Adrià Roig, Luca Marchionni, Sai Kishor Kothakota, ileniaperrella

0.1.17 (2025-03-05)
-------------------
* Update Changelog
* add parameters of kangaroo-4 tests
* Contributors: Sai Kishor Kothakota

0.1.16 (2025-02-03)
-------------------
* Update Changelog
* Contributors: Adrià Roig

0.1.15 (2024-09-30)
-------------------
* Update Changelog
* Change transmission parameters of the leg length
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
* change the default safety parameter for kangaroo-3 as they need tuning
* Contributors: Adrià Roig, Sai Kishor Kothakota

0.1.10 (2024-07-25)
-------------------
* Update Changelog
* add initialization tolerance to the ankle transmission parameters
* Contributors: Adria Roig, Sai Kishor Kothakota

0.1.9 (2024-07-16)
------------------
* Update Changelog
* Contributors: Adrià Roig

0.1.8 (2024-07-12)
------------------
* Update Changelog
* Fix gazebo PID contact gains
* Contributors: Adria Roig, Sai Kishor Kothakota

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
* add missing controller dependencies
* Contributors: Sai Kishor Kothakota

0.1.4 (2024-07-09 18:03)
------------------------
* Update Changelog
* Don't use integral factors for the Hip RPY joints
* Remove extra unused args
* Add FT sensor estimator directly to launch on startup
* Set the zeros properly
* update the leg length position PID gains tuned at TUWien
* Put back all joint torque/force sensor offset to 0 in actuator_parameters_specific_params.yaml
* Enable default safety
* Update configuration files from latest value tested on Kangaroo 3
* Add arguments to enable / disable torque control for specific transmissions
* Fix wrong impedance gain in leg_left_1_joint
* Add new transmission parameters after fix ankle transmission
* delete gravity compensation parameters on restart of controller
* Add torque control gains of kangaroo-3
* Reduce by factor of 100 the integral gain of the position loop for hip actuators
* reduce the position Kp of the leg right 1 motor
* fix the PID parameters to be double
* add actuator_pid_controllers dependency
* added the gains corresponding to the kangaroo 3
* Contributors: Adria Roig, Pierre Fernbach, Sai Kishor Kothakota

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
* Contributors: Adria Roig

0.1.0 (2024-04-04)
------------------
* Update Changelog
* Contributors: Adria Roig

0.0.30 (2024-01-10)
-------------------
* Update Changelog
* Apply transmission_parameters update as per code review
* Parameterize the version of Hip Z installed on the robot and update the parameters
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.29 (2023-11-08)
-------------------
* Update Changelog
* Modify parameters for direct_position_control
* Modify parameters for direct_position_control
* Add parameters for direct_position_control
* Contributors: Adria Roig, Adrià Roig, Sai Kishor Kothakota

0.0.28 (2023-07-04)
-------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.0.27 (2023-02-07)
-------------------
* Update Changelog
* added direct_position_control config and launch files
* added direct_current_control files
* Update the actuator and safety parameters of the joints
* Update the inertia shaping analytic parameters from the robot
* use direct_torque_control instead of no_control in the force_control launch files
* add new bringup controllers and use common hardware file based on ft_sensors argument
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.26 (2023-01-17)
-------------------
* Update Changelog
* Update homing and launch force_torque_sensor_controller when ft_sensors is true
* Contributors: Adrià Roig, Sai Kishor Kothakota

0.0.25 (2023-01-12)
-------------------
* Update Changelog
* update the walking controller parameters as in the robot
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.24 (2022-12-22)
-------------------
* Update Changelog
* add some minor fixes
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
* 0.0.20
* Update Changelog
* update gains and launch files from the robot
* 0.0.19
* Update Changelog
* added more package dependencies to the packages
* added IK plugin
* Contributors: Sai Kishor Kothakota

0.0.18 (2022-03-25)
-------------------
* Update changelogs
* updated parameters, compared with full model
* Contributors: Narcis Miguel

0.0.17 (2022-03-14)
-------------------
* Update Changelog
* Revert contact PIDs to old values
  This reverts commit d66f0b433452aaf0a4c34e11e3435e565833988d.
* Contributors: Sai Kishor Kothakota

0.0.16 (2022-03-11 12:01)
-------------------------
* Update Changelog
* set the position controllers back in default controllers
* update the walking controlle parameters
* update contact PIDs
* Add desired step time parameter
* update gazebo PID gains
* update default controllers launch file
* Added walking controller parameters
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
* fix the wrong transmission parameters for hip z
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.11 (2021-12-28)
-------------------
* Update Changelog
* Fix IMU wrong orientation
* Tune torque control params
* Contributors: Adria Roig

0.0.10 (2021-11-22)
-------------------
* Update Changelog
* Contributors: Adria Roig

0.0.9 (2021-11-18)
------------------
* Update Changelog
* Add torque control in local joint control launcher
* Launch torque control when local joint control type specified
* Fix typo in the torque control launch files
* Tune filter and torque control gains
* update transmission parameters
* Add launch files fro launching toruqe control in both legs
* Add torque offsets + impedance files
* tuned pids
* Add no control parameters
* Changes to fix issues with tf
* Tune torque control in the real robot
* Changes for run torque control on the real robot
* small tuning
* Contributors: Adria Roig, Sai Kishor Kothakota, enricomingo

0.0.8 (2021-09-10)
------------------
* Update Changelog
* param name fix
* Adding hip z custom transmission
* Contributors: Sai Kishor Kothakota, narcismiguel

0.0.7 (2021-09-07)
------------------
* Update Changelog
* remove the launch of non existing current_limit_controllers
* Contributors: Sai Kishor Kothakota

0.0.6 (2021-09-06)
------------------
* Update Changelog
* added effort based joint trajectory controllers configuration
* moved the position joint trajectory config files to position folder
* Contributors: Sai Kishor Kothakota

0.0.5 (2021-09-03)
------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.0.4 (2021-09-02)
------------------
* Update Changelog
* remove the starting of force_torque_sensor_controller
* Contributors: Sai Kishor Kothakota

0.0.3 (2021-08-30 10:51)
------------------------
* Updated Changelog
* Contributors: Victor Lopez

0.0.2 (2021-08-30 09:26)
------------------------
* Add changelog
* Add bs parameters in the actuator parameters
* Increase damping for leg_1_joint
* Remove tibia link nad mimic joint
* Add collision meshes for knee_link and femur_link
* Tune gazebo pids contact gains
* Create actuator parameters yamls
* cleanup the selective_rosparam_loader
* added selective_rosparam_loader launch file
* load the transmission parameters with bringup
* Add F/T sensor
* Fix primatic model. Add IMU. Tune PIDS
* Change to prismatic model with mimic joints
* Update the gazebo pid files with the leg length joints
* remove prismatic model pid files and position controller configuration
* Update the gazebo and position controllers launch file
* added changes of single URDF with leg length and dynamic model
* Update the new PID gains and the initial joint positions for dynamic model
* Tune PIDs and update the leg 2 position for the new changes of Torso
* Tuned the gains a bit for the old mass and inertia of the base_link
* Update pid gains for contact_prismatic
* add different pids values when simulating in contact
* Clean the way different files are loaded depending on prismatic arg
* Add different pids config file for prismatic model
* Update joint_trajectory_controllers for prismatic model regarding the change in the joints names
* update position_controllers.launch to use the 'prismatic' parameter
* added transmission parameters yaml
* tuned PIDs of the gazebo sim
* add the Gazebo joint pids yaml
* launch and load both legs position controllers
* added joint state controller configuration and launch
* added left and right leg joint trajectory controller configuration
* First commit
* Contributors: Adria Roig, Luca Marchionni, Pierre Fernbach, Sai Kishor Kothakota, Victor Lopez
