^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package kangaroo_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
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
