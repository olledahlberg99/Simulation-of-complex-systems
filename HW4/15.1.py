import random
import numpy as np
import matplotlib.pyplot as plt

N = 16
M = np.zeros((N,N))
k = 8

for i in range(N):
    for j in range(i+1,N):
        if random.uniform(0,1) < 0.3:
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
plt.subplot(1,3,2)
plt.imshow(W)
plt.subplot(1,3,3)
plt.imshow(D)

lista = []
a = random.randint(0,N)
lista.append(a)
for i in range(k-1):
    print(lista)
    temp = lista[i]
    templist = M[:,temp]
    print(templist)
    index = np.where(templist == 1)
    print(random.choice(random.choice(index)))
    lista.append(round(random.choice(random.choice(index))))
print(lista)

P = 0
for i in range(len(lista)-1):
    P += D[lista[i],lista[i+1]]

print("start")
lista = np.array(lista)
for k in range(N):
    [index] = np.where(lista == k)
    print(index)
    for i in range(len(index)-1):
        tempvector = [j for j in range(index[i],index[i+1])]
        lista = np.delete(lista,tempvector)

print(lista)
plt.show()
