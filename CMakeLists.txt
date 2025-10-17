cmake_minimum_required(VERSION 3.8)
project(ros_uv_sample)

find_package(ament_cmake_auto REQUIRED)

add_custom_target(${PROJECT_NAME}_venv ALL
  COMMAND UV_PROJECT_ENVIRONMENT=${CMAKE_INSTALL_PREFIX}/share/${PROJECT_NAME}/.venv uv sync
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

ament_python_install_package(${PROJECT_NAME} PACKAGE_DIR src/${PROJECT_NAME})

install(PROGRAMS scripts/minimal_publisher DESTINATION lib/${PROJECT_NAME})

ament_auto_package()
