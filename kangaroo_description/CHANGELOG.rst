^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package kangaroo_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.12 (2022-01-10)
-------------------
* Merge branch 'fix_transmission_params' into 'master'
  fix the wrong transmission parameters for hip z
  See merge request robots/kangaroo_robot!24
* fix the wrong transmission parameters for hip z
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.20 (2022-05-04)
-------------------

0.0.19 (2022-05-04)
-------------------

Forthcoming
-----------
* Merge branch 'ft_robot' into 'master'
  Argument to launch robot with F/T sensors or not
  See merge request robots/kangaroo_robot!35
* Remove fixed from sole & ft_sensor joints
* Fix ft sensor transformations
* Add sensor and sole link transformations
* Update homing and launch force_torque_sensor_controller when ft_sensors is true
* Rotate leg_7_link_ft mesh origin
* Argument to launch robot with F/T sensors or not
* Contributors: Adria Roig, Adrià Roig, saikishor

0.0.25 (2023-01-12)
-------------------
* Merge branch 'add_joy_teleop' into 'master'
  added joy_teleop and twist_mux files to kangaroo_bringup
  See merge request robots/kangaroo_robot!33
* changed the default configuration by reducing a bit the leg length
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.24 (2022-12-22)
-------------------
* Merge branch 'add_use_cage_argument' into 'master'
  Added use_case argument to the kangaroo.urdf.xacro and other files
  See merge request robots/kangaroo_robot!34
* add some minor fixes
* Added use_case argument to the kangaroo.urdf.xacro and other files
* Contributors: Sai Kishor Kothakota, saikishor

0.0.23 (2022-10-03)
-------------------
* Fix the homing procedure to retry in case of failure
* wait for 1 sec instead of continously checking
* Contributors: Sai Kishor Kothakota

0.0.22 (2022-09-30)
-------------------

0.0.21 (2022-09-30)
-------------------
* Merge branch 'kangaroo_mpc' into 'master'
  Kangaroo mpc
  See merge request robots/kangaroo_robot!31
* Increase leg length effort limits
* Increase foot inertia for MPC experiments
* 0.0.20
* Update Changelog
* 0.0.19
* Update Changelog
* Contributors: Adria Roig, Sai Kishor Kothakota, saikishor

0.0.18 (2022-03-25)
-------------------
* Added frame aligned to ankle joint_5 axis
* Contributors: enricomingo

0.0.17 (2022-03-14)
-------------------

0.0.16 (2022-03-11)
-------------------
* Merge branch 'walking_controller' into 'master'
  Walking controller
  See merge request robots/kangaroo_robot!10
* Increase firction of the foot
* Contributors: Adria Roig, saikishor

0.0.15 (2022-03-11)
-------------------
* update the reduced collision meshes of kangaroo
* Contributors: Sai Kishor Kothakota

0.0.14 (2022-03-11)
-------------------
* Add missing installation homing script
* Contributors: Adria Roig

0.0.13 (2022-01-26)
-------------------
* Merge branch 'master' of gitlab:robots/kangaroo_robot
* Fix wrong dt for Gazebo simulation
* 0.0.12
* Update Changelog
* Merge branch 'fix_transmission_params' into 'master'
  fix the wrong transmission parameters for hip z
  See merge request robots/kangaroo_robot!24
* fix the wrong transmission parameters for hip z
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.11 (2021-12-28)
-------------------
* Merge branch 'master' of gitlab:robots/kangaroo_robot
* Fix IMU wrong orientation
* Solved issue #1 regarding improving homing procedure. Still something
  more can be done in order to use it as a service everytime is needed.
* Tune torque control params
* Contributors: Adria Roig, enricomingo

0.0.10 (2021-11-22)
-------------------
* Merge branch 'homing_procedure' into 'master'
  Homing procedure
  See merge request robots/kangaroo_robot!23
* Added homing script (as python node) procedure
* Removed call to set configuration in gazebo.launch file
* Contributors: Adria Roig, enricomingo

