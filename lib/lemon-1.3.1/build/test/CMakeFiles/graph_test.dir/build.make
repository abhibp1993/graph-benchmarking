# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.13

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/thirdparty/lemon-1.3.1

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/thirdparty/lemon-1.3.1/build

# Include any dependencies generated for this target.
include test/CMakeFiles/graph_test.dir/depend.make

# Include the progress variables for this target.
include test/CMakeFiles/graph_test.dir/progress.make

# Include the compile flags for this target's objects.
include test/CMakeFiles/graph_test.dir/flags.make

test/CMakeFiles/graph_test.dir/graph_test.cc.o: test/CMakeFiles/graph_test.dir/flags.make
test/CMakeFiles/graph_test.dir/graph_test.cc.o: ../test/graph_test.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/thirdparty/lemon-1.3.1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object test/CMakeFiles/graph_test.dir/graph_test.cc.o"
	cd /home/thirdparty/lemon-1.3.1/build/test && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/graph_test.dir/graph_test.cc.o -c /home/thirdparty/lemon-1.3.1/test/graph_test.cc

test/CMakeFiles/graph_test.dir/graph_test.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/graph_test.dir/graph_test.cc.i"
	cd /home/thirdparty/lemon-1.3.1/build/test && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/thirdparty/lemon-1.3.1/test/graph_test.cc > CMakeFiles/graph_test.dir/graph_test.cc.i

test/CMakeFiles/graph_test.dir/graph_test.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/graph_test.dir/graph_test.cc.s"
	cd /home/thirdparty/lemon-1.3.1/build/test && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/thirdparty/lemon-1.3.1/test/graph_test.cc -o CMakeFiles/graph_test.dir/graph_test.cc.s

# Object files for target graph_test
graph_test_OBJECTS = \
"CMakeFiles/graph_test.dir/graph_test.cc.o"

# External object files for target graph_test
graph_test_EXTERNAL_OBJECTS =

test/graph_test: test/CMakeFiles/graph_test.dir/graph_test.cc.o
test/graph_test: test/CMakeFiles/graph_test.dir/build.make
test/graph_test: lemon/libemon.a
test/graph_test: test/CMakeFiles/graph_test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/thirdparty/lemon-1.3.1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable graph_test"
	cd /home/thirdparty/lemon-1.3.1/build/test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/graph_test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
test/CMakeFiles/graph_test.dir/build: test/graph_test

.PHONY : test/CMakeFiles/graph_test.dir/build

test/CMakeFiles/graph_test.dir/clean:
	cd /home/thirdparty/lemon-1.3.1/build/test && $(CMAKE_COMMAND) -P CMakeFiles/graph_test.dir/cmake_clean.cmake
.PHONY : test/CMakeFiles/graph_test.dir/clean

test/CMakeFiles/graph_test.dir/depend:
	cd /home/thirdparty/lemon-1.3.1/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/thirdparty/lemon-1.3.1 /home/thirdparty/lemon-1.3.1/test /home/thirdparty/lemon-1.3.1/build /home/thirdparty/lemon-1.3.1/build/test /home/thirdparty/lemon-1.3.1/build/test/CMakeFiles/graph_test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : test/CMakeFiles/graph_test.dir/depend

