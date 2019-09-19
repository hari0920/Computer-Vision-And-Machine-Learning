cmake_minimum_required(VERSION 3.0.0)
project(displayimage VERSION 0.1.0)

include(CTest)
enable_testing()

set(OpenCV_DIR "D:\\git\\opencv-4.1.1\\build")
find_package(OpenCV REQUIRED)
add_executable(displayimage displayimage.cpp)
include_directories(${OpenCV_Include_DIRS})
target_link_libraries(displayimage ${OpenCV_LIBS})
set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
