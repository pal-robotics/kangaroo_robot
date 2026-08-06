^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package kangaroo_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.14.1 (2026-08-06)
-------------------

2.14.0 (2026-07-30)
-------------------
* Fix leg_1_link mesh
  See merge request robots/kangaroo_robot!168
* Fix leg_1_link mesh
* Contributors: Aina Irisarri, Isaac Acevedo

2.13.2 (2026-07-06)
-------------------

2.13.1 (2026-07-06)
-------------------
* Add force to the idle_mode_on_stop_interfaces
  See merge request robots/kangaroo_robot!165
* Add force to the idle_mode_on_stop_interfaces
* Contributors: Sai Kishor Kothakota

2.13.0 (2026-07-05)
-------------------

2.12.1 (2026-07-05)
-------------------
* Modify the limits of the leg length
  See merge request robots/kangaroo_robot!163
* Modify the limits of the leg length
* Contributors: Sai Kishor Kothakota

2.12.0 (2026-07-04)
-------------------
* Adding pid gains for force and impedance-current + force interface added
  See merge request robots/kangaroo_robot!160
* Minor fix
* Adding pid gains for force and impedance-current + force interface added
* Contributors: Sai Kishor Kothakota, antoniomartinez

2.11.2 (2026-07-03)
-------------------
* Change the foot sole to a simpler and ligher one
  See merge request robots/kangaroo_robot!161
* Change the foot sole to a simpler and ligher one
* Contributors: Sai Kishor Kothakota

2.11.1 (2026-07-03)
-------------------
* Ankle bar frames were swapped, now they are correct
  See merge request robots/kangaroo_robot!159
* ankle bar frames were swapped, now they are correct
* Contributors: Daniel Costanzi, Sai Kishor Kothakota

2.11.0 (2026-07-03)
-------------------
* Suppress overrun warnings for the microstrain IMU
  See merge request robots/kangaroo_robot!158
* Suppress overrun warnings for the microstrain IMU
* Add force torque sensor related changes
  See merge request robots/kangaroo_robot!157
* Add missing mujoco tags for force and torque
* Contributors: Sai Kishor Kothakota

2.10.0 (2026-07-01)
-------------------
* Rename sole frame for detachable feet type so it has the same name as the fixed version
  See merge request robots/kangaroo_robot!156
* Rename sole frame for detachable feet type so it has the same name as the fixed version
* Disable joint limiting for the effort interface
  See merge request robots/kangaroo_robot!152
* Disable joint limiting for the effort interface
* Add closed loop frames to the feet to reuse for full model
  See merge request robots/kangaroo_robot!150
* fixed if condition
* add cloesd loop frames to the foot conditionally
* Contributors: Daniel Costanzi, Pierre Fernbach, Sai Kishor Kothakota

2.9.0 (2026-06-26)
------------------
* Remove pal_mujoco_scenes dependency
* Contributors: Sai Kishor Kothakota

2.8.0 (2026-06-25)
------------------
* Change fakeforearm to 4dof with no end effector
* fixed name of the ft link so that it coherent with broadcaster config
* Contributors: Aina, Daniel Costanzi

2.7.0 (2026-06-23)
------------------
* Merge branch 'fix/detachable_covers' into 'humble-devel'
  Replace feet and ankle stl with covers and axis fixed
  See merge request robots/kangaroo_robot!145
* Replace values to use deg_to_rad macro
* Change feet angle
* Replace stl with covers and axis fixed
* Merge branch 'filter/mujoco/collision_exclude' into 'humble-devel'
  Filter out the collision exclude when used with --fuse
  See merge request robots/kangaroo_robot!142
* Add pairs for fixation type fixed
* Set ankle attach joint to fixed
* Donot decompose leg 7 link as we use pregenerated mjcfs
* Filter out the collision exclude when used with --fuse
* Merge branch 'fix/imu_simulation' into 'humble-devel'
  Fix imu simulation
  See merge request robots/kangaroo_robot!143
* Add imu tags for mujoco
* Merge branch 'fix/mj_tags' into 'humble-devel'
  Fix renamed IMU mujoco tags
  See merge request robots/kangaroo_robot!141
