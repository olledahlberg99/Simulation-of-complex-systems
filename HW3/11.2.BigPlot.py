import numpy as np
import random
import matplotlib.pyplot as plt


numberOfIndividuals = 1000
numberOfLoops = 1000
d = 0.8
initialInfectionRate = 0.01
gamma = 0.01
maxX = maxY = 100
beta = 0.4
#1 = suceptible, 2 = infected, 3 = recovered
individualPosition = []
individualStatus = []
StatusList = np.zeros((3,numberOfLoops))
Beta = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
BG = [80,70,60,50,40,30,20,10]

betaList = []
for bg in range(len(BG)):
    bgList = []
    for b in range(len(Beta)):
        beta = Beta[b]
        gamma = 1/(BG[bg]/beta)
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
        bgList.append(StatusList[2][numberOfLoops-1])
    print(bgList)
    betaList.append(bgList)

print(betaList)
plt.imshow(betaList)
plt.colorbar()
plt.show()
