def A_Star_Search(start, goal):
    Open = []
    Open.append(start)
    path = []
    cost = 0
    vertex_tested = 0
    vertex_not_tested = 0
    while len(Open) != 0:
        position = 0
        min_f = Open[position].getF()
        for i, j in enumerate(Open):
            if j.getF() < min_f:
                min_f = j.getF()
                position = i
        actual = Open.pop(position)
        actual.setVisited()
        vertex_tested = vertex_tested + 1
        for v in actual.getNeighbors():
            if not v.getVertex().isVisited():
                if v.getVertex() not in Open:
                    v.getVertex().setFather(actual)
                    v.getVertex().setG(actual.getG() + v.getValue())
                    Open.append(v.getVertex())
                else:
                    if v.getVertex().getF() > v.getVertex().getH() + v.getValue() + actual.getG():
                        v.getVertex().setFather(actual)
                        v.getVertex().setG(actual.getG() + v.getValue())
            # print(v.getVertex().getName(),"-->",v.getVertex().getF())
        if actual == goal:
            vertex_not_tested = len(Open)
            cost = actual.getF()
            Open.clear()
            vertex = actual
            while vertex is not None:
                path.insert(0, vertex)
                vertex = vertex.getFather();
            break
    print("chemin : ", end="")
    for i in path:
        print(i.getName(), "-->", end="")
    print("end\ncost :", cost)
    print("Vertex tested :", vertex_tested)
    print("Vertedx not tested :", vertex_not_tested)
