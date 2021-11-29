from DSAGraph import *

#  _SETUP_ #
graph = DSAGraph()

# Vertices
graph.addVertex(1, "1")
graph.addVertex(2, "2")
graph.addVertex(3, "3")
graph.addVertex(4, "4")
graph.addVertex(5, "5")
graph.addVertex(6, "6")

# Edges (two directional)
graph.addEdgeObj(1, 2, "5m")
graph.addEdgeObj(1, 3, "4m")
graph.addEdgeObj(1, 6, "3m")
graph.addEdgeObj(2, 3, "6m")
graph.addEdgeObj(2, 5, "2m")
graph.addEdgeObj(4, 5, "8m")
graph.addEdgeObj(5, 6, "1m")

# Display
graph.display()

# Searches
testVert = graph.getVertex(1)

print("DEPTH-FIRST SEARCH")
graph.depthFirst(testVert)

print("BREADTH-FIRST SEARCH")

t = graph.breadthFirst(testVert)
for vertex in t:
    print(vertex)

print("\nDISPLAYING WITH EDGE OBJECTS")
graph.displayObjects()

print("\nPRINTING NEIGHBORS OF NODE LABEL '2'")
print(graph.getNeighbors(2))

