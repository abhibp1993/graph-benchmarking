import iglsynthcpp as igl

g = igl.SnapGraph()
n1 = g.AddNode("n1")
n2 = g.AddNode("n2")
e = g.AddEdge("e", n1, n2)

print(g)
print(n1)
print(n2)
print(e)