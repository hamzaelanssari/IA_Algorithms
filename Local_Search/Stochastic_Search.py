import random


def getFunction(x):
    return -(x - 1) * (x - 1) + 2


def Stochastic_Search():
    Start_Point = -2
    End_Point = 2
    max = getFunction(Start_Point)
    for i in range(1000):
        Test_Point = random.randint(Start_Point, End_Point)
        if getFunction(Test_Point) > max:
            max = Test_Point
    print("Maximum is: ", max)


if __name__ == '__main__':
    Stochastic_Search()
