from Best_First_Search.Algorithm import BFS
from Best_First_Search.Vertex import Vertex
from  Best_First_Search.arc import arc
import cmath

#Example 1
vertexA=Vertex(8,"A")
vertexB=Vertex(8,"B")
vertexC=Vertex(4,"C")
vertexD=Vertex(5,"D")
vertexE=Vertex(cmath.inf,"E")
vertexF=Vertex(cmath.inf,"F")
vertexH=Vertex(4,"H")
vertexK=Vertex(6,"K")
vertexG=Vertex(0,"G")
#from A
arc_A_B=arc(vertexB,1); arc_A_C=arc(vertexC,5); arc_A_D=arc(vertexD,8)
#from B
arc_B_E=arc(vertexE,3); arc_B_F=arc(vertexF,7); arc_B_G=arc(vertexG,9)
#from C
arc_C_H=arc(vertexH,5);arc_C_K=arc(vertexK,7)
#from D
arc_D_G=arc(vertexG,4)

#from H
arc_H_B=arc(vertexB,5);arc_H_D=arc(vertexD,7)


# A Neighnors
vertexA.AddNeighbor(arc_A_B);vertexA.AddNeighbor(arc_A_C);vertexA.AddNeighbor(arc_A_D)
# B Neighnors
vertexB.AddNeighbor(arc_B_E);vertexB.AddNeighbor(arc_B_F);vertexB.AddNeighbor(arc_B_G)
# C Neighnors
vertexC.AddNeighbor(arc_C_H);vertexC.AddNeighbor(arc_C_K);
# D Neighnors
vertexD.AddNeighbor(arc_D_G)
# H Neighnors
vertexH.AddNeighbor(arc_H_B);vertexH.AddNeighbor(arc_H_D)
'''
#Example 2

vertexF=Vertex(10,"F")
vertexG=Vertex(10,"G")
vertexA=Vertex(10,"A")
vertexB=Vertex(20,"B")
vertexD=Vertex(5,"D")
vertexH=Vertex(0,"H")
vertexC=Vertex(10,"C")
vertexE=Vertex(10,"E")
vertexK=Vertex(0,"K")
#from F
arc_F_G=arc(vertexG,15)
#from G
arc_G_A=arc(vertexA,10); arc_G_C=arc(vertexC,5)
#from A
arc_A_D=arc(vertexD,10);arc_A_H=arc(vertexH,10);arc_A_B=arc(vertexB,5)
#from B
arc_B_F=arc(vertexF,5)
#from D
arc_D_G=arc(vertexG,10);arc_D_E=arc(vertexE,5)
#from H
arc_H_B=arc(vertexB,5);arc_H_K=arc(vertexK,20)
#from C
arc_C_D=arc(vertexD,5)
#from E
arc_E_C=arc(vertexC,10);arc_E_A=arc(vertexA,5);arc_E_K=arc(vertexK,10)
#from K
arc_K_B=arc(vertexB,10)

# F Neighnors
vertexF.AddNeighbor(arc_F_G)
# G Neighnors
vertexG.AddNeighbor(arc_G_A);vertexG.AddNeighbor(arc_G_C)
# A Neighnors
vertexA.AddNeighbor(arc_A_B);vertexA.AddNeighbor(arc_A_H);vertexA.AddNeighbor(arc_A_D)
# B Neighnors
vertexB.AddNeighbor(arc_B_F)
# D Neighnors
vertexD.AddNeighbor(arc_D_G);vertexD.AddNeighbor(arc_D_E)
# H Neighnors
vertexH.AddNeighbor(arc_H_B);vertexH.AddNeighbor(arc_H_K)
# C Neighnors
vertexC.AddNeighbor(arc_C_D)
# E Neighnors
vertexE.AddNeighbor(arc_E_A);vertexE.AddNeighbor(arc_E_C);vertexE.AddNeighbor(arc_E_K)
# K Neighnors
vertexK.AddNeighbor(arc_K_B)'''
BFS(vertexA,vertexG)