0.0.9 (2021-11-18)
------------------
* Merge branch 'play_motion_setup' into 'master'
  Play motion setup
  See merge request robots/kangaroo_robot!19
* Updated the crane URDF to be similar to that of the TALOS
* Updtae the collision blacklist and the default floating base position
* Merge branch 'kangaroo_leg_state' into 'master'
  added the leg state transmission
  See merge request robots/kangaroo_robot!22
* added the leg state transmission
* Merge branch 'master' of gitlab:robots/kangaroo_robot
* fixed base hight
* Add femur and knee joints in default configuration
* Merge branch 'torque_control_rebased' into 'master'
  Added files to run kangaroo model in CartesI/O. Notice that: to have the model...
  See merge request robots/kangaroo_robot!21
* Changes to fix issues with tf
* Increase max effort
* Changes for run torque control on the real robot
* Updated Kangaroo model with base_link with cage. Added possibility to use also old model without cage
* added missing wolrd file
* removed comment from xacro
* when using use_mimic true the old masses and inertias are now used
* passed use_mimic option to all nodes. set initial config for use_mimic
  false but does not work
* added closed kinematic chain joint for gazebo when use_mimic is false
* removed useless mesh
* using link5 collision mesh for visualization
* added clenaed leg_5_link mesh
* updated frames according to data sent to Pau
* Removed kangaroo.urdf. Now for CartesI/O the default knagaroo.urdf.xacro is included in kangaroo_cartesio.urdf.xacro and loaded in CartesI/O with disabled mimic
* added use_mimic parameter to enable/disable mimic joints
* small fix in ankles + added foot frames in the corners
* roll ankle joint is not a problem (RBDL just complain but it works)
* Added files to run kangaroo model in CartesI/O. Notice that: to have the model loaded in RBDL the foot roll joint axis has been modified to being unit!
* Added frame located at the tip of the knee link. Needs to be validated against CAD!
* Contributors: Adria Roig, EnricoMingo, Sai Kishor Kothakota, enricomingo

0.0.8 (2021-09-10)
------------------
* Merge branch 'hip_z_implementation' into 'master'
  Hip z implementation
  See merge request robots/kangaroo_robot!17
* remove commented transmission
* Adding hip z custom transmission
* Contributors: narcismiguel, saikishor

0.0.7 (2021-09-07)
------------------

0.0.6 (2021-09-06)
------------------
* added the kangaroo_transmissions exec dependency
* Contributors: Sai Kishor Kothakota

0.0.5 (2021-09-03)
------------------
* add missing install rule of launch folder
* Contributors: Sai Kishor Kothakota

0.0.4 (2021-09-02)
------------------
* Update the transmission plugin names
* Contributors: Sai Kishor Kothakota

0.0.3 (2021-08-30)
------------------
* Merge branch 'enable_ankle_transmission' into 'master'
  enable the ankle transmission on the real robot
  See merge request robots/kangaroo_robot!12
* added missing urdf_test dependency
* fix the kangaroo_description tests
* added test dependency of the rostest
* enable the ankle transmission on the real robot
* Contributors: Sai Kishor Kothakota, victor

0.0.2 (2021-08-30)
------------------
* Merge branch 'kangaroo_wbc' into 'master'
  Kangaroo wbc
  See merge request robots/kangaroo_robot!11
* fix the parameters of the hip
* Uncomment femur meshes for visualization
* Merge branch 'dcm_kangaroo' of gitlab:robots/kangaroo_robot into dcm_kangaroo
* Uncomment transmission for kangaroo pal_physics_simulator
* added extra collision blacklist links
* reduce the default floating base position
* uncomment the kangaroo_leg_length_actuator_transmission in transmission xacro
* Change negative axis of rotation
* Fix duplicated leg in transmission
* Start without controllers by default
* Merge branch 'master' of gitlab:robots/kangaroo_robot
* Merge branch 'default_configuration_loading' into 'master'
  load the default configuration of the robot
  See merge request robots/kangaroo_robot!9
