import igraph
import networkx as nx
import snap
import graph_tool as gt
# import iglsynthcpp

import random
import matplotlib.pyplot as plt

import time
import tracemalloc

LIBRARY = ['Networkx', 'Snap', 'igraph', 'Graph_tool']
GRAPH_TYPES =  [nx.DiGraph, snap.TUNGraph.New, igraph.Graph, gt.Graph]
#SAMPLE = [10, 100, 1000]
SAMPLE = [10, 100, 1000, 10000, 100000, 1000000, 10000000]


def experiment1(idx, samp):
    g = GRAPH_TYPES[idx]()

    if idx == 0:
        for i in range(samp):
            g.add_node(i)
    elif idx == 1:
        for i in range(samp):
            g.AddNode(i)
    elif idx == 2:
        for i in range(samp):
            g.add_vertices(i)
    else:
        for i in range(samp):
            g.add_vertex(i)





def experiment2(idx, samp):
    g = GRAPH_TYPES[idx]()

    if idx == 0:
        for i in range(samp):
            rand1 = random.randint(0,5000)
            rand2 = random.randint(0,5000)
            g.add_edge(rand1,rand2)
    elif idx == 1:
        for i in range(samp):
            rand1 = random.randint(0,5000)
            rand2 = random.randint(0,5000)
            if not g.IsNode(rand1):
                g.AddNode(rand1)
            if not g.IsNode(rand2):
                g.AddNode(rand2)
            g.AddEdge(rand1,rand2)
    elif idx == 2:
        for i in range(samp):
            rand1 = random.randint(0,5000)
            rand2 = random.randint(0,5000)
            g.add_vertices(rand1)
            g.add_vertices(rand2)
            g.add_edges([(rand1,rand2)])
    else:
        for i in range(samp):
            rand1 = random.randint(0,5000)
            rand2 = random.randint(0,5000)
            g.add_edge(rand1,rand2)


def recordData(experimentIdx):
    running_time = []
    current_usage = []
    peak_usage = []
    for idx in range(len(GRAPH_TYPES)):

        print("======",LIBRARY[idx])
        runningT = []
        currentU = []
        peakU = []

        for samp in SAMPLE:

            print(samp)
            start = time.time()
            tracemalloc.start()

            if experimentIdx == 1:
                experiment1(idx, samp)
            elif experimentIdx == 2:
                experiment2(idx, samp)

            end = time.time()
            current, peak = tracemalloc.get_traced_memory()

            runningT.append(end-start)
            currentU.append(current / 10**6)
            peakU.append(peak / 10**6)
            #print(GRAPH_TYPES[idx1])
            #print("Spent", end-start, " second.")
            #print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
            tracemalloc.stop()

        running_time.append(runningT)
        current_usage.append(currentU)
        peak_usage.append(peakU)

    return running_time, current_usage, peak_usage

def visualization(running_time, current_usage, peak_usage, experiment):
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
    for current in current_usage:
        plt.plot(SAMPLE, current, label = LIBRARY[i])
        i+= 1
    plt.ylabel('Current Memory Usage')
    plt.title(experiment)
    plt.legend()
    plt.savefig(experiment + "_current_usage.png")
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
    running_time, current_usage, peak_usage = recordData(1)
    visualization(running_time, current_usage, peak_usage, "Experiment1")


    print("======== Experiment 2 ========")
    running_time, current_usage, peak_usage = recordData(2)
    visualization(running_time, current_usage, peak_usage, "Experiment2")