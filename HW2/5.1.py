import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
fig, ax = plt.subplots(2,3)
bigList1 = []
bigList2 = []
bigList3 = []
variables1 = [1,-1]
variables3 = [-1, (1-np.sqrt(3))/2, (1+np.sqrt(3))/2]
numberOfRuns = 1000
numberOfSteps = 1000
for j in range(numberOfRuns):
    list1 = []
    list2 = []
    list3 = []
    value1 = 0
    value2 = 0
    value3 = 0
    for i in range(numberOfSteps):
        value1 = value1 + random.choice(variables1)
        value2 = value2 + np.random.normal(0,1)
        value3 = value3 + random.choice(variables3)
        list1.append(value1)
        list2.append(value2)
        list3.append(value3)
    bigList1.append(list1)
    bigList2.append(list2)
    bigList3.append(list3)
numberList = range(0,numberOfSteps)
for i in range(numberOfRuns):
    ax[0,0].plot(bigList1[i],numberList, linewidth = 0.01, color = "b")
    ax[0,1].plot(bigList2[i],numberList, linewidth = 0.01, color = "g")
    ax[0,2].plot(bigList3[i],numberList, linewidth = 0.01, color = "r")

finalNumber1 = []
finalNumber2 = []
finalNumber3 = []
for i in range(numberOfRuns):
    finalNumber1.append(bigList1[i][numberOfSteps-1])
    finalNumber2.append(bigList2[i][numberOfSteps-1])
    finalNumber3.append(bigList3[i][numberOfSteps-1])
ax[1,0].hist(finalNumber1, bins=30, color = "b")
ax[1,1].hist(finalNumber2, bins=30, color = "g")
ax[1,2].hist(finalNumber3, bins=30, color = "r")

plt.show()
