import matplotlib.pyplot as plt
import numpy as np


def openFile(dataX, dataY):
    with open("temperatures.txt", "r") as myFile:
        for line in myFile:

            line = line.split(" ")
            dataX.append(line[0])
            dataY.append(float(line[1][:-1]))


def plotTempsLine(dataX, dataY):

    x_axis = tuple(dataY)
    x_axis = np.arange(len(x_axis))
    y_axis = np.array(dataY)

    plt.plot(x_axis, y_axis)
    plt.xlabel("Days")
    plt.ylabel("Temperature")
    plt.show()

def plotTempsBar(dataX, dataY):
    x_axis = tuple(dataY)
    x_axis = np.arange(len(x_axis))
    y_axis = np.array(dataY)

    plt.bar(x_axis, y_axis)
    plt.xlabel("Days")
    plt.ylabel("Temperature")
    plt.show()

def menu():
    print("Main Menu\n"
          "1. Plot as a line graph\n"
          "2. Plpt as a bar graph")
    choice = int(input("Enter your choice: "))
    return choice

def main():
    days = []  # x values on the graph
    temperatures = [] # y values on the graph
    openFile(days, temperatures)
    x = menu()

    if x == 1:
        plotTempsLine(days, temperatures)
    elif x == 2:
        plotTempsBar(days, temperatures)
    else:
        print("Invalid choice")



main()