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
            return NULL;
        }

        int nid = m_Graph->AddNode();
        Node n = Node(nid, name);
        m_Nodes.insert({name, n});
        return n;
    }

    Edge AddEdge(std::string name, std::int SrcNId, std::int TgtNId) {      // Incorrect. int is just referred as is.
//  Correct:   Edge AddEdge(std::string name, int SrcNId, int TgtNId) {

        if(m_Edges.find(name) == m_Edges.end()){    // Incorrect. If this clause is true, then it means that edge with this name does NOT exist.
            printf("Edge with name %c is already existed.", name);  // In C++, we prefer to use std::cout << string-to-print << std::endl;
            return NULL;
        }

        int eId = m_Graph->AddEdge(SrcNId, TgtNId);
        Node srcN = m_Graph->GetNode(SrcNId);           // This won't work. You are querying SNAP graph to return a Node object.
                                                        // Instead, I think you should be querying m_Nodes in SnapGraph data structure for it.
                                                        // Remember: SnapGraph data structure stores the names, id correspondence.
                                                        // and SNAP's TNEGraph stores nodes only by their IDs.
        Node tgtN = m_Graph->GetNode(TgtNId);
        Edge edge = Edge(eid, srcN, tgtN);
        m_Edges.insert({name, edge});
        return edge;

    }

    // Let's discuss this function after you have implemented AddEdge.
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
