set(target "beaconing_${PLATFORM}_${SOFTDEVICE}")

add_executable(${target}
    "${CMAKE_CURRENT_SOURCE_DIR}/src/main.c"
    "${CMAKE_CURRENT_SOURCE_DIR}/src/spis.c"
    "${CMAKE_CURRENT_SOURCE_DIR}/src/m2s.c"
    "${CMAKE_CURRENT_SOURCE_DIR}/src/s2m.c"
    "${CMAKE_CURRENT_SOURCE_DIR}/src/spis_data.c"
    "${CMAKE_SOURCE_DIR}/mesh/stack/src/mesh_stack.c"
    "${CMAKE_SOURCE_DIR}/examples/common/src/mesh_provisionee.c"
    "${CMAKE_SOURCE_DIR}/examples/common/src/simple_hal.c"
    "${SDK_ROOT}/modules/nrfx/drivers/src/nrfx_gpiote.c"
    "${CMAKE_SOURCE_DIR}/examples/common/src/mesh_app_utils.c"
    # Added by Gaosheng, for checksum
    #"${SDK_ROOT}/components/libraries/crypto/nrf_crypto_init.c"
    #"${SDK_ROOT}/components/libraries/crypto/nrf_crypto_hash.c"
    #"${CMAKE_CURRENT_SOURCE_DIR}/src/hash.c"
    "${SDK_ROOT}/components/boards/boards.c"
    "${SDK_ROOT}/integration/nrfx/legacy/nrf_drv_spis.c"
    #"${SDK_ROOT}/components/libraries/crypto/backend/oberon/oberon_backend_hash.c"
    "${SDK_ROOT}/modules/nrfx/drivers/src/nrfx_spis.c"
    #
    ${BLE_SOFTDEVICE_SUPPORT_SOURCE_FILES}
    ${ACCESS_SOURCE_FILES}
    ${WEAK_SOURCE_FILES}
    ${CONFIG_SERVER_SOURCE_FILES}
    ${HEALTH_SERVER_SOURCE_FILES}
    ${PROV_PROVISIONEE_SOURCE_FILES}
    ${PROV_COMMON_SOURCE_FILES}
    ${PROV_BEARER_ADV_SOURCE_FILES}
    ${MESH_CORE_SOURCE_FILES}
    ${MESH_BEARER_SOURCE_FILES}
    ${MESH_APP_TIMER_SOURCE_FILES}
    ${${PLATFORM}_SOURCE_FILES}
    ${${nRF5_SDK_VERSION}_SOURCE_FILES})

target_include_directories(${target} PUBLIC
    "${CMAKE_CURRENT_SOURCE_DIR}/include"
    "${CMAKE_CURRENT_SOURCE_DIR}/../include"
    "${CMAKE_SOURCE_DIR}/examples/common/include"
    # Added by me
    "${SDK_ROOT}/components/libraries/delay"
    "${SDK_ROOT}/components/libraries/timer"
    "${SDK_ROOT}/components/boards"
    #"${SDK_ROOT}/components/libraries/crypto"
    #"${SDK_ROOT}/components/libraries/crypto/backend/cc310"
    #"${SDK_ROOT}/components/libraries/crypto/backend/oberon"
    #/home/gaosheng/mesh/my_mesh/nRF5_SDK_17.0.2_d674dde/modules/nrfx/drivers/src/nrfx_spis.c
    "${SDK_ROOT}/modules/nrfx/drivers/include"
    "${SDK_ROOT}/modules/nrfx/drivers"
    "${SDK_ROOT}/components/boards"
    "${SDK_ROOT}/integration/nrfx/legacy"
    "${SDK_ROOT}/integration/nrfx"
    "${SDK_ROOT}/modules/nrfx/hal"
    "${SDK_ROOT}/modules/nrfx"
    "${SDK_ROOT}/modules/nrfx/templates/nRF9160"
    "${SDK_ROOT}/modules/nrfx/templates/nRF52840"
    #
    ${BLE_SOFTDEVICE_SUPPORT_INCLUDE_DIRS}
    ${CONFIG_SERVER_INCLUDE_DIRS}
    ${HEALTH_SERVER_INCLUDE_DIRS}
    ${MESH_INCLUDE_DIRS}
    ${${SOFTDEVICE}_INCLUDE_DIRS}
    ${${PLATFORM}_INCLUDE_DIRS}
    ${${BOARD}_INCLUDE_DIRS}
    ${${nRF5_SDK_VERSION}_INCLUDE_DIRS})

set_target_link_options(${target}
    ${CMAKE_CURRENT_SOURCE_DIR}/linker/${PLATFORM}_${SOFTDEVICE})

target_compile_options(${target} PUBLIC
    ${${ARCH}_DEFINES})

target_compile_definitions(${target} PUBLIC
    ${USER_DEFINITIONS}
    -DUSE_APP_CONFIG
    ${${PLATFORM}_DEFINES}
    ${${SOFTDEVICE}_DEFINES}
    ${${BOARD}_DEFINES})

target_link_libraries(${target}
    rtt_${PLATFORM}
    uECC_${PLATFORM})

create_hex(${target})
add_flash_target(${target})

get_property(target_include_dirs TARGET ${target} PROPERTY INCLUDE_DIRECTORIES)
add_pc_lint(${target}
    "${CMAKE_CURRENT_SOURCE_DIR}/src/main.c"
    "${target_include_dirs}"
    "${${PLATFORM}_DEFINES};${${SOFTDEVICE}_DEFINES};${${BOARD}_DEFINES}")
add_ses_project(${target})
