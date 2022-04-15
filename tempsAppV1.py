# introduction to how to use and create a plot, the basics
import matplotlib.pyplot as plt
import numpy as np


mylist = [1, 2, 3]
myYvalue = [6, 0, -1]
x_axis = np.array(mylist)
y_axis = np.array(myYvalue)

plt.plot(x_axis, y_axis)
plt.show()