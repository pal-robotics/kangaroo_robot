^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package kangaroo_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.12 (2022-01-10)
-------------------
* Merge branch 'fix_transmission_params' into 'master'
  fix the wrong transmission parameters for hip z
  See merge request robots/kangaroo_robot!24
* fix the wrong transmission parameters for hip z
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.20 (2022-05-04)
-------------------
* update gains and launch files from the robot
* Contributors: Sai Kishor Kothakota

0.0.19 (2022-05-04)
-------------------
* Merge branch 'fix_package_information' into 'master'
  Fix package information
  See merge request robots/kangaroo_robot!27
* added more package dependencies to the packages
* added IK plugin
* Contributors: Sai Kishor Kothakota, saikishor

Forthcoming
-----------
* Merge branch 'add_joy_teleop' into 'master'
  added joy_teleop and twist_mux files to kangaroo_bringup
  See merge request robots/kangaroo_robot!33
* update the walking controller parameters as in the robot
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.24 (2022-12-22)
-------------------
* Merge branch 'add_use_cage_argument' into 'master'
  Added use_case argument to the kangaroo.urdf.xacro and other files
  See merge request robots/kangaroo_robot!34
* add some minor fixes
* Contributors: Sai Kishor Kothakota, saikishor

0.0.23 (2022-10-03)
-------------------

0.0.22 (2022-09-30)
-------------------

0.0.21 (2022-09-30)
-------------------
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
* Merge branch 'update-leg-params' into 'master'
  updated parameters, compared with full model
  See merge request robots/kangaroo_robot!26
* updated parameters, compared with full model
* Contributors: Narcis Miguel, narcismiguel

0.0.17 (2022-03-14)
-------------------
* Revert contact PIDs to old values
  This reverts commit d66f0b433452aaf0a4c34e11e3435e565833988d.
* Contributors: Sai Kishor Kothakota

0.0.16 (2022-03-11)
-------------------
* Merge branch 'walking_controller' into 'master'
  Walking controller
  See merge request robots/kangaroo_robot!10
* set the position controllers back in default controllers
* update the walking controlle parameters
* update contact PIDs
* Add desired step time parameter
* update gazebo PID gains
* update default controllers launch file
* Added walking controller parameters
* Contributors: Sai Kishor Kothakota, saikishor

0.0.15 (2022-03-11)
-------------------

0.0.14 (2022-03-11)
-------------------

0.0.13 (2022-01-26)
-------------------
* Merge branch 'master' of gitlab:robots/kangaroo_robot
* 0.0.12
* Update Changelog
* Merge branch 'fix_transmission_params' into 'master'
  fix the wrong transmission parameters for hip z
  See merge request robots/kangaroo_robot!24
* fix the wrong transmission parameters for hip z
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.11 (2021-12-28)
-------------------
* Fix IMU wrong orientation
* Tune torque control params
* Contributors: Adria Roig

0.0.10 (2021-11-22)
-------------------

0.0.9 (2021-11-18)
------------------
* Add torque control in local joint control launcher
* Launch torque control when local joint control type specified
* Fix typo in the torque control launch files
* Merge branch 'master' of gitlab:robots/kangaroo_robot
* Tune filter and torque control gains
* update transmission parameters
* Add launch files fro launching toruqe control in both legs
* Add torque offsets + impedance files
* tuned pids
* Merge branch 'torque_control_rebased' into 'master'
  Added files to run kangaroo model in CartesI/O. Notice that: to have the model...
  See merge request robots/kangaroo_robot!21
* Add no control parameters
* Changes to fix issues with tf
* Tune torque control in the real robot
* Changes for run torque control on the real robot
* small tuning
* Contributors: Adria Roig, Sai Kishor Kothakota, enricomingo

0.0.8 (2021-09-10)
------------------
* Merge branch 'hip_z_implementation' into 'master'
  Hip z implementation
  See merge request robots/kangaroo_robot!17
* param name fix
* Adding hip z custom transmission
* Contributors: narcismiguel, saikishor

0.0.7 (2021-09-07)
------------------
* remove the launch of non existing current_limit_controllers
* Contributors: Sai Kishor Kothakota

0.0.6 (2021-09-06)
------------------
* Merge branch 'current_controllers' into 'master'
  moved the position joint trajectory config files to position folder
  See merge request robots/kangaroo_robot!14
* added effort based joint trajectory controllers configuration
* moved the position joint trajectory config files to position folder
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.5 (2021-09-03)
------------------

0.0.4 (2021-09-02)
------------------
* Merge branch 'imu_and_other_configuration' into 'master'
  Imu and other configuration
  See merge request robots/kangaroo_robot!13
* remove the starting of force_torque_sensor_controller
* Contributors: Jordan Palacios, Sai Kishor Kothakota

0.0.3 (2021-08-30)
------------------

0.0.2 (2021-08-30)
------------------
* Merge branch 'kangaroo_wbc' into 'master'
  Kangaroo wbc
  See merge request robots/kangaroo_robot!11
* Add bs parameters in the actuator parameters
* Increase damping for leg_1_joint
* Remove tibia link nad mimic joint
* Add collision meshes for knee_link and femur_link
* Tune gazebo pids contact gains
* Merge branch 'master' of gitlab:robots/kangaroo_robot
* Create actuator parameters yamls
* cleanup the selective_rosparam_loader
* Merge branch 'simulator_setup' into 'master'
  Simulator setup
  See merge request robots/kangaroo_robot!7
* added selective_rosparam_loader launch file
* load the transmission parameters with bringup
* Add F/T sensor
* Fix primatic model. Add IMU. Tune PIDS
* Change to prismatic model with mimic joints
* Merge branch 'kangaroo_lower_body_with_leg_length' into 'master'
  Kangaroo lower body with leg length
  See merge request robots/kangaroo_robot!6
* Update the gazebo pid files with the leg length joints
* remove prismatic model pid files and position controller configuration
* Update the gazebo and position controllers launch file
* added changes of single URDF with leg length and dynamic model
* Merge branch 'kangaroo_lower_body_prismatic' into 'master'
  Kangaroo lower body prismatic
  See merge request robots/kangaroo_robot!5
* Merge branch 'kangaroo_lower_body' into 'master'
  Kangaroo lower body
  See merge request robots/kangaroo_robot!4
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
* Contributors: Adria Roig, Luca Marchionni, Pierre Fernbach, Sai Kishor Kothakota, victor
