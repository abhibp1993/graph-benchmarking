import igraph
import networkx as nx
import snap
import graph_tool as gt
# import iglsynthcpp


import time
import tracemalloc


GRAPH_TYPES =  [nx.DiGraph, snap.TUNGraph.New, igraph.Graph, gt.Graph]

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

    tracemalloc.start()
    print("======== Experiment 1 ========")
    for idx in range(len(GRAPH_TYPES)):
        start = time.time()
        snapshot1 = tracemalloc.take_snapshot()
        experiment1(idx)
        end = time.time()
        snapshot2 = tracemalloc.take_snapshot()
        stats = snapshot1.compare_to(snapshot2, 'lineno')
        tracemalloc.start()
        print(GRAPH_TYPES[idx])
        print("Spent", end-start, " second.")
        #print("Memory used: ", stats)
