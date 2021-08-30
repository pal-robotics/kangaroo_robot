^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package kangaroo_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
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
