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
        if(m_NodesId.find(name) != m_NodesId.end()){
            std::cout << "Node with name " << name << " is already existed." << std::endl;
            return m_Nodes[m_NodesId.find(name)->second];
        }

        int nid = m_Graph->AddNode();
        Node n = Node(nid, name);
        m_NodesId.insert({name, nid});
        m_Nodes[nid] = n;
        return n;
    }

    Edge AddEdge(std::string name, std::shared_ptr<Node> srcN, std::shared_ptr<Node> tgtN) {

        if(m_EdgesId.find(name) != m_EdgesId.end()){
            std::cout << "Edge with name " << name << " is already existed." << std::endl;
            return m_Edges[m_EdgesId.find(name)->second];
        }

        int eId = m_Graph->AddEdge(srcN->getNId(), tgtN->getNId());
        Edge edge = Edge(eId, srcN, tgtN);
        m_EdgesId.insert({name, eId});
        m_Edges[eId] = edge;
        return edge;

    }


    std::vector<Edge> GetInEdges(std::shared_ptr<Node> u) {
        Node n = *u;
        int nId = n.getNId();
        Node n_snap = m_Graph->GetNode(nId)
        std::vector<Edge> inEdges;


        //compile error here

        int inDeg = (m_Graph->GetNode(nId))->GetInDeg();
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
    std::unordered_map<std::string, int> m_NodesId;
    std::unordered_map<std::string, int> m_EdgesId;
    std::vector<Node> m_Nodes;
    std::vector<Edge> m_Edges;
};


#endif //IGLSYNTH_GRAPH_SNAP_H
