cmake_minimum_required(VERSION 2.8.3)
project(kangaroo_mj_description)

find_package(catkin REQUIRED)

catkin_package()

foreach(dir xml meshes)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

install(PROGRAMS bin/simulation
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)