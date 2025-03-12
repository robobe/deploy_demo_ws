cmake_minimum_required(VERSION 3.8)
project(pkg_interface)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

set(MESSAGES
  "msg/Demo.msg"
)

set(SERVICES 
  "srv/Demo.srv"
)


rosidl_generate_interfaces(${PROJECT_NAME}
  ${MESSAGES}
  ${SERVICES} 
)


ament_export_dependencies(rosidl_default_runtime)

ament_package()
