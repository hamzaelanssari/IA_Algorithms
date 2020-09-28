from Depth_First_Search.Vertex import Vertex
from Depth_First_Search.IterationAlgorithm import DFS
vertex1=Vertex(1)
vertex2=Vertex(2)
vertex3=Vertex(3)
vertex4=Vertex(4)
vertex5=Vertex(5)
vertex6=Vertex(6)
vertex7=Vertex(7)
vertex1.AddNeighbor(vertex2)
vertex1.AddNeighbor(vertex5)
vertex5.AddNeighbor(vertex6)
vertex5.AddNeighbor(vertex7)
vertex2.AddNeighbor(vertex3)
vertex2.AddNeighbor(vertex4)
DFS(vertex1)

