import igraph

class Graph(igraph.Graph):
    def __init__(self):
        super(Graph, self).__init__()

    def add_node(self, id):
        super(Graph, self).add_vertex()

    def add_edge(self, uid, vid):
        super(Graph, self).add_edges([(uid,vid)])

    def number_of_nodes(self):
        return super(Graph, self).vcount()

    def in_edges(self, uid):
        return super(Graph, self).incident(uid)