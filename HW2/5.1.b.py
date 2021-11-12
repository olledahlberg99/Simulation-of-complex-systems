import random
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
bigList = []
numberOfRuns = 100
numberOfSteps = 1000
for j in range(numberOfRuns):
    list = []
    value = 0
    for i in range(numberOfSteps):
        value = value + np.random.normal(0,1)
        list.append(value)
    bigList.append(list)
numberList = range(0,numberOfSteps)
for i in range(numberOfRuns):
    plt.plot(bigList[i],numberList, "b")

plt.show()

finalNumber = []
for i in range(numberOfRuns):
    finalNumber.append(bigList[i][numberOfSteps-1])
plt.hist(finalNumber, bins=30)
plt.show()