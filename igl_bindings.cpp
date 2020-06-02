#include "src/graph_snap.h"
#include "src/graph_lemon.h"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>


namespace py = pybind11;

PYBIND11_MODULE(iglsynthcpp, m) {

    m.def("hello", [](){return 0;});
    
    py::class_<SnapGraph>(m, "SnapGraph")
        .def(py::init<>())
        // .def("AddNode", &SnapGraph::AddNode)
        // .def("AddEdge", &SnapGraph::AddEdge)
        // .def("GetInEdges", &SnapGraph::GetInEdges)
        ;

    py::class_<LemonGraph>(m, "LemonGraph")
        .def(py::init<>())
        // .def("AddNode", &LemonGraph::AddNode)
        // .def("AddEdge", &LemonGraph::AddEdge)
        // .def("GetInEdges", &LemonGraph::GetInEdges)
        ;
}