import matplotlib.pyplot as plt
import numpy as np


def getFunction(x, g, numbers):
    result = 0
    for i in range(g + 1):
        result = result + numbers[i] * pow(x, i)
    return result


def BasicSearch():
    print("-----------------------------------------------\n"
          "this is an example of an function 1+5*x+4(x*x) \n"
          "number Num1= 1\nnumber Num2=5\nnumber Num3=4\n"
          "-----------------------------------------------")
    numbers = []
    g = int(input("the degree of function : "))
    for i in range(g + 1):
        message="enter number "+ str(i) +" : "
        number = float(input(str(message)))
        numbers.append(number)
    print(numbers)
    Start_Point = float(input("Start Point : "))
    Destination_Point = float(input("Destination Point : "))
    dx = float(input("Scale : "))
    # 100 linearly spaced numbers
    x = np.linspace(Start_Point, Destination_Point, 100)

    # the function, which is y = x^2 here
    y = 0
    for i in range(g + 1):
        y = y + numbers[i] * pow(x, i)

    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('graph!')
    plt.plot(x, y, 'r')

    max = getFunction(Start_Point, g, numbers)
    x_max = Start_Point
    x_min = Start_Point
    min = getFunction(Start_Point, g, numbers)
    i = Start_Point
    while i < Destination_Point:
        if (max < getFunction(i, g, numbers)):
            max = getFunction(i, g, numbers)
            x_max = i
        if (min > getFunction(i, g, numbers)):
            min = getFunction(i, g, numbers)
            x_min = i
        i = i + dx
    # plot the function
    plt.scatter(x_max, max, edgecolors='green')
    plt.scatter(x_min, min, edgecolors='blue')
    # show the plot
    plt.show()
    print("-----------------------------------------------")
    print("maximum --->\t x=", x_max, " and f(x)=", max)
    print("minimum --->\t x=", x_min, " and f(x)=", min)
    print("-----------------------------------------------")


if __name__ == '__main__':
    BasicSearch()
