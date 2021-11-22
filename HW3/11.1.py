import numpy as np
import random
import matplotlib.pyplot as plt

# plt.ion()
numberOfIndividuals = 1000
numberOfLoops = 1000
d = 0.8
initialInfectionRate = 0.03
gamma = 0.01
maxX = maxY = 100
beta = 0.4
#1 = suceptible, 2 = infected, 3 = recovered
individualPosition = []
individualStatus = []
StatusList = np.zeros((3,numberOfLoops))

for i in range(numberOfIndividuals):
    individualPosition.append([random.randint(0,maxX), random.randint(0,maxY)])
    individualStatus.append(1)

initialInfected = random.sample(range(numberOfIndividuals), round(numberOfIndividuals*initialInfectionRate))
for i in initialInfected:
    individualStatus[i] = 2


for k in range(numberOfLoops):
    for i in range(numberOfIndividuals):
        r = random.random()
        if r<d:
            move = np.random.choice([1,2,3,4])
            if move == 1:
                if individualPosition[i][0] < maxX:
                    individualPosition[i][0] += 1
                else:
                    individualPosition[i][0] = 0
            elif move == 2:
                if individualPosition[i][0] > 0:
                    individualPosition[i][0] -= 1
                else:
                    individualPosition[i][0] = maxX
            elif move == 3:
                if individualPosition[i][1] < maxY:
                    individualPosition[i][1] += 1
                else:
                    individualPosition[i][1] = 0
            elif move == 4:
                if individualPosition[i][1] > 0:
                    individualPosition[i][1] -= 1
                else:
                    individualPosition[i][1] = maxY

    for i in range(numberOfIndividuals):
        if individualStatus[i] == 2:
            indPos = individualPosition[i]
            if random.random() < beta:
                for j in range(numberOfIndividuals):
                    if individualPosition[j] == indPos and individualStatus[j] == 1:
                        individualStatus[j] = 2
            if random.random() < gamma:
                individualStatus[i] = 3
    
    for i in range(numberOfIndividuals):
        if individualStatus[i] == 1:
            StatusList[0][k] += 1
        if individualStatus[i] == 2:
            StatusList[1][k] += 1
        if individualStatus[i] == 3:
            StatusList[2][k] += 1
    # plt.clf()
    for i in range(numberOfIndividuals):
        if individualStatus[i] == 1:
            plt.scatter(individualPosition[i][0],individualPosition[i][1], color = "b")
        if individualStatus[i] == 2:
            plt.scatter(individualPosition[i][0],individualPosition[i][1], color = "r")
        if individualStatus[i] == 3:
            plt.scatter(individualPosition[i][0],individualPosition[i][1], color = "g")
    # plt.show()
    # plt.pause(0.001)
    
plt.plot(range(numberOfLoops), StatusList[0][:], "b")
plt.plot(range(numberOfLoops), StatusList[1][:], "r")
plt.plot(range(numberOfLoops), StatusList[2][:], "g")
plt.show()

print(StatusList)

    