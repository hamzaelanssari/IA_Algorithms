def BFS(start, goal):
    Open = [start]
    path = []
    vertex_tested = 0
    vertex_not_tested = 0
    while len(Open) != 0:
        position = 0
        min_h = Open[position].getH()
        for i, j in enumerate(Open):
            if (j.getH() < min_h):
                min_h = j.getH()
                position = i
        actual = Open.pop(position)
        actual.setVisited()
        vertex_tested = vertex_tested + 1
        for v in actual.getNeighbors():
            if not v.getVertex().isVisited():
                if v.getVertex() not in Open:
                    v.getVertex().setFather(actual)
                    v.getVertex().setG(v.getValue() + actual.getG())
                    Open.append(v.getVertex())

        if actual == goal:
            vertex_not_tested = len(Open)
            Open.clear()
            vertex = actual
            while vertex is not None:
                path.insert(0, vertex)
                vertex = vertex.getFather();
            break
    print("chemin : ", end="")
    cost = actual.getG()
    for i in path:
        print(i.getName(), "-->", end="")
    print("end\ncost :", cost)
    print("Vertex tested :", vertex_tested)
    print("Vertedx not tested :", vertex_not_tested)
