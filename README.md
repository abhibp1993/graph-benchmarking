# Benchmarking of Graph Tools in C++ and Python.

In IGLSynth, we typically deal with large networks (~10^6+ nodes and ~10^7+ edges). 
Thus, we want an efficient graph data representation in IGLSynth. 

In this project, we evaluate benchmarks to compare the following graph libraries. 

* `iglsynth v0.2.3` (Python): Preliminary implementation of graph.
* `iglsynthcpp` (C++): Custom wrapper around Stanford's graph library (Snap) and LEMON graph library.
* `snap` (Python): Stanford's graph library (python-bindings).
* `networkx` (Python): Most popular graph library in Python.
* `graph_tool` (Python): Efficient graph library written in C++ and exposed in Python using Boost.Python.
* `igraph` (Python): Efficient graph library written in C and exposed in Python using SWIG.


## Experiment 1: Creation of Nodes
Generate a graph of time and space required to generate 0, 10, 100, 1000, ..., 10^7 nodes.

## Experiment 2: Creation of Edges 
Generate a graph of time and space required to generate 0, 10, 100, 1000, ..., 10^7 edges.
(Use random function to generate nodes and edges.)

## Experiment 3: Neighborhood accession
Given the above graphs, compare the time and space required to run 0, 10, 100, ..., 10^7 neighborhood queries. 

## Experiment 4: BFS, DFS traversal
Compare time and space required for BFS and DFS traversal for randomly generated graphs of size 0, 10, 100, ..., 10^7.

## Experiment 5: Products of Two Graphs
Compare time and space required for performing following product operations on two randomly generated graphs 
of size 0, 10, 100, ..., 10^5.

    - Tensor product
    - Cartesian product 
    - Lexicographic product
    - Normal product
    - Disjunctive product


#  TODOs

1. Create an abstract `GraphBase` class that will serve as parent class for all graph class.
    `GraphBase` defines `AddNode, AddEdge, GetInEdges, GetOutEdges` functions. 

2. Create algorithms file that contains `Bfs(GraphBase)` and `Dfs(GraphBase)` functions. 

3. Create products file that contains `Tensor(GraphBase, GraphBase)`, `Cartesian(GraphBase, GraphBase)`, ... 

4. Bind all functionality to python.

5. Create a `benchmarks.py` file that generates benchmarking results. 

6. Generate graphical outputs (comparison plots, tables). 

7. Make a recommendation on which library to use in backend, and why?


# Contributors: 
1. Abhishek N. Kulkarni (ankulkarni@wpi.edu)
2. Yaru Gong (email?)
