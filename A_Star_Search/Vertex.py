class Vertex:
    def __init__(self, h, name, father=None):
        self.Name = name
        self.h = h  # this represents the heuristic estimated cost
        self.neighbors = []
        self.father = father
        self.g = 0
        self.visited = False

    def AddNeighbor(self, arc):
        self.neighbors.append(arc)

    def getNeighbors(self):
        return self.neighbors

    def getH(self):
        return self.h

    def setG(self, g):
        self.g = g

    def getG(self):
        return self.g

    def getName(self):
        return self.Name

    def getF(self):
        return self.g + self.h

    def setFather(self, father):
        self.father = father

    def getFather(self):
        return self.father

    def isVisited(self):
        return self.visited

    def setVisited(self):
        self.visited = True
