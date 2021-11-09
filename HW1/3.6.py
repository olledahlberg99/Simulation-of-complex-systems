import numpy as np
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import random
from matplotlib import colors
from scipy.stats import linregress

firePosition = []
newFirePosition = []
N = 256
forrest = np.zeros((N,N))
treeGrowthProbability = 0.01
lightningProbability= 0.2
count = 0
fireSizes = []



while count < 5000:
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

D = []
slope, intercept, r, p, se = linregress(new_alog,new_Clog)
alpha = 1-slope
print(alpha)
for i in range(len(fireSizes)):
    D.append(intercept+alog[i]*slope)



plt.scatter(alog,Clog)
plt.plot(alog,D,'r')



plt.show()