# Find spot, a platform for LTL and ω-automata manipulation
# See https://spot.lrde.epita.fr

# This file is included in ltlsynth from OMPL project <https://github.com/ompl/ompl>.

INCLUDE(FindPackageHandleStandardArgs)

FIND_PACKAGE(PkgConfig)
if(PKGCONFIG_FOUND)
    pkg_search_modules(SNAP libsnap)
    set(SNAP_INCLUDE_DIRS "/lib/Snap-5.0/snap-core;/lib/Snap-5.0/glib-core")
    # if(SNAP_LIBRARIES AND NOT SNAP_INCLUDE_DIRS)
    #     set(SPOT_INCLUDE_DIRS "/home/abhibp1993-ubuntu/MyWorld/1-\ CodeBase/2-FunProjects/iglsynth-cpp/lib/snap/snap-core")
    # endif()
endif()
find_package_handle_standard_args(SNAP DEFAULT_MSG SNAP_LIBRARIES SNAP_INCLUDE_DIRS)