import iglsynthcpp as igl

g = igl.SnapGraph()
n1 = g.AddNode("n1")
n2 = g.AddNode("n2")
n3 = g.AddNode("n3")
n4 = g.AddNode("n4")
e1 = g.AddEdge("e1", n1, n2)
e2 = g.AddEdge("e2", n1, n3)
e3 = g.AddEdge("e3", n1, n4)



print(g)
print(n1)
print(n2)
print(e1)
print(g.GetInEdges(n1))
print(g.GetOutEdges(n1))