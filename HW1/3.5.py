import numpy as np
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import random
from matplotlib import colors

firePosition = []
newFirePosition = []
N = 256
forrest = np.zeros((N,N))
treeGrowthProbability = 0.01
lightningProbability= 0.2
count = 0
fireSizes = []
temp_fireSizes = []
temp_newFirePosition = []



while count < 25000:
    fireCount = 0
    forrest[( np.random.rand(N,N)<treeGrowthProbability ) & (forrest==0) ] = 1   
    randomXPosition = random.randint(0, N-1)
    randomYPosition = random.randint(0, N-1) 


    if np.random.rand() < lightningProbability and forrest[randomXPosition,randomYPosition] == 1:
        
        temp_fireCount = 0
        temp_firePosition = []
        temp_forrest = forrest.copy()
        np.random.shuffle(temp_forrest)
        a,b = np.where(temp_forrest == 1)
        index = random.randint(0,len(a))
        temp_firePosition.append([a[index],b[index]])
        while len(temp_firePosition) > 0:
            for i,j in temp_firePosition:
                if i < N-1 and temp_forrest[i+1,j] == 1:
                    temp_forrest[i+1,j] = 2
                    temp_newFirePosition.append([i+1,j])
                elif i == N-1 and temp_forrest[1,j] == 1:
                    temp_forrest[1,j] = 2
                    temp_newFirePosition.append([1,j])
                if i > 0 and temp_forrest[i-1,j] == 1:
                    temp_forrest[i-1,j] = 2
                    temp_newFirePosition.append([i-1,j])
                elif i == 0 and temp_forrest[N-1,j] == 1:
                    temp_forrest[N-1,j] = 2
                    temp_newFirePosition.append([N-1,j])
                if j < N-1 and temp_forrest[i,j+1] == 1:
                    temp_forrest[i,j+1] = 2
                    temp_newFirePosition.append([i,j+1])
                elif j == N-1 and temp_forrest[i,1] == 1:
                    temp_forrest[i,1] = 2
                    temp_newFirePosition.append([i,1])
                if j > 0 and temp_forrest[i,j-1] == 1:
                    temp_forrest[i,j-1] = 2
                    temp_newFirePosition.append([i,j-1])
                elif j == 0 and temp_forrest[i,N-1] == 1:
                    temp_forrest[i,N-1] = 2
                    temp_newFirePosition.append([i,N-1])
                temp_forrest[i,j] = 0
                temp_fireCount += 1
            temp_firePosition = temp_newFirePosition.copy()
            temp_newFirePosition = []
        temp_fireSizes.append(temp_fireCount)


        
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
print('japp')
print(fireSizes)
print(temp_fireSizes)

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


temp_C = []
for i in range(len(temp_fireSizes)):
    temp_C.append((len(temp_fireSizes)-i)/len(temp_fireSizes))
    temp_fireSizes[i] = temp_fireSizes[i]/(N**2)
temp_fireSizes.sort()

temp_Clog = []
temp_alog = []
for i in range(len(temp_fireSizes)):
    temp_Clog.append(np.log10(temp_C[i]))
    temp_alog.append(np.log10(temp_fireSizes[i]))

plt.scatter(alog,Clog)
plt.scatter(temp_alog,temp_Clog)
plt.show()