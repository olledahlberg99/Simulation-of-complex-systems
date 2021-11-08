import numpy as np
from tkinter import *
from PIL import Image
from PIL import ImageTk as itk
import time
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
from matplotlib import colors
import random


# Create forest
N = 16          # Setting parameters
p = 0.01        # Growth rate
f = 1         # Lighting probability

forest = np.zeros((N,N))    # Creating lattice by size N x N
fireCount = 0               # Counter for number of fires
fireLocations = []
fireLocationsNew = []
count = 0
fireSize = 0
colormap = colors.ListedColormap(['black','green','red','red'])
norm = colors.BoundaryNorm([-1,0.5,1.5,2.5,3.5], colormap.N)
plt.imshow(forest, cmap=colormap, norm=norm)
# Initialize forest and fire,    0 for empty, 1 for tree, 2 for fire

while count < 100:
    forest[( np.random.rand(N,N)<p ) & (forest==0) ] = 1
    r2 = np.random.random(1)
    lightningLocation = (np.random.rand(2)*N).astype(int)
    lightningX = lightningLocation[0]
    lightningY = lightningLocation[1]
    fireSize = 0
    if forest[lightningX,lightningY] == 1 and r2 < f:
        forest[lightningX,lightningY] = 2
        fireLocations.append([lightningX,lightningY])
        fireCount += 1
        fireLocationsNew = []
        while len(fireLocations) > 0:
            for i,j in fireLocations:
                if forest[min(i+1,N-1),j] == 1:                                    # check expansion to the right
                    forest[min(i+1,N-1),j] = 2
                    fireLocationsNew.append([min(i+1,N-1),j])
                if forest[max(i-1,0),j] == 1:                                      # check expansion to the left
                    forest[max(i-1,0),j] = 2
                    fireLocationsNew.append([max(i-1,0),j])
                if forest[i,min(j+1,N-1)] == 1:                                    # check expansion upwards
                    forest[i,min(j+1,N-1)] = 2
                    fireLocationsNew.append([i,min(j+1,N-1)])
                if forest[i,max(j-1,0)] == 1:                                      # check expansion downwards
                    forest[i,max(j-1,0)] = 2
                    fireLocationsNew.append([i,max(j-1,0)])
                forest[i,j] = 0
                fireSize += 1
            fireLocations = fireLocationsNew.copy()
            fireLocationsNew = []
        plt.imshow(forest)
    fireCount += 1
    count += 1
    print(count)
    print(fireCount)
    print(fireSize)