from Perceptron.point import point
from Perceptron.corp import corp
from Perceptron.Algorithm import Perceptron
X=[16,8,12,20,10,15,6]
Y=[14,15,10,15,6,10,12]
print(X)
print(Y)
p1=point(2,0)
p2=point(0,3)
p3=point(3,0)
p4=point(1,1)
array=[corp(p1,1),corp(p2,0),corp(p3,0),corp(p4,1)]
Perceptron(0.5,0,5)