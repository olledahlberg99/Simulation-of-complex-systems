import numpy as np
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import random
from matplotlib import colors

fire_pos = []
new_fire_pos = []
N = 16
forrest = np.zeros((N,N))
tgp = 0.01
lp = 0.2
count = 0
stored_fire = []
temp_stored_fire = []
temp_new_fire_pos = []



while count < 5000:
    fire_count = 0
    forrest[( np.random.rand(N,N)<tgp ) & (forrest==0) ] = 1   
    random_squarex = random.randint(1, N-1)
    random_squarey = random.randint(1, N-1) 


    if np.random.rand() < lp and forrest[random_squarex,random_squarey] == 1:
        
        temp_fire_count = 0
        temp_fire_pos = []
        temp_forrest = forrest.copy()
        np.random.shuffle(temp_forrest)
        print(temp_forrest)
        a,b = np.where(temp_forrest == 1)
        temp_fire_pos.append([a[1],b[1]])
        print(temp_fire_pos)
        while len(temp_fire_pos) > 0:
            for i,j in temp_fire_pos:
                if i < N-1 and temp_forrest[i+1,j] == 1:
                    temp_forrest[i+1,j] = 2
                    temp_new_fire_pos.append([i+1,j])
                if i > 0 and temp_forrest[i-1,j] == 1:
                    temp_forrest[i-1,j] = 2
                    temp_new_fire_pos.append([i-1,j])
                if j < N-1 and temp_forrest[i,j+1] == 1:
                    temp_forrest[i,j+1] = 2
                    temp_new_fire_pos.append([i,j+1])
                if j > 0 and temp_forrest[i,j-1] == 1:
                    temp_forrest[i,j-1] = 2
                    temp_new_fire_pos.append([i,j-1])
                temp_forrest[i,j] = 0
                temp_fire_count += 1
            temp_fire_pos = temp_new_fire_pos.copy()
            temp_new_fire_pos = []
        temp_stored_fire.append(temp_fire_count)


        
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
        stored_fire.append(fire_count)
    count += 1
print('japp')
print(stored_fire)
print(temp_stored_fire)