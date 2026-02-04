^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package kangaroo_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
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
