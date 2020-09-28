def DFS(vertex):
    Queue = []
    vertex.setVisit()
    Queue.insert(0, vertex)
    # list=[]
    while len(Queue) != 0:
        position = Queue.index(Queue[-1])
        actual = Queue.pop()
        # list.append(actual.getValue())
        print(actual.getValue(), "-->", end="")
        for v in actual.getNeighbors():
            if not v.isVisited():
                v.setVisit()
                Queue.insert(position, v)
    # print(list)
    print("end")
