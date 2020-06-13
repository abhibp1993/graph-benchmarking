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
SAMPLE = [10, 100, 1000, 10000]
#SAMPLE = [10, 100, 1000, 10000, 100000, 1000000, 10000000]


def experiment1(Graph, samp):
    g = Graph()

    for i in range(samp):
        g.add_node(i)


def experiment2(Graph, samp):
    g = Graph()
    for i in range(samp):
        #print(i)
        rand1 = random.randint(0,5000)
        rand2 = random.randint(0,5000)
        g.add_edge(rand1,rand2)


def recordData(experimentIdx):
    running_time = []
    peak_usage = []
    for graph in GRAPH_TYPES:

        print("======", graph)
        runningT = []
        peakU = []

        for samp in SAMPLE:
            start = time.time()
            tracemalloc.start()

            if experimentIdx == 1:
                experiment1(graph, samp)
            elif experimentIdx == 2:
                experiment2(graph, samp)

            end = time.time()
            current, peak = tracemalloc.get_traced_memory()
            duration = 1e3 * (end - start)

            runningT.append(duration)
            space = peak * 1e-3
            peakU.append(space)

            tracemalloc.stop()
            print(f"Experiment: Add({samp}):: Time={duration} ms, RAM={space} Kb")

        running_time.append(runningT)
        peak_usage.append(peakU)

    return running_time, peak_usage

def visualization(running_time, peak_usage, experiment):
    #Draw Plots
    i = 0
    for runTime in running_time:
        plt.plot(SAMPLE, runTime, label = LIBRARY[i])
        i+= 1
    plt.ylabel('Time')
    plt.title(experiment)
    plt.legend()
    plt.savefig(experiment+ "_time.png")
    plt.close()

    i = 0
    for peak in peak_usage:
        plt.plot(SAMPLE, peak, label = LIBRARY[i])
        i+= 1
    plt.ylabel('Peak Memory Usage')
    plt.title(experiment)
    plt.legend()
    plt.savefig(experiment + "_peak_usage.png")
    plt.close()



if __name__ == '__main__':


    print("======== Experiment 1 ========")
    running_time, peak_usage = recordData(1)
    visualization(running_time, peak_usage, "Experiment1")


    print("======== Experiment 2 ========")
    running_time, peak_usage = recordData(2)
    visualization(running_time, peak_usage, "Experiment2")