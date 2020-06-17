import networkx as nx


class Graph(nx.MultiDiGraph):
    def __init__(self):
        super(Graph, self).__init__()

    def add_node(self, id):
        super(Graph, self).add_node(id)

    def add_edge(self, uid, vid):
        super(Graph, self).add_edge(uid, vid)

    def number_of_nodes(self):
        return super(Graph, self).number_of_nodes()

    def in_edges(self, uid):
        return super(Graph, self).in_edges(uid)
