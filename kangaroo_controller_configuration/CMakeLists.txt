cmake_minimum_required(VERSION 3.8)
project(kangaroo_controller_configuration)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

ament_auto_package(INSTALL_TO_SHARE config launch)
