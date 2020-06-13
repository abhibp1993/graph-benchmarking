import snap

class Graph(snap.TNGraph):
    def __init__(self):
        super(Graph, self).__init__()

    def add_node(self, id):
        super(Graph, self).AddNode(id)

    def add_edge(self, uid, vid):
        if not super(Graph, self).IsNode(uid):
            super(Graph, self).AddNode(uid)
        if not super(Graph, self).IsNode(vid):
            super(Graph, self).AddNode(vid)
        super(Graph, self).AddEdge(uid, vid)


