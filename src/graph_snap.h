//
// Created by abhibp1993-ubuntu on 5/27/20.
//

#ifndef IGLSYNTH_GRAPH_SNAP_H
#define IGLSYNTH_GRAPH_SNAP_H

#include "graph_base.h"
#include <unordered_map>
#include <Snap.h>

class SnapGraph : public GraphBase {
public:
    SnapGraph() { m_Graph = TNEGraph::New(); }

    Node AddNode(std::string name) {
        // TODO: Check whether node with same name is already added.

        // Note: For benchmarking purposes, we know by design repetition is avoided. 
        if(m_Nodes.find(name) == m_Nodes.end()){
            printf("Node with name %c is already existed.", name);
            return Null;
        }

        int nid = m_Graph->AddNode();
        Node n = Node(nid, name);
        m_Nodes.insert({name, n});
        return n;
    }

    Edge AddEdge(std::string name, std::int SrcNId, std::int TgtNId) {
        if(m_Edges.find(name) == m_Edges.end()){
            printf("Edge with name %c is already existed.", name);
            return Null;
        }

        int eId = m_Graph->AddEdge(SrcNId, TgtNId);
        Node srcN = m_Graph->GetNode(SrcNId);
        Node tgtN = m_Graph->GetNode(TgtNId);
        Edge edge = Edge(eid, srcN, tgtN);
        m_Edges.insert({name, edge});
        return edge;

    }


    std::vector<Edge> GetInEdges(std::shared_ptr<Node> u) {
        Node n = u*;
        std::vector<Edge> inEdges;
        int inDeg = n->GetInDeg;
        for(int i  = 0; i < inDeg; i++){
            int eId = m_Graph->GetInEId(i, n);
            inEdges.push_back(m_Egdes.find(eId));
        }
        return inEdges;
    }

    std::vector<Edge> GetOutEdges(std::shared_ptr<Node> u) {
        Node n = u*;
        std::vector<Edge> outEdges;
        int outDeg = n->GetOutDeg;
        for(int i  = 0; i < outDeg; i++){
            int eId = m_Graph->GetOutEId(i, n);
            outEdges.push_back(m_Egdes.find(eId));
        }
        return outEdges;
        
    }

private:
    PNEGraph m_Graph;
    std::unordered_map<std::string, Node> m_Nodes;
    std::unordered_map<std::string, Edge> m_Edges;
};


#endif //IGLSYNTH_GRAPH_SNAP_H
