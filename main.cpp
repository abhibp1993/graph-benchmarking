#include <iostream>
#include <Snap.h>
#include <lemon/list_graph.h>
#include <pybind11/pybind11.h>


using namespace lemon;
using namespace std;
int main()
{
    ListDigraph g;
    ListDigraph::Node u = g.addNode();
    ListDigraph::Node v = g.addNode();
    ListDigraph::Arc  a = g.addArc(u, v);
    cout << "Hello World! This is LEMON library here." << endl;
    cout << "We have a directed graph with " << countNodes(g) << " nodes "
         << "and " << countArcs(g) << " arc." << endl;
    return 0;
}


int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring
    m.def("add", &add, "A function which adds two numbers");
}