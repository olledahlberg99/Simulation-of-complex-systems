import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
fig, ax = plt.subplots(2,3)
t1 = 0.01
t1Steps = int(5/t1)
t2 = 0.05
t2Steps = int(5/t2)
t3 = 0.1
t3Steps = int(5/t3)
bigList1 = []
bigList2 = []
bigList3 = []
numberOfRuns = 10000
for j in range(numberOfRuns):
    list1 = []
    list2 = []
    list3 = []
    value1 = 0
    value2 = 0
    value3 = 0
    for i in range(t1Steps):
        value1 = value1 + np.random.normal(0,1)*np.sqrt(t1)
        list1.append(value1)
    for i in range(t2Steps):
        value2 = value2 + np.random.normal(0,1)*np.sqrt(t2)
        list2.append(value2)
    for i in range(t3Steps):
        value3 = value3 + np.random.normal(0,1)*np.sqrt(t3)
        list3.append(value3)

    bigList1.append(list1)
    bigList2.append(list2)
    bigList3.append(list3)
numberList1 = np.linspace(0,5,num=t1Steps)
numberList2 = np.linspace(0,5,num=t2Steps)
numberList3 = np.linspace(0,5,num=t3Steps)
for i in range(numberOfRuns):
    ax[0,0].plot(numberList1, bigList1[i], linewidth = 0.1, color = "b")
    ax[0,1].plot(numberList2, bigList2[i], linewidth = 0.1, color = "g")
    ax[0,2].plot(numberList3, bigList3[i], linewidth = 0.1, color = "r")

mean1 = []
for j in range(t1Steps):
    mean = 0
    for i in range(numberOfRuns):
        mean += (bigList1[i][j]-bigList1[i][0])**2
    mean1.append(mean/numberOfRuns)
print(mean1)

mean2 = []
for j in range(t2Steps):
    mean = 0
    for i in range(numberOfRuns):
        mean += (bigList1[i][j]-bigList1[i][0])**2
    mean2.append(mean/numberOfRuns)


mean3 = []
for j in range(t3Steps):
    mean = 0
    for i in range(numberOfRuns):
        mean += (bigList3[i][j]-bigList3[i][0])**2
    mean3.append(mean/numberOfRuns)




ax[1,0].plot(numberList1,mean1, color = "b")
ax[1,1].plot(numberList2,mean2, color = "g")
ax[1,2].plot(numberList3,mean3, color = "r")
plt.show()



