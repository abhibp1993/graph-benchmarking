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


    print("======== Experiment 1 ========")
    for idx in range(len(GRAPH_TYPES)):
        start = time.time()
        tracemalloc.start()
        experiment1(idx)
        end = time.time()
        current, peak = tracemalloc.get_traced_memory()

        print(GRAPH_TYPES[idx])
        print("Spent", end-start, " second.")
        print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
        tracemalloc.stop()
