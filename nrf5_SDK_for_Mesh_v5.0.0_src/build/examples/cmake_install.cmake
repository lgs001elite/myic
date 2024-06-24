# Install script for directory: C:/Users/glu250/Downloads/myic/nrf5_SDK_for_Mesh_v5.0.0_src/examples

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/Program Files (x86)/MBTLE")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "RelWithDebInfo")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "TRUE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "C:/Program Files (x86)/Arm GNU Toolchain arm-none-eabi/13.2 Rel1/bin/arm-none-eabi-objdump.exe")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("C:/Users/glu250/Downloads/myic/nrf5_SDK_for_Mesh_v5.0.0_src/build/examples/common/cmake_install.cmake")
  include("C:/Users/glu250/Downloads/myic/nrf5_SDK_for_Mesh_v5.0.0_src/build/examples/beaconing/cmake_install.cmake")
  include("C:/Users/glu250/Downloads/myic/nrf5_SDK_for_Mesh_v5.0.0_src/build/examples/coordinator/cmake_install.cmake")
  include("C:/Users/glu250/Downloads/myic/nrf5_SDK_for_Mesh_v5.0.0_src/build/examples/pb_remote/cmake_install.cmake")
  include("C:/Users/glu250/Downloads/myic/nrf5_SDK_for_Mesh_v5.0.0_src/build/examples/provisioner/cmake_install.cmake")
  include("C:/Users/glu250/Downloads/myic/nrf5_SDK_for_Mesh_v5.0.0_src/build/examples/sensor/cmake_install.cmake")
  include("C:/Users/glu250/Downloads/myic/nrf5_SDK_for_Mesh_v5.0.0_src/build/examples/scene/cmake_install.cmake")
  include("C:/Users/glu250/Downloads/myic/nrf5_SDK_for_Mesh_v5.0.0_src/build/examples/light_lightness/cmake_install.cmake")
  include("C:/Users/glu250/Downloads/myic/nrf5_SDK_for_Mesh_v5.0.0_src/build/examples/light_lc/cmake_install.cmake")
  include("C:/Users/glu250/Downloads/myic/nrf5_SDK_for_Mesh_v5.0.0_src/build/examples/light_ctl/cmake_install.cmake")
  include("C:/Users/glu250/Downloads/myic/nrf5_SDK_for_Mesh_v5.0.0_src/build/examples/enocean_switch/cmake_install.cmake")
  include("C:/Users/glu250/Downloads/myic/nrf5_SDK_for_Mesh_v5.0.0_src/build/examples/dimming/cmake_install.cmake")
  include("C:/Users/glu250/Downloads/myic/nrf5_SDK_for_Mesh_v5.0.0_src/build/examples/lpn/cmake_install.cmake")
  include("C:/Users/glu250/Downloads/myic/nrf5_SDK_for_Mesh_v5.0.0_src/build/examples/dfu/cmake_install.cmake")
  include("C:/Users/glu250/Downloads/myic/nrf5_SDK_for_Mesh_v5.0.0_src/build/examples/serial/cmake_install.cmake")
  include("C:/Users/glu250/Downloads/myic/nrf5_SDK_for_Mesh_v5.0.0_src/build/examples/light_switch/cmake_install.cmake")

endif()

