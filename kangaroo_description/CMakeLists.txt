cmake_minimum_required(VERSION 3.8)
project(kangaroo_description)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

ament_auto_add_executable(parameter_blackboard src/parameter_blackboard.cpp)

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

ament_auto_package(INSTALL_TO_SHARE config launch meshes mujoco robots urdf ros2_control)
