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
    for i in range(samp):
        graph.add_node(i)
    return graph


def experiment2(graph, samp):
    for i in range(samp):
        rand1 = random.randint(0,graph.number_of_nodes()-1)
        rand2 = random.randint(0,graph.number_of_nodes()-1)
        graph.add_edge(rand1,rand2)
    return graph

def experiment3(GRAPH):
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


def visualization(running_time, peak_usage, experiment):
    if not experiment == "Experiment3" :
        drawPlot(running_time, "Time", experiment)
        drawPlot(peak_usage, "Memory", experiment)
    else:
        print(running_time, peak_usage, experiment)
        #i = 0
        #for graph_time in running_time:
        #    plt.plot(SAMPLE, graph_time[i], label= LIBRARY[i])
    #Draw Plots
    #i = 0
    #for runTime in running_time:
    #    plt.plot(SAMPLE, runTime, label = LIBRARY[i])
    #    i+= 1
    #plt.ylabel('Time')
    #plt.title(experiment)
    #plt.legend()
    #plt.savefig(experiment+ "_time.png")
    #plt.close()

    #i = 0
    #for peak in peak_usage:
    #    plt.plot(SAMPLE, peak, label = LIBRARY[i])
    #    i+= 1
    #plt.ylabel('Peak Memory Usage')
    #plt.title(experiment)
    #plt.legend()
    #plt.savefig(experiment + "_peak_usage.png")
    #plt.close()



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