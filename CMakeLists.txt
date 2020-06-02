cmake_minimum_required(VERSION 3.13)
project(cmake_example)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -fPIC -O3 -DNDEBUG -fopenmp -fmax-errors=1")

add_subdirectory(lib/Snap-5.0)
add_subdirectory(lib/lemon-1.3.1)
add_subdirectory(lib/pybind11)

pybind11_add_module(cmake_example main.cpp)
target_link_libraries(cmake_example PUBLIC snapcore lemon)