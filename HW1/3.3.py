import numpy as np
import matplotlib.pyplot as plt
import random
x = []
C = []
listOfNumbers = []
xmin = 3
numberOfNumbers = 100

for i in range(100):
    b = random.uniform(0,1)
    x.append(xmin*b**(1/(1-2)))


plt.hist(x, bins = 100) 
plt.title("p(n)")
plt.show()

for i in range(len(x)):
    C.append(((len(x)-i)/len(x)))
    xmax = max(x)
    x[i] = x[i]
x.sort()


for j in range(numberOfNumbers):
    r = random.uniform(0,1)
    difference = []
    for number in C:
        difference.append(abs(r-number))
    ind = difference.index(min(difference))
    listOfNumbers.append(round(x[ind]))

print(listOfNumbers)
plt.hist(listOfNumbers, bins = 100) 
plt.title("p(n)")
plt.show()

