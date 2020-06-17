#import igraph
#import networkx as nx
#import snap
#import graph_tool as gt
# import iglsynthcpp

import random
import matplotlib.pyplot as plt

import time
import tracemalloc

import graph_nx as nx
import graph_snap as snap
import graph_igraph as igraph
import graph_gt as gt


LIBRARY = ['Networkx', 'Snap', 'igraph', 'Graph_tool']
GRAPH_TYPES =  [nx.Graph, snap.Graph, igraph.Graph, gt.Graph]
#SAMPLE = [10, 100, 1000, 10000, 100000]
SAMPLE = [10, 100, 1000, 10000, 100000, 1000000, 10000000]


def experiment1(graph, samp):
    """
    Experiment 1
    :param graph: A graph object.
    :param samp: number of nodes
    :return: graph with added nodes
    """
    for i in range(samp):
        graph.add_node(i)
    return graph


def experiment2(graph, samp):
    """
    Experiment 2
    :param graph: A graph object.
    :param samp: number of edges
    :return: graph with added edges
    """
    for i in range(samp):
        rand1 = random.randint(0,graph.number_of_nodes()-1)
        rand2 = random.randint(0,graph.number_of_nodes()-1)
        graph.add_edge(rand1,rand2)
    return graph

def experiment3(GRAPH):
    """
    Experiment 3
    :param graph: A graph object.
    :return: two 4*20*7 lists of timing and usage for 4 graph methods, 20 Node_Edge layout, and 7 N.
    """
    x = 0
    running_time_graph = []
    memory_used_graph = []
    for graph in GRAPH:
        graph = graph()
        print("======", LIBRARY[x])
        N = [0, 1, 10, 100, 1000]
        running_time_NE = []
        memory_used_NE = []

        for i in N[1:]:

            currentG = experiment1(graph, i)
            for j in N:
                currentG = experiment2(currentG, j)
                running_time_samp = []
                memory_used_samp = []
                print("Node = ", i, "Edge = ", j, ": ")
                for k in SAMPLE:
                    start = time.time()
                    tracemalloc.start()


                    rand = random.randint(0, i-1)
                    graph.in_edges(rand)

                    end = time.time()
                    current, peak = tracemalloc.get_traced_memory()
                    duration = 1e3 * (end - start)
                    space = peak * 1e-3

                    running_time_samp.append(duration)
                    memory_used_samp.append(space)
                    tracemalloc.stop()

                    print(f"Experiment: {k}: Time={duration} ms, RAM={space} Kb")

                running_time_NE.append(running_time_samp)
                memory_used_NE.append(memory_used_NE)

        x += 1

        running_time_graph.append(running_time_NE)
        memory_used_graph.append(memory_used_NE)

    return running_time_graph, memory_used_graph




def recordData(GRAPH, experimentIdx):
    """
    Helper function for Experiment 1 and 2, it record the time and usage
    :param graph: A graph object.
    :param experimentIdx: experiment 1 or 2
    :return: running_time: a 4*7 list for each graph method and N
             peak_usage: a 4*7 list for each graph method and N
             Graph: graph after experiment
    """

    running_time = []
    peak_usage = []
    Graph = []
    i = 0
    for graph in GRAPH:

        print("======", LIBRARY[i])
        runningT = []
        peakU = []

        for samp in SAMPLE:
            start = time.time()
            tracemalloc.start()

            if experimentIdx == 1:
                g = graph()
                g = experiment1(g, samp)
            elif experimentIdx == 2:
                g = experiment2(graph, samp)

            end = time.time()
            current, peak = tracemalloc.get_traced_memory()
            duration = 1e3 * (end - start)

            runningT.append(duration)
            space = peak * 1e-3
            peakU.append(space)

            tracemalloc.stop()
            print(f"Experiment: {samp}: Time={duration} ms, RAM={space} Kb")

        running_time.append(runningT)
        peak_usage.append(peakU)
        Graph.append(g)
        i += 1

    return running_time, peak_usage, Graph

def drawPlot(data, data_name, title):
    """
    Helper function to draw plots
    :param data: a 4*7 list for each graph method and N
    :param data_name: Time or Memory
    :param title: plots title
    """
    #Draw Plots
    i = 0
    for d in data:
        plt.plot(SAMPLE, d, label = LIBRARY[i])
        i+= 1
    plt.ylabel(data_name)
    plt.title(title)
    plt.legend()
    plt.savefig(title+ "_" + data_name + ".png")
    plt.close()


def transpose(list):
    """
    Helper function to transpose a list
    :param list: A list(4*20*7)
    :return: list after transpose(20*4*7)
    """
    new_list = []
    for i in range(len(list[0])):
        row = []
        for j in list:
            row.append(j[i])
        new_list.append(row)
    return new_list


def visualization(running_time, peak_usage, experiment):
    """
    visualize the results
    :param running_time: a list of timing
    :param peak_usage: a list of memory usage
    :param experiment: experiment name
    """
    if not experiment == "Experiment3" :
        drawPlot(running_time, "Time", experiment)
        drawPlot(peak_usage, "Memory", experiment)
    else:
        running_time = transpose(running_time)
        peak_usage = transpose(peak_usage)
        #print(len(running_time))
        #print(running_time)
        NE_pair = [[1,0],[1,1], [1,10], [1,100], [1,1000],
                    [10,0],[10,1], [10,10], [10,100], [10,1000],
                    [100,0],[100,1], [100,10], [100,100], [100,1000],
                    [1000,0],[1000,1], [1000,10], [1000,100], [1000,1000]]
        ne = 0
        for rt_NE in running_time:
            drawPlot(rt_NE, "Time", experiment+"_[Node, Egde]:"+str(NE_pair[ne]))
            ne+=1
        ne = 0
        for pu_NE in peak_usage:
            drawPlot(pu_NE, "Memory", experiment+"_[Node, Egde]:"+str(NE_pair[ne]))
            ne+=1



if __name__ == '__main__':

    GRAPH = GRAPH_TYPES
    print("======== Experiment 1 ========")
    running_time, peak_usage, GRAPH = recordData(GRAPH, 1)
    visualization(running_time, peak_usage, "Experiment1")


    print("======== Experiment 2 ========")
    running_time, peak_usage, GRAPH = recordData(GRAPH, 2)
    visualization(running_time, peak_usage, "Experiment2")

    print("======== Experiment 3 ========")
    running_time, peak_usage = experiment3(GRAPH_TYPES)
    visualization(running_time, peak_usage, "Experiment3")