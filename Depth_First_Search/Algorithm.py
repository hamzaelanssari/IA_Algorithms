def DFS(vertex):
    vertex.setVisit=True
    print(vertex.getValue())
    for v in vertex.getNeighbors():
        if not v.isVisited():
            DFS(v)



