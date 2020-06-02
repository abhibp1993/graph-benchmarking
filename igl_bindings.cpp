#include "src/graph_snap.h"
#include "src/graph_lemon.h"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>


namespace py = pybind11;

PYBIND11_MODULE(iglcpp, m) {

    m.def("hello", [](){return 0;});

}