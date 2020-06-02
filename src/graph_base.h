//
// Created by abhibp1993-ubuntu on 5/27/20.
//

#ifndef IGLSYNTH_GRAPH_BASE_H
#define IGLSYNTH_GRAPH_BASE_H

#include <memory>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

// Declarations
class GraphBase;


class Node {
    Node(std::shared_ptr<GraphBase>& p_graph, int id, std::string& name):
        m_Graph(p_graph), m_Id(id), m_Name(name) {}

protected:
    std::shared_ptr<GraphBase> m_Graph;
    int m_Id;
    std::string m_Name;
};


class Edge {
    Edge(std::shared_ptr<GraphBase>& p_graph, int id, std::shared_ptr<Node>& p_source, std::shared_ptr<Node>& p_target):
        m_Graph(p_graph), m_Id(id), m_Source(p_source), m_Target(p_target) {}

protected:
    std::shared_ptr<GraphBase> m_Graph;
    int m_Id;
    std::shared_ptr<Node> m_Source;
    std::shared_ptr<Node> m_Target;
};


class GraphBase {
public:
    virtual void AddNode(std::shared_ptr<Node> u) = 0;
    virtual void AddEdge(std::shared_ptr<Edge> e) = 0;
    virtual std::vector<Edge> GetInEdges(std::shared_ptr<Node> u) = 0;
    virtual std::vector<Edge> GetOutEdges(std::shared_ptr<Node> u) = 0;
};


#endif //IGLSYNTH_GRAPH_BASE_H