* Fix renamed IMU mujoco tags
* Do not initialize rclpy, if already initialized by other entities
* Contributors: Aina, Aina Irisarri, Noel Jimenez, Sai Kishor Kothakota

2.6.1 (2026-06-21)
------------------
* Merge branch 'condition/absolute_position' into 'humble-devel'
  Don't add absolute position state interface for simulation
  See merge request robots/kangaroo_robot!137
* Don't add absolute position state interface for simulation
* Contributors: Sai Kishor Kothakota

2.6.0 (2026-06-18)
------------------
* Fix low data reporting of microstrain base IMU
* Change data_rate to 1000
* Change data_rate_hz to 1000
* Change imu's baudrate
* Fix sensor name
* Rename device port
* Create imu macro
* Change io device to be define
* Change data rate to effective one
* Add no imu option for torso imu
* Add tag for base imu in mujoco
* Add broadcaster for the base imu if exists
* Add imus on the urdf
* Add 2 imu models
* Revert "Merge branch 'fix/show_home_position' into 'humble-devel'"
  This reverts merge request !121
* Enable absolute position interface on kangaroo
* Fix show launcher
* Contributors: Aina, Aina Irisarri, Carles Lopez, Carles Lopez Parera, antoniomartinez

2.5.2 (2026-06-12)
------------------
* Merge branch 'fix/pelvis_axis' into 'humble-devel'
  Fix the pelvis axis to maintain consistency with ROS 1
  See merge request robots/kangaroo_robot!126
* Fix the pelvis axis to maintain consistency with ROS 1
* Contributors: Noel Jimenez, Sai Kishor Kothakota

2.5.1 (2026-06-09)
------------------

2.5.0 (2026-06-09)
------------------
* Merge branch 'fix/mujoco_sim' into 'humble-devel'
  Fix mujoco tags
  See merge request robots/kangaroo_robot!111
* Remove the duplicate interfaces information defined in the transmissions
* Add missing kangaroo leg state and command interface
* Extend condition to also hceck for end_effector_left
* Add end effectors sides on mujoco tags
* Merge branch 'feat/add_ankle_ft' into 'humble-devel'
  Add ankle ft
  See merge request robots/kangaroo_robot!110
* Add ankle ft to launch and module
* Fix arguments ros2_control urdf
* Add ros2 ft sensor for ankle
* Add ankle ft side arguments
* Merge branch 'fix/rm_arm_meshes' into 'humble-devel'
  Remove arm meshes
  See merge request robots/kangaroo_robot!109
* Remove arm meshes
* Merge branch 'feat/add_feet_type' into 'humble-devel'
  Add feet type
  See merge request robots/kangaroo_robot!108
* Fix detachable feet joints
* Add argument on the module
* Remove legs_type
* Add both types of feet
* Remove leg_type and add fett_type
* Contributors: Aina, Aina Irisarri, Noel Jimenez, Sai Kishor Kothakota

2.4.5 (2026-06-04)
------------------
* Fix pelvis 1 axis
* Contributors: Aina

2.4.4 (2026-06-03)
------------------

2.4.3 (2026-05-31)
------------------

2.4.2 (2026-05-29)
------------------
* Change home position for show file
* Contributors: Aina

2.4.1 (2026-05-28)
------------------
* Add kangaroo_transmissions missing dependency
* Contributors: Noel Jimenez

2.4.0 (2026-05-27)
------------------
* Merge branch 'update/robot_model' into 'humble-devel'
  Model with updated masses, origin and inertias
  See merge request robots/kangaroo_robot!113
* Fix the missing inertial tag
* Update torso link mass and inertial properties
* update pelvis_link mass and inertial parameters
* Update base_link mass and inertial properties
* Update the mass and the inertial elements of leg links
* Contributors: Sai Kishor Kothakota

2.3.2 (2026-05-19)
------------------
* Merge branch 'fix/pelvis_trans' into 'humble-devel'
  Use differential transmission for  pelvis joints
  See merge request robots/kangaroo_robot!112
