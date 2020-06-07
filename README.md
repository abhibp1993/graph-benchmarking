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


# Instructions to Setup Code

## Build Environment 
It is recommended to use docker for this project. The Dockerfile can be built using 
```
$ cd <path>/graph-benchmarking/docker
$ docker build -t graph-benchmarking .
```

Check if everything went alright:
```
$ docker run -v D:\MyWorld\GitHub-Projects\graph-benchmarking:/home/graph-benchmarking --name graph-benchmarking --rm graph-benchmarking:latest 
```

This will open the shell within docker. Run the following commands to generate the bindings. 
```
$ cd /home/graph-benchmarking/
$ python3 setup.py develop
```

The `setup.py` will invoke the cmake to compile and link the C++ code and generate bindings. 
To use it, run the following command. 

```
$ python3
>>> import iglsynthcpp as igl
>>> igl.hello()
# should print "0"
>>> g1 = igl.SnapGraph()
>>> g2 = igl.LemonGraph()
```

## Writing Code
Here are some tips for code organization. 

* All C++ code (`.h, .cpp`) goes into `src` folder. 
* All Python code goes into `benchmark` folder. 

The `benchmark` folder contains a `main.py` file that runs all the benchmarks. 


## Python Binding 
Python binding is done using `pybind11`. 
In C++, `igl_bindings.cpp` defines what needs to be bound to python.
The `main.cpp` will be used to generate C++ executable, which may be executed using `./main` from `build` folder.

Note: Just uncomment the code in `igl_bindings.cpp` to bind a particular function to python. 


# TODOs

1. Create an abstract `GraphBase` class that will serve as parent class for all graph class.
    `GraphBase` defines `AddNode, AddEdge, GetInEdges, GetOutEdges` functions. 

2. Create algorithms file that contains `Bfs(GraphBase)` and `Dfs(GraphBase)` functions. 

3. Create products file that contains `Tensor(GraphBase, GraphBase)`, `Cartesian(GraphBase, GraphBase)`, ... 

4. Bind all functionality to python.

5. Create a `main.py` file that generates benchmarking results. 

6. Generate graphical outputs (comparison plots, tables). 

7. Make a recommendation on which library to use in backend, and why?


# Contributors: 
1. Abhishek N. Kulkarni (ankulkarni@wpi.edu)
2. Yaru Gong (ygong5@wpi.edu)
