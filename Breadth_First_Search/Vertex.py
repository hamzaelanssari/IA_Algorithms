from multiprocessing.dummy import Array


class Vertex:
    def __init__(self,value):
        self.value=value
        self.visited= False
        self.neighbors=[]
    def setVisit(self):
        self.visited=True
    def isVisited(self):
        return  self.visited
    def AddNeighbor(self,vertex):
        self.neighbors.append(vertex)
    def getNeighbors(self):
        return self.neighbors
    def getValue(self):
        return self.value
