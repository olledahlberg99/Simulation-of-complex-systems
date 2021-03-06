import numpy as np
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import random
import time
from matplotlib import colors

fire_pos = []
new_fire_pos = []

N = 16
forrest = np.zeros((N,N))
tgp = 0.01
lp = 0.2
count = 0
stored_fire = []
fig = plt.figure()


while len(stored_fire) < 5000:
    fire_count = 0
    forrest[( np.random.rand(N,N)<tgp ) & (forrest==0) ] = 1   
    
    random_squarex = random.randint(1, N-1)
    random_squarey = random.randint(1, N-1) 
    if np.random.rand() < lp and forrest[random_squarex,random_squarey] == 1:
        forrest[random_squarex,random_squarey] = 2
        fire_pos.append([random_squarex,random_squarey])
        while len(fire_pos) > 0:
            for i,j in fire_pos:
                if i < N-1 and forrest[i+1,j] == 1:
                    forrest[i+1,j] = 2
                    new_fire_pos.append([i+1,j])
                if i > 0 and forrest[i-1,j] == 1:
                    forrest[i-1,j] = 2
                    new_fire_pos.append([i-1,j])
                if j < N-1 and forrest[i,j+1] == 1:
                    forrest[i,j+1] = 2
                    new_fire_pos.append([i,j+1])
                if j > 0 and forrest[i,j-1] == 1:
                    forrest[i,j-1] = 2
                    new_fire_pos.append([i,j-1])
                forrest[i,j] = 0
                fire_count += 1
            fire_pos = new_fire_pos.copy()
            new_fire_pos = []
            ax = fig.add_subplot(111)
            colormap = colors.ListedColormap(['black','green','red'])
            norm = colors.BoundaryNorm([-1,0.5,1.5,2.5], colormap.N)
            ax.matshow(forrest,cmap=colormap, norm = norm)
            plt.draw()
    count += 1
    print('number of counts',count)
    if fire_count > 0:
        stored_fire.append(fire_count)
    #    print(fire_count)
    # ax = fig.add_subplot(111)
    # colormap = colors.ListedColormap(['black','green','red'])
    # norm = colors.BoundaryNorm([-1,0.5,1.5,2.5], colormap.N)
    # ax.matshow(forrest,cmap=colormap, norm = norm)
    # plt.draw()
    #plt.pause(0.0001)

print(stored_fire)



    
