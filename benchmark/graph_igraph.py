import igraph

class Graph(igraph.Graph):
    def __init__(self):
        super(Graph, self).__init__()

    def add_node(self, id):
        super(Graph, self).add_vertices(id)

    def add_edge(self, uid, vid):
        super(Graph, self).add_vertices(uid)
        super(Graph, self).add_vertices(vid)
        super(Graph, self).add_edges([(uid,vid)])