* load the default configuration of the robot
* Remove tibia link nad mimic joint
* Add collision meshes for knee_link and femur_link
* Merge branch 'collision_parameters' into 'master'
  added kangaroo minimal collision parameters
  See merge request robots/kangaroo_robot!8
* added kangaroo minimal collision parameters
* Fix transformation of sole link
* Add missing tag for F/T sensor
* Add F/T sensor
* Update imu transformation
* Fix primatic model. Add IMU. Tune PIDS
* Change to prismatic model with mimic joints
* Inertial modifcations for torso + base link
* fix COM displaced in y axis
* Merge branch 'kangaroo_lower_body_with_leg_length' into 'master'
  Kangaroo lower body with leg length
  See merge request robots/kangaroo_robot!6
* Change masses and inertias for prismatic joint
* added leg length simple transmission
* Update the gazebo and position controllers launch file
* Update the upload and display launch files
* Update URDF to use the complex model (prismatic + dynamic model)
* added changes of single URDF with leg length and dynamic model
* Merge branch 'kangaroo_lower_body_prismatic' into 'master'
  Kangaroo lower body prismatic
  See merge request robots/kangaroo_robot!5
* Merge branch 'kangaroo_lower_body' into 'master'
  Kangaroo lower body
  See merge request robots/kangaroo_robot!4
* Update the new PID gains and the initial joint positions for dynamic model
* Tune PIDs and update the leg 2 position for the new changes of Torso
* Modified the start position of joint 2 of the leg
* Added friction parameters to the leg
* Fix mistake introduced by rebase
* Fix ankle position with respect to the leg lenght
* Remove collision shape of primsatic moving part
* update effort and velocity limit for primsatic model
* Merge branch 'lower_body_with_torso' into 'kangaroo_lower_body_prismatic'
  Updated base_link information with torso meshes and data
  See merge request robots/kangaroo_robot!3
* Updated base_link information with torso meshes and data
* replace tabs by spaces in the files
* add different pids values when simulating in contact
* automatically unpause gazebo when model is spawned
* Clean the way different files are loaded depending on prismatic arg
* Add initial joint position for real model
* WIP: spawn the robot with the leg extended
* Update the base position with freeflying base
* Add different pids config file for prismatic model
* Add 'fixed_base' argument to fixe the base_link or not
  enable_crane now only add the collision shape of the crane
* Add conditionnal block in leg.urdf.xacro for the gazebo parameters depending on the primsatic parameter
* minor fixes to maintain the naming sequence
* extend the prismatic argument to the display.launch
* Update prismatic leg model to avoid change rotation of the joint frame
* Use only one file for both leg type with conditionnal blocks
* add the prismatic parameter to gazebo.launch and upload.launch
* update leg_transmission.xacro to use the 'prismatic' parameter
* Add leg_prismatic.urdf and parameter 'prismatic' to load it
* commit a rviz config version
* add the new ankle urdf macro to the leg
* split ankle into separate urdf files
* Choose the arg simulation and forward the argument to xacro
* Updated the leg xacro to use the transmission according to the arg simulation
* added the rest the main transmission for rest of the joints
* change the limits of the joints of hip yaw
* Start the simulation unpaused
* When enable crane option is parsed, use the world link rather than parsing up the crane model
* add the initial version of gazebo.launch file
* added the missing info of the effort and velocity limits in the URDF
* add simple transmission macro to the URDF
* add missing gazebo include and materials
* add the pending gazebo reference info
* use the simple transmission for the simulation
* Update transmission model info
* Update display.launch to use upload.launch to load the parameters
* Update the URDF to use the option of crane
* Invert the min and max joint values of the leg_3 joint
* Update the URDF configuration with limits w.r.t to kangaroo_leg_specifics
* fix the issue with the leg_3_link mesh
* Update URDF with new meshes and zero at crouched position
* added meshes and display launch files
* Added kangaroo leg lowerbody URDF configuration
* First commit
* Contributors: Adria Roig, Luca Marchionni, Pierre Fernbach, Sai Kishor Kothakota, saikishor, victor
