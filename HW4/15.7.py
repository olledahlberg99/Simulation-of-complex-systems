import numpy as np
import random 
from numpy.random import choice
import random
import numpy as np
import matplotlib.pyplot as plt

N = 16
M = np.zeros((N,N))
k = 80
rho = 0.5
alpha = 0.8
beta = 1


for i in range(N):
    for j in range(i+1,N):
        if random.uniform(0,1) < 0.5:
            M[i,j] = 1
            M[j,i] = 1
        else:
            M[i,j] = 0
            M[j,i] = 0
plt.subplot(1,3,1)
plt.imshow(M)

W = np.zeros((N,N))
D = np.zeros((N,N))
for i in range(N):
    for j in range(i+1,N):
        if M[i,j] == 1:
            r = random.uniform(1,100)
            W[i,j] = r
            W[j,i] = r
        else:
            W[i,j] = 100000000
            W[j,i] = 100000000
        D[i,j] = 1/W[i,j]
        D[j,i] = 1/W[j,i]
# plt.subplot(1,3,2)
# plt.imshow(W)
# plt.subplot(1,3,3)
# plt.imshow(D)



#Gå en route
numberOfAnts = 20
s0 = 1
target = 5
Q = 10
for ants in range(numberOfAnts):
    lista = []
    lista.append(s0)
    for i in range(k-1):
        temp = lista[i]
        templist = M[:,temp]
        index = np.where(templist == 1)
        lista.append(round(random.choice(random.choice(index))))
    lista = np.array(lista)

    print(lista)
    [index] = np.where(lista == target)
    tempvector = [j for j in range(index[0])]
    print(lista)
    for k in range(N):
        [index] = np.where(lista == k)
        if len(index) > 1:
            tempvector = [j for j in range(index[0],index[len(index)-1])]
            lista = np.delete(lista,tempvector)
    print(lista)
    L = 0
    for i in range(len(lista)-1):
        L += D[lista[i],lista[i+1]]

    P = np.multiply(P,(1-rho)) 

    for i in range(N):
        if i in lista:
            [index] = np.where(lista == i)
            P[lista[index],lista[index+1]] += Q/L
            P[lista[index+1],lista[index]] += Q/L        




# plt.subplot(1,3,2)
# plt.imshow(W)
# plt.subplot(1,3,3)
# plt.imshow(D)
# print(lista)
# plt.show()
#next choice
next = choice()




