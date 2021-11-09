import numpy as np
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import random
import time
from matplotlib import colors

firePosition = []
newFirePosition = []

N = 16
forrest = np.zeros((N,N))
treeGrowthProbability = 0.01
lightningProbability= 0.5
loopCount = 0
fireSizes = []
fig = plt.figure()


while len(fireSizes) < 5000:
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
                elif i == N-1 and forrest[0,j] == 1:
                    forrest[0,j] = 2
                    newFirePosition.append([0,j])
                if i > 0 and forrest[i-1,j] == 1:
                    forrest[i-1,j] = 2
                    newFirePosition.append([i-1,j])
                elif i == 0 and forrest[N-1,j] == 1:
                    forrest[N-1,j] = 2
                    newFirePosition.append([N-1,j])
                if j < N-1 and forrest[i,j+1] == 1:
                    forrest[i,j+1] = 2
                    newFirePosition.append([i,j+1])
                elif j == N-1 and forrest[i,0] == 1:
                    forrest[i,0] = 2
                    newFirePosition.append([i,0])
                if j > 0 and forrest[i,j-1] == 1:
                    forrest[i,j-1] = 2
                    newFirePosition.append([i,j-1])
                elif j == 0 and forrest[i,N-1] == 1:
                    forrest[i,N-1] = 2
                    newFirePosition.append([i,N-1])
                forrest[i,j] = 3
                fireCount += 1
            firePosition = newFirePosition.copy()
            newFirePosition = []
        ax = fig.add_subplot(111)
        colormap = colors.ListedColormap(['black','green','red','red'])
        norm = colors.BoundaryNorm([-1,0.5,1.5,2.5,3.5], colormap.N)
        ax.matshow(forrest,cmap=colormap, norm = norm)
        plt.draw()
        plt.pause(6)
        forrest[forrest==3] = 0
    loopCount += 1
    print('Number of fires',len(fireSizes))
    if fireCount > 0:
        fireSizes.append(fireCount)
        print(fireCount)
    ax = fig.add_subplot(111)
    colormap = colors.ListedColormap(['black','green','red'])
    norm = colors.BoundaryNorm([-1,0.5,1.5,2.5], colormap.N)
    ax.matshow(forrest,cmap=colormap, norm = norm)
    plt.draw()
    plt.pause(0.0001)

print(fireSizes)



    
