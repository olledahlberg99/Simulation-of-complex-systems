import numpy as np
import random 
from numpy.random import choice

#next choice
next = choice()


P = np.multiply(P,(1-rho))
for i in range(N):
    if exists == i in lista:
        [index] = np.where(lista == i)
        P[lista[index],lista[index+1]] += Q/L
        P[lista[index+1],lista[index]] += Q/L        

