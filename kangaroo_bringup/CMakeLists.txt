cmake_minimum_required(VERSION 3.8)
project(kangaroo_bringup)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

# Install Python modules
# ament_python_install_package(${PROJECT_NAME})

ament_auto_package(INSTALL_TO_SHARE config launch)

