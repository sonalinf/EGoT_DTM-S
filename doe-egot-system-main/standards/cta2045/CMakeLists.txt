FetchContent_Declare(
  cea2045
  GIT_REPOSITORY https://github.com/epri-dev/CTA-2045-UCM-CPP-Library.git
  GIT_TAG        master
)


FetchContent_MakeAvailable(cea2045)

set(COMPONENT_NAME cta2045_ucm)

add_library(${COMPONENT_NAME} STATIC
    ucm.cpp
    device.cpp
)

# Create ALIAS targets.
add_library( ${PROJECT_NAME}::${COMPONENT_NAME} ALIAS ${COMPONENT_NAME} )

target_link_libraries(${COMPONENT_NAME} PUBLIC 
    cea2045
    pthread
)

target_include_directories(${COMPONENT_NAME} PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    ${cea2045_SOURCE_DIR}/cea2045
)