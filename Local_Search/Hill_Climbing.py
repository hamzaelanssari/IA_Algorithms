def getFunction(x):
    return -(x - 1) * (x - 1) + 2;


def HillClimbing():
    dx = 0.01;
    Start_Point = -2
    max = getFunction(Start_Point)
    actual_Point = Start_Point + dx
    while getFunction(actual_Point) > max or getFunction(actual_Point) == max:
        max = getFunction(actual_Point)
        print("X:", actual_Point, " y:", getFunction(actual_Point))
        actual_Point = actual_Point + dx
    print("Max with hill climbing: ", max)


if __name__ == '__main__':
    HillClimbing()
