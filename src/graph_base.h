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
public:
    Node(int id, std::string& name):
        m_Id(id), m_Name(name) {}

    int getNId(){return m_Id;}

protected:
//    std::shared_ptr<GraphBase> m_Graph;
    int m_Id;
    std::string m_Name;
};


class Edge {
public:
    Edge(int id, std::shared_ptr<Node>& p_source, std::shared_ptr<Node>& p_target):
        m_Id(id), m_Source(p_source), m_Target(p_target) {}


protected:
//    std::shared_ptr<GraphBase> m_Graph;
    int m_Id;
    std::shared_ptr<Node> m_Source;
    std::shared_ptr<Node> m_Target;
};


class GraphBase {
public:
    GraphBase() {}

    Node AddNode(std::string name);
    Edge AddEdge(std::string name, std::string srcName, std::string tgtName);
    std::vector<Edge> GetInEdges(std::shared_ptr<Node> u);
    std::vector<Edge> GetOutEdges(std::shared_ptr<Node> u);
};


#endif //IGLSYNTH_GRAPH_BASE_H