* Readding missing pelvis trans
* Contributors: Sai Kishor Kothakota, Óscar Martínez

2.3.1 (2026-05-14)
------------------

2.3.0 (2026-05-12)
------------------
* Merge branch 'amr/test-new-transmissions' into 'humble-devel'
  Adapt urdf to new kangaroo transmissions
  See merge request robots/kangaroo_robot!103
* Apply merge request review suggestions
  Co-authored-by: Sai Kishor Kothakota <sai.kishor@pal-robotics.com>
* enable nl trans for all the joints
* Changes to make work hipxy and leg length transmissions
* Test hip-z on actual robot
* Testing custom transmission or robot instead of simple hipz
* Added custom transmission xacros for ros2 testing
* Merge branch 'feat/rm_cover_ee' into 'humble-devel'
  Remove cover as ee option and just check ee when has_arms is True
  See merge request robots/kangaroo_robot!101
* Fix comments RA8D to RH8D
* Remove cover as ee option and just check ee when has_arms is True
* Merge branch 'feat/add_tests' into 'humble-devel'
  Feat/add tests
  See merge request robots/kangaroo_robot!99
* Add tests
* Fix pep257 tests
* Fix uncrustify
* Fix flake8 tests
* Missing blank last line
* Fix copyrights
* Add tests
* Merge branch 'fix/kangaroo_description' into 'humble-devel'
  Fix/kangaroo description
  See merge request robots/kangaroo_robot!98
* Add ft sensors
* Fix default end effectors
* Fix module arguments
* Merge branch 'feat/move_arm' into 'humble-devel'
  Move arm to pal_sea_arm_description
  See merge request robots/kangaroo_robot!97
* Fix includes for end effectors
* Add condition for no arm and no left end effector cover
* Split end effectors into sides
* Move arm to pal_sea_arm_description
* Contributors: Aina, Daniel Costanzi, Noel Jimenez, Sai Kishor Kothakota, antoniomartinez

2.2.0 (2026-04-14)
------------------
* using rear instead of back
* update urdf and cleaning
* added properties to make it compatible with last changes of pal_urdf_utils
* add torso cameras
* Contributors: Andrea Capodacqua, andreacapodacqua

2.1.2 (2026-03-06)
------------------
* Merge branch 'fix/add_orientus_imu' into 'humble-devel'
  Add orientus imu
  See merge request robots/kangaroo_robot!94
* Adding orientus ros2_control hardware
* Contributors: Jordan Palacios, Sai Kishor Kothakota

2.1.1 (2026-03-05)
------------------
* Renaming robot_state_publisher module file
  As it is, there is a name clash with:
  pal_sea_arm_description/module/10_robot_state_publisher.yaml
  Both are installed in kangaroo
* Contributors: Jordan Palacios

2.1.0 (2026-02-25)
------------------
* removed unecessary comments
* updated dt to 2khz
* commented local model
* reduce broadcaster update rate and uncomment the meshes
* updated xml path
* test to make inference work
* Contributors: Sai Kishor Kothakota, sergiacosta

2.0.1 (2026-02-10)
------------------
* Expose safety interface
* Contributors: Noel Jimenez

2.0.0 (2026-02-04)
------------------
* set last ros1 version
* updated version and metadeta
* added logic for simple transmissions loading sim/real
* added ros2 control pid gains and command interfaces
* improved fixed base logic
* use keyframe to initialize base position
* added is_async param to robot_system
* updated afinity ros2control parameter
* added simple transmissions to all joints
* added ros2control logic for sim and real robot
* added robot state publisher module
* updated legs initial position
* updated initial position
* updated wrong comment
* updated ros2 actuator logic
* handling floating base from launchfile
* updated logic actuator simtype
* changed default robot config
* removed unnecesary meshes
* fixed plugin name
* added free floating base joint by defauladded free floating base joint by default
* added decompose parameter for feet mesh
* Updated mujoco tags in urdf
* fixed fixed base logic
* created logic for leg direct effort controllers
* improved xacro logic for mujoco tags
* removed temp code
* updated ros2control tags
* updated rviz config
* added tags for pal_mujoco_model_loader tool
* created ros2 control xacro files
* created ros2 launchfiles
* added blackboard node
* added python modules
* set parameters for description
* updated meshes
* updated URDF with new configurations
* updated packages to ros2
* removed old files
* Contributors: Ortisa Poci, sergiacosta

