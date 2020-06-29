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
        int nid = m_Graph->AddNode(); 
        Node n = Node(nid, name);
        m_Nodes.insert({name, n});
        return n;
    }

    Edge AddEdge(std::string name) {

    }

    std::vector<Edge> GetInEdges(std::shared_ptr<Node> u) {
        
    }

    std::vector<Edge> GetOutEdges(std::shared_ptr<Node> u) {
        
    }

private:
    PNEGraph m_Graph;
    std::unordered_map<std::string, Node> m_Nodes;
    std::unordered_map<std::string, Node> m_Edges;
};


#endif //IGLSYNTH_GRAPH_SNAP_H
