cmake_minimum_required(VERSION 3.13)
project(iglsynthcpp)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -fPIC -O3 -DNDEBUG -fopenmp -fmax-errors=1")

add_subdirectory(lib/Snap-5.0)
add_subdirectory(lib/lemon-1.3.1)
add_subdirectory(lib/pybind11)

pybind11_add_module(iglsynthcpp igl_bindings.cpp)
target_link_libraries(iglsynthcpp PUBLIC snapcore lemon)

add_executable(main main.cpp)
target_link_libraries(main PUBLIC snapcore lemon)