0.3.0 (2025-11-04)
------------------
* Update Changelog
* Remove comment arm 5 reflection
* updated arm 5 joint limits
* updated collision excludes for gripper
* updated transmission tags for gripper
* changed ros transmission sintax
* set initial position for gripper joint
* added gripper configuration parameters
* changed initial position
* fixed joint limits and directions
* updated exclude collision list
* added xacro arguments for 7dof arm
* added 7dof arm
* updated arm meshes
* added arm_type and robot_type argument logic
* updated config files for 7dof arm
* Contributors: Sai Kishor Kothakota, sergiacosta

0.2.3 (2025-09-25)
------------------
* Update Changelog
* updated handle inertia
* updated exclude collision list
* Contributors: Sai Kishor Kothakota, sergiacosta

0.2.2 (2025-09-24)
------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.2.1 (2025-09-23)
------------------
* Update Changelog
* Cleaner way to set ef_frames
* Setting properly ef frames (hardcoded way prior fix on parent tfs)
* Propagate changes from VIVE teleoperation + Automatica + RL
* Add ef frames for the WBC
* Contributors: Adria Roig, Sai Kishor Kothakota, antoniomartinez, ileniaperrella

0.2.0 (2025-09-15)
------------------
* Update Changelog
* Small typo fix
* Fix torso mesh normals
* Fix torso mesh and add material for better coloring in rviz
* first draft
* Disable waist protector collisions
* Contributors: Luca Marchionni, Sai Kishor Kothakota, antoniomartinez, ileniaperrella

0.1.18 (2025-05-22)
-------------------
* Update Changelog
* update the robot_type arg
* Set old impedance gains
* Set arguments and launch files for different robot configurations
* 0.1.17
* Update Changelog
* adding parameters for pelvis and legs
* Add torso.launch
* differential transmission gear ration tested on robot kangaroo-2
* fix tests
* different base_link with and without pelvis, split torso from arm covers
* tested motions on the robot for standing up from ground
* Testing on the robot
* fix urdf for arm mesh and inertia
* rexported mesh from mechanics
* tested with pal_physics_simulator
* Arms param and added pelvis transmission
* pelvis param and removed version 2022, default to 2023
* Added torso and pelvis without params
* Contributors: Adria Roig, Adrià Roig, Luca Marchionni, Sai Kishor Kothakota, ileniaperrella

0.1.17 (2025-03-05)
-------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.1.16 (2025-02-03)
-------------------
* Update Changelog
* Set correct effort joint limits
* Contributors: Adrià Roig, sergiacosta

0.1.15 (2024-09-30)
-------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.1.14 (2024-09-16)
-------------------
* Update Changelog
* revert the meshes to version 0.1.11 to fix unstable simulation behaviour
* Contributors: Sai Kishor Kothakota

0.1.13 (2024-09-10 12:56)
-------------------------
* Update Changelog
* (fix) correct torso position w.r.t. base link
* Contributors: PepMS, Sai Kishor Kothakota

0.1.12 (2024-09-10 12:17)
-------------------------
* Update Changelog
* Update changes in Hip Z
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
* update the order of switching controllers in homing script of Gazebo
* Contributors: Adrià Roig, Sai Kishor Kothakota

0.1.8 (2024-07-12)
------------------
* Update Changelog
* Fix the post homing reset position
* Contributors: Adria Roig, Sai Kishor Kothakota

0.1.7 (2024-07-11 14:56)
------------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.1.6 (2024-07-11 10:30)
------------------------
* Update Changelog
* Add 20 deg angle change to the old ankle model
* Contributors: Adria Roig, Sai Kishor Kothakota

