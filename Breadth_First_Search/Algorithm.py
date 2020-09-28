def BFS(vertex):
    Queue = []
    vertex.setVisit()
    Queue.append(vertex)
    # list=[]
    while len(Queue) != 0:
        actual = Queue.pop(0)
        # list.append(actual.getValue())
        print(actual.getValue(), "-->", end="")
        for v in actual.getNeighbors():
            if not v.isVisited():
                v.setVisit()
                Queue.append(v)
    # print(list)
    print("end")
