#include "src/graph_base.h"
#include "src/graph_snap.h"
#include "src/graph_lemon.h"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>


namespace py = pybind11;

PYBIND11_MODULE(iglsynthcpp, m) {

    m.def("hello", [](){return 0;});


    py::class_<GraphBase>(m, "GraphBase")
        .def(py::init<>())
        ;

    py::class_<Node>(m, "Node")
        .def(py::init<int, std::string&>())
        ;

    py::class_<Edge>(m, "Edge")
        .def(py::init<int, std::shared_ptr<Node>&, std::shared_ptr<Node>&>())
        ;

    py::class_<SnapGraph, GraphBase>(m, "SnapGraph")
        .def(py::init<>())
        .def("AddNode", &SnapGraph::AddNode)
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