0.1.5 (2024-07-09 18:08)
------------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.1.4 (2024-07-09 18:03)
------------------------
* Update Changelog
* calibrated camera position for better overlapping with torso front camera
* Add velocity interface
* use the roll joint as the parent to the roll aligned joint
* change the ankle pitch joint to be aligned with the ankle roll link
* Fix the leg sole link parent link
* Fix the ankle sole link position for the new soles
* Fix the collision link orientation
* Set the link 5 to the aligned one by default
* apply angle with macro
* fix the hip roll-pitch transmission parameters
* Add the new collision pairs with the cameras into blacklist
* Add removed imu link and modify the placement of macros torso and waist
* Fix typo in waist
* Added gazebo simulator plugins
* Added realsense2 description dependency
* Fix back cameras tf
* Change wrist to waist
* Fix xacro macro urdf
* Added the kangaroo cameras
* Contributors: Adria Roig, Luca Marchionni, Sai Kishor Kothakota, sergiomoyano

0.1.3 (2024-04-30)
------------------
* Update Changelog
* reduce the range of the ankle
* Set the proper IMU transform for the new model 2023
* Set the IMU definition for base version 2022
* reduce the hip pitch range
* Contributors: Adria Roig, Sai Kishor Kothakota

0.1.2 (2024-04-19)
------------------
* Update Changelog
* update the hipz with new version
* Contributors: Adria Roig, Sai Kishor Kothakota

0.1.1 (2024-04-18)
------------------
* Update Changelog
* Dependencies needed for the gazebo simulation of both the versions
* add version argument to all launch files using upload.launch
* add version to the testing of URDF
* added new ankle version changes to the URDF
* move the original ankle.urdf.xacro to be version 2022
* Contributors: Adria Roig, Sai Kishor Kothakota

0.1.0 (2024-04-04)
------------------
* Update Changelog
* remove the torso link convex copy
* parse the kangaroo version from the upload.launch directly
* update the leg collision links without bars for the new leg description
* Update the collision parameters of the new kangaroo description
* update the ankle inertia and collision info when considering the ft_sensor
* fix the version hardcoded value of macro
* hardcode hipz model inside the leg urdf xacros
* added the new version of the base link and torso
* add version argument into the base link xacro
* move the base link to use the version 2022
* update the ankle links mass, inertia and meshes
* update link 3 without the ball screws just for visualization purpose
* update femur and tibia link properties information (mass, inertia and meshes)
* update hip roll and pitch inertia, mass properties and meshes
* update hip z inertia, mass properties and the mesh file
* added version arg to the URDF and create different leg URDFs
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.30 (2024-01-10)
-------------------
* Update Changelog
* Parameterize the version of Hip Z installed on the robot and update the parameters
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.29 (2023-11-08)
-------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.0.28 (2023-07-04)
-------------------
* Update Changelog
* fix the ft link frame as per the datasheet
* Contributors: Sai Kishor Kothakota

0.0.27 (2023-02-07)
-------------------
* Update Changelog
* Contributors: Adria Roig

0.0.26 (2023-01-17)
-------------------
* Update Changelog
* Remove fixed from sole & ft_sensor joints
* Fix ft sensor transformations
* Add sensor and sole link transformations
* Update homing and launch force_torque_sensor_controller when ft_sensors is true
* Rotate leg_7_link_ft mesh origin
* Argument to launch robot with F/T sensors or not
* Contributors: Adria Roig, Adrià Roig, Sai Kishor Kothakota

0.0.25 (2023-01-12)
-------------------
* Update Changelog
* changed the default configuration by reducing a bit the leg length
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.24 (2022-12-22)
-------------------
* Update Changelog
* add some minor fixes
* Added use_case argument to the kangaroo.urdf.xacro and other files
* Contributors: Sai Kishor Kothakota

0.0.23 (2022-10-03)
-------------------
* Update Changelog
* Fix the homing procedure to retry in case of failure
* wait for 1 sec instead of continously checking
* Contributors: Sai Kishor Kothakota

0.0.22 (2022-09-30 14:21)
-------------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.0.21 (2022-09-30 10:25)
-------------------------
* Update Changelog
* Increase leg length effort limits
* Increase foot inertia for MPC experiments
* 0.0.20
* Update Changelog
* 0.0.19
* Update Changelog
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.18 (2022-03-25)
-------------------
* Update changelogs
* Added frame aligned to ankle joint_5 axis
* Contributors: Narcis Miguel, enricomingo

