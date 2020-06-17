import graph_tool as gt


class Graph(gt.Graph):
    def __init__(self):
        super(Graph, self).__init__()

    def add_node(self, id):
        super(Graph, self).add_vertex()

    def add_edge(self, uid, vid):
        super(Graph, self).add_edge(super(Graph, self).vertex(uid), super(Graph, self).vertex(vid))

    def number_of_nodes(self):
        return super(Graph, self).num_vertices()
        
    def in_edges(self, uid):
        return super(Graph, self).vertex(uid).in_edges()

