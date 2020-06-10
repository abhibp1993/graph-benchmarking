# import igraph
# import networkx as nx
# import snap
# import graph_tool as gt
# # import iglsynthcpp

import graph_nx as nx

from random import randint
import time
import tracemalloc

# GRAPH_TYPES =  [nx.DiGraph, snap.TUNGraph.New, igraph.Graph, gt.Graph]


def experiment_add_nodes(Graph, n):
    """
    The function

    :param grf: A graph object.
    :param n: number of nodes
    :return: time (in ms), space (in Kb)
    """
    grf = Graph()

    tracemalloc.start()
    time_start = time.time()

    for i in range(0, int(n)):
        grf.add_node(n)

    time_end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return 1e3 * (time_end - time_start), peak * 1e-3


def experiment1(idx):
    g = GRAPH_TYPES[idx]()

    if idx == 0:
        for i in range(10000000):
            g.add_node(i)
    elif idx == 1:
        for i in range(10000000):
            g.AddNode(i)
    elif idx == 2:
        for i in range(10000000):
            g.add_vertices(i)
    else:
        for i in range(10000000):
            g.add_vertex(i)


def experiment2():
    pass


if __name__ == '__main__':

    # Define types of graphs, size of nodes
    GRAPH = [nx.Graph]
    N = [0, 1, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]

    # The following loop can be modified as follows.
    #   This results in a cleaner structure with a good level of abstraction,
    #   where experiment_add_nodes encapsulates the actual measurement of time and RAM.
    print("======== Experiment 1 ========")

    # for idx in range(len(GRAPH_TYPES)):
    for graph in GRAPH:
        for num_nodes in N:
            duration, space = experiment_add_nodes(graph, num_nodes)
            print(f"Experiment: Add Nodes({num_nodes}):: Time={duration} ms, RAM={space} Kb")

    #     start = time.time()
    #     tracemalloc.start()
    #     experiment1(idx)
    #     end = time.time()
    #     current, peak = tracemalloc.get_traced_memory()
    #
    #     print(GRAPH_TYPES[idx])
    #     print("Spent", end-start, " second.")
    #     print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    #     tracemalloc.stop()