0.0.17 (2022-03-14)
-------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.0.16 (2022-03-11 12:01)
-------------------------
* Update Changelog
* Increase firction of the foot
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.15 (2022-03-11 10:24)
-------------------------
* Update Changelog
* update the reduced collision meshes of kangaroo
* Contributors: Sai Kishor Kothakota

0.0.14 (2022-03-11 09:10)
-------------------------
* Update Changelog
* Add missing installation homing script
* Contributors: Adria Roig

0.0.13 (2022-01-26)
-------------------
* Update Changelog
* Fix wrong dt for Gazebo simulation
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
* Solved issue #1 regarding improving homing procedure. Still something
  more can be done in order to use it as a service everytime is needed.
* Tune torque control params
* Contributors: Adria Roig, enricomingo

0.0.10 (2021-11-22)
-------------------
* Update Changelog
* Added homing script (as python node) procedure
* Removed call to set configuration in gazebo.launch file
* Contributors: Adria Roig, enricomingo

0.0.9 (2021-11-18)
------------------
* Update Changelog
* Updated the crane URDF to be similar to that of the TALOS
* Updtae the collision blacklist and the default floating base position
* added the leg state transmission
* fixed base hight
* Add femur and knee joints in default configuration
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
* Update Changelog
* remove commented transmission
* Adding hip z custom transmission
* Contributors: Sai Kishor Kothakota, narcismiguel

0.0.7 (2021-09-07)
------------------
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.0.6 (2021-09-06)
------------------
* Update Changelog
* added the kangaroo_transmissions exec dependency
* Contributors: Sai Kishor Kothakota

0.0.5 (2021-09-03)
------------------
* Update Changelog
* add missing install rule of launch folder
* Contributors: Sai Kishor Kothakota

0.0.4 (2021-09-02)
------------------
* Update Changelog
* Update the transmission plugin names
* Contributors: Sai Kishor Kothakota

0.0.3 (2021-08-30 10:51)
------------------------
* Updated Changelog
* added missing urdf_test dependency
* fix the kangaroo_description tests
* added test dependency of the rostest
* enable the ankle transmission on the real robot
* Contributors: Sai Kishor Kothakota, Victor Lopez

0.0.2 (2021-08-30 09:26)
------------------------
* Add changelog
* fix the parameters of the hip
* Uncomment femur meshes for visualization
* Uncomment transmission for kangaroo pal_physics_simulator
* added extra collision blacklist links
* reduce the default floating base position
* uncomment the kangaroo_leg_length_actuator_transmission in transmission xacro
* Change negative axis of rotation
* Fix duplicated leg in transmission
* Start without controllers by default
* load the default configuration of the robot
* Remove tibia link nad mimic joint
* Add collision meshes for knee_link and femur_link
* added kangaroo minimal collision parameters
* Fix transformation of sole link
* Add missing tag for F/T sensor
* Add F/T sensor
* Update imu transformation
* Fix primatic model. Add IMU. Tune PIDS
* Change to prismatic model with mimic joints
* Inertial modifcations for torso + base link
* fix COM displaced in y axis
* Change masses and inertias for prismatic joint
* added leg length simple transmission
* Update the gazebo and position controllers launch file
* Update the upload and display launch files
* Update URDF to use the complex model (prismatic + dynamic model)
* added changes of single URDF with leg length and dynamic model
* Update the new PID gains and the initial joint positions for dynamic model
* Tune PIDs and update the leg 2 position for the new changes of Torso
* Modified the start position of joint 2 of the leg
* Added friction parameters to the leg
* Fix mistake introduced by rebase
* Fix ankle position with respect to the leg lenght
* Remove collision shape of primsatic moving part
* update effort and velocity limit for primsatic model
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
* Contributors: Adria Roig, Luca Marchionni, Pierre Fernbach, Sai Kishor Kothakota, Victor Lopez
