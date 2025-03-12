set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR aarch64)  # Change to match your target architecture
set(CROSS_COMPILER_PATH /home/user/cross_compilers/aarch64--glibc--stable-2022.08-1)
# Set cross-compiler paths
set(CMAKE_C_COMPILER ${CROSS_COMPILER_PATH}/bin/${CMAKE_SYSTEM_PROCESSOR}-buildroot-linux-gnu-gcc)
set(CMAKE_CXX_COMPILER ${CROSS_COMPILER_PATH}/bin/${CMAKE_SYSTEM_PROCESSOR}-buildroot-linux-gnu-g++)
set(XXX /home/user/rootfs/ubuntuRootFS)  # Set to your root filesystem
#CMAKE_SYSROOT #TODO - why only when i remove CMAKE_SYSROOT its work
# Set where CMake should look for libraries and headers
set(CMAKE_LIBRARY_PATH ${XXX}/usr/lib/aarch64-linux-gnu/)

set(CMAKE_FIND_ROOT_PATH ${XXX} ${XXX}/usr ${XXX}/usr/local)

# Only search inside the target rootfs
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)

# ROS 2 paths
set(AMENT_PREFIX_PATH ${XXX}/opt/ros/humble)
set(CMAKE_PREFIX_PATH ${AMENT_PREFIX_PATH})