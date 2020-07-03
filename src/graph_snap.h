//
// Created by abhibp1993-ubuntu on 5/27/20.
//

#ifndef IGLSYNTH_GRAPH_SNAP_H
#define IGLSYNTH_GRAPH_SNAP_H

#include "graph_base.h"
#include <unordered_map>
#include <Snap.h>
#include <iostream>


class SnapGraph : public GraphBase {
public:
    SnapGraph() { m_Graph = TNEGraph::New(); }

    Node AddNode(std::string name) {
        // TODO: Check whether node with same name is already added.

        // Note: For benchmarking purposes, we know by design repetition is avoided.
        if(m_Nodes.find(name) != m_Nodes.end()){
            std::cout << "Node with name " << name << " is already existed." << std::endl;
            return m_Nodes.find(name)->second;
        }

        int nid = m_Graph->AddNode();
        Node n = Node(nid, name);
        m_Nodes.insert({name, n});
        return n;
    }

    Edge AddEdge(std::string name, Node srcN, Node tgtN) {

        if(m_Edges.find(name) != m_Edges.end()){
            std::cout << "Edge with name " << name << " is already existed." << std::endl;
            return m_Edges.find(name)->second;
        }

        int eId = m_Graph->AddEdge(srcN.getNId(), tgtN.getNId());
        std::shared_ptr<Node> src = std::make_shared<Node>(srcN);
        std::shared_ptr<Node> tgt = std::make_shared<Node>(tgtN);

        Edge edge = Edge(eId, src, tgt);
        m_Edges.insert({name, edge});
        return edge;

    }


    // Let's discuss this function after you have implemented AddEdge.
    std::vector<Edge> GetInEdges(std::shared_ptr<Node> u) {
        Node n = *u;
        std::vector<Edge> inEdges;
        int inDeg = n->GetInDeg();
        for(int i  = 0; i < inDeg; i++){
            int eId = m_Graph->GetInEId(i, n);
            inEdges.push_back(m_Egdes.find(eId).second);
        }
        return inEdges;
    }

    std::vector<Edge> GetOutEdges(std::shared_ptr<Node> u) {
        Node n = *u;
        std::vector<Edge> outEdges;
        int outDeg = n->GetOutDeg();
        for(int i  = 0; i < outDeg; i++){
            int eId = m_Graph->GetOutEId(i, n);
            outEdges.push_back(m_Egdes.find(eId).second);
        }
        return outEdges;
        
    }

private:
    PNEGraph m_Graph;
    std::unordered_map<std::string, Node> m_Nodes;
    std::unordered_map<std::string, Edge> m_Edges;
};


#endif //IGLSYNTH_GRAPH_SNAP_H
