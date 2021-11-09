import numpy as np
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import random
from matplotlib import colors
from scipy.stats import linregress

firePosition = []
newFirePosition = []
treeGrowthProbability = 0.01
lightningProbability= 0.2
count = 0
fireSizes = []
variables = [16,32,64,128,256,512,1024]
alphaList = []

for p in range(len(variables)):
    N = variables[p]
    forrest = np.zeros((N,N))
    temp_alphaList = []
    for k in range(10):
        count = 0
        while count < 10000:
            fireCount = 0
            forrest[( np.random.rand(N,N)<treeGrowthProbability ) & (forrest==0) ] = 1   
            randomXPosition = random.randint(0, N-1)
            randomYPosition = random.randint(0, N-1) 


            if np.random.rand() < lightningProbability and forrest[randomXPosition,randomYPosition] == 1:
                
                
                forrest[randomXPosition,randomYPosition] = 2
                firePosition.append([randomXPosition,randomYPosition])
                while len(firePosition) > 0:
                    for i,j in firePosition:
                        if i < N-1 and forrest[i+1,j] == 1:
                            forrest[i+1,j] = 2
                            newFirePosition.append([i+1,j])
                        elif i == N-1 and forrest[1,j] == 1:
                            forrest[1,j] = 2
                            newFirePosition.append([1,j])
                        if i > 0 and forrest[i-1,j] == 1:
                            forrest[i-1,j] = 2
                            newFirePosition.append([i-1,j])
                        elif i == 0 and forrest[N-1,j] == 1:
                            forrest[N-1,j] = 2
                            newFirePosition.append([N-1,j])
                        if j < N-1 and forrest[i,j+1] == 1:
                            forrest[i,j+1] = 2
                            newFirePosition.append([i,j+1])
                        elif j == N-1 and forrest[i,1] == 1:
                            forrest[i,1] = 2
                            newFirePosition.append([i,1])
                        if j > 0 and forrest[i,j-1] == 1:
                            forrest[i,j-1] = 2
                            newFirePosition.append([i,j-1])
                        elif j == 0 and forrest[i,N-1] == 1:
                            forrest[i,N-1] = 2
                            newFirePosition.append([i,N-1])
                        forrest[i,j] = 0
                        fireCount += 1
                    firePosition = newFirePosition.copy()
                    newFirePosition = []
                fireSizes.append(fireCount)
            count += 1

        C = []
        for i in range(len(fireSizes)):
            C.append((len(fireSizes)-i)/len(fireSizes))
            fireSizes[i] = fireSizes[i]/(N**2)
        fireSizes.sort()
        Clog = []
        alog = []
        for i in range(len(fireSizes)):
            Clog.append(np.log10(C[i]))
            alog.append(np.log10(fireSizes[i]))

        new_Clog = []
        new_alog = []
        for i in range(len(fireSizes)):
            if alog[i] < -1:
                new_Clog.append(Clog[i])
                new_alog.append(alog[i])

        slope, intercept, r, p, se = linregress(new_alog,new_Clog)
        alpha = 1-slope
        temp_alphaList.append(alpha)
        print("N=",N,", Iteration = ",k,", alpha = ",alpha)
    alphaList.append(temp_alphaList)

print(alphaList)

meanList = []
Ninverse = []
for j in range(len(variables)):
    mean = 0
    Ninverse.append(1/variables[j])
    for i in range(10):
        mean = mean + alphaList[j][i]
    meanList.append(mean/10)
new_Ninverse = []
new_meanList = []
D = []

for i in range(len(variables)-1):
    new_Ninverse.append(Ninverse[i]) 
    new_meanList.append(meanList[i])
slope, intercept, r, p, se = linregress(new_Ninverse,new_meanList)
for i in range(len(variables)-1):
    D.append(intercept+Ninverse[i]*slope)

plt.scatter(Ninverse,meanList)
plt.plot(new_Ninverse,D,'r')
plt.show()
print(slope)


