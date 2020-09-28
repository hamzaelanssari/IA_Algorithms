from Breadth_First_Search.Algorithm import BFS
from Breadth_First_Search.Vertex import Vertex

vertex1=Vertex(1)
vertex2=Vertex(2)
vertex3=Vertex(3)
vertex4=Vertex(4)
vertex5=Vertex(5)
vertex6=Vertex(6)
vertex7=Vertex(7)
vertex1.AddNeighbor(vertex2)
vertex1.AddNeighbor(vertex3)
vertex3.AddNeighbor(vertex6)
vertex3.AddNeighbor(vertex7)
vertex2.AddNeighbor(vertex4)
vertex2.AddNeighbor(vertex5)
BFS(vertex1)

