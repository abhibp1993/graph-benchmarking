import snap

class Graph(snap.TNGraph):
    def __init__(self):
        super(Graph, self).__init__()

    def add_node(self, id):
        if not super(Graph, self).IsNode(id):
            super(Graph, self).AddNode(id)

    def add_edge(self, uid, vid):
        self.add_node(uid)
        self.add_node(vid)
        super(Graph, self).AddEdge(uid, vid)

    def number_of_nodes(self):
        return super(Graph, self).GetNodes()

    def in_edges(self, uid):
        return super(Graph, self).GetNI(uid).GetInDeg()


