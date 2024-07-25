^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package kangaroo_bringup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.12 (2022-01-10)
-------------------

0.0.20 (2022-05-04)
-------------------

0.0.19 (2022-05-04)
-------------------
* Merge branch 'fix_package_information' into 'master'
  Fix package information
  See merge request robots/kangaroo_robot!27
* added more package dependencies to the packages
* Adapt motion home to real robot limits
* Contributors: Adria Roig, Sai Kishor Kothakota, saikishor

0.1.7 (2024-07-11)
------------------

Forthcoming
-----------

0.1.9 (2024-07-16)
------------------

0.1.8 (2024-07-12)
------------------
* 0.1.7
* Update Changelog
* Contributors: Sai Kishor Kothakota

0.1.6 (2024-07-11)
------------------

0.1.5 (2024-07-09)
------------------

0.1.4 (2024-07-09)
------------------
* Merge branch 'kangaroo_3' into 'master'
  Update configuration files from latest value tested on Kangaroo 3
  See merge request robots/kangaroo_robot!52
* Add fake_walking and fake_walking2 play_motion motions
* Merge branch 'kangaroo_3_changes' into 'master'
  Kangaroo 3 changes
  See merge request robots/kangaroo_robot!50
* Open ref_velocity port and change IMU Hw transformation
* Fix the enu transformation of the imu
* Merge branch 'fix_play_motion_ranges' into 'master'
  fix play_motion range for leg_exploration
  See merge request robots/kangaroo_robot!49
* fix play_motion range for leg_exploration
* Contributors: Adria Roig, Sai Kishor Kothakota

0.1.3 (2024-04-30)
------------------

0.1.2 (2024-04-19)
------------------

0.1.1 (2024-04-18)
------------------
* Merge branch 'fix/urdf/02024/foot' into 'master'
  Fix/urdf/02024/foot
  See merge request robots/kangaroo_robot!42
* add version argument to all launch files using upload.launch
* Contributors: Adria Roig, Sai Kishor Kothakota

0.1.0 (2024-04-04)
------------------

0.0.30 (2024-01-10)
-------------------

0.0.29 (2023-11-08)
-------------------

0.0.28 (2023-07-04)
-------------------

0.0.27 (2023-02-07)
-------------------
* Merge branch 'kangaroo_deployed_changes' into 'master'
  Kangaroo deployed changes
  See merge request robots/kangaroo_robot!36
* added the proper configuration of the bota FTs
* add new bringup controllers and use common hardware file based on ft_sensors argument
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.26 (2023-01-17)
-------------------
* Merge branch 'ft_robot' into 'master'
  Argument to launch robot with F/T sensors or not
  See merge request robots/kangaroo_robot!35
* Remove fixed from sole & ft_sensor joints
* Fix ft sensor transformations
* Update homing and launch force_torque_sensor_controller when ft_sensors is true
* Contributors: Adria Roig, Adrià Roig, saikishor

0.0.25 (2023-01-12)
-------------------
* Merge branch 'add_joy_teleop' into 'master'
  added joy_teleop and twist_mux files to kangaroo_bringup
  See merge request robots/kangaroo_robot!33
* added joy_teleop and twist_mux files to kangaroo_bringup
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.24 (2022-12-22)
-------------------
* Merge branch 'add_use_cage_argument' into 'master'
  Added use_case argument to the kangaroo.urdf.xacro and other files
  See merge request robots/kangaroo_robot!34
* Added use_case argument to the kangaroo.urdf.xacro and other files
* Contributors: Sai Kishor Kothakota, saikishor

0.0.23 (2022-10-03)
-------------------

0.0.22 (2022-09-30)
-------------------

0.0.21 (2022-09-30)
-------------------
* Merge branch 'kangaroo_mpc' into 'master'
  Kangaroo mpc
  See merge request robots/kangaroo_robot!31
* Add F/T sensors in Gazebo for simplicity in the experiments
* 0.0.20
* Update Changelog
* 0.0.19
* Update Changelog
* added more package dependencies to the packages
* Adapt motion home to real robot limits
* Contributors: Adria Roig, Sai Kishor Kothakota, saikishor

0.0.18 (2022-03-25)
-------------------

0.0.17 (2022-03-14)
-------------------

0.0.16 (2022-03-11)
-------------------

0.0.15 (2022-03-11)
-------------------

0.0.14 (2022-03-11)
-------------------

0.0.13 (2022-01-26)
-------------------
* Merge branch 'master' of gitlab:robots/kangaroo_robot
* 0.0.12
* Update Changelog
* Contributors: Adria Roig

0.0.11 (2021-12-28)
-------------------
* Merge branch 'master' of gitlab:robots/kangaroo_robot
* Fix IMU wrong orientation
* Solved issue #1 regarding improving homing procedure. Still something
  more can be done in order to use it as a service everytime is needed.
* Contributors: Adria Roig, enricomingo

0.0.10 (2021-11-22)
-------------------
* Merge branch 'homing_procedure' into 'master'
  Homing procedure
  See merge request robots/kangaroo_robot!23
* Mv homing motion to kangaroo motions
* Added files for play_motion homing
* Contributors: Adria Roig, enricomingo

0.0.9 (2021-11-18)
------------------
* Merge branch 'play_motion_setup' into 'master'
  Play motion setup
  See merge request robots/kangaroo_robot!19
* added kangaroo initial motions
* added the both legs configuration
* added play_motion setup without motions
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.8 (2021-09-10)
------------------

0.0.7 (2021-09-07)
------------------

0.0.6 (2021-09-06)
------------------

0.0.5 (2021-09-03)
------------------

0.0.4 (2021-09-02)
------------------
* Merge branch 'imu_and_other_configuration' into 'master'
  Imu and other configuration
  See merge request robots/kangaroo_robot!13
* remove the force torque sensors information
* add the IMU hardware configuration
* Contributors: Jordan Palacios, Sai Kishor Kothakota

0.0.3 (2021-08-30)
------------------

0.0.2 (2021-08-30)
------------------
* Fix package version
* Merge branch 'kangaroo_wbc' into 'master'
  Kangaroo wbc
  See merge request robots/kangaroo_robot!11
* Adding new pids and ff term ports
* Add F/T sensor
* Fix primatic model. Add IMU. Tune PIDS
* First commit
* Contributors: Adria Roig, Jordan Palacios, Luca Marchionni, Victor Lopez, victor
