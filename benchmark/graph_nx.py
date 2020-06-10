import networkx as nx


class Graph(nx.DiGraph):
    def __init__(self):
        super(Graph, self).__init__()

    def add_node(self, id):
        super(Graph, self).add_node(id)

    def add_edge(self, uid, vid):
        super(Graph, self).add_edge(uid, vid)

