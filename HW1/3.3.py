import numpy as np
import matplotlib.pyplot as plt
import random
x = []
xmin = 1
alpha = 2
numberOfNumbers = 100

for i in range(100):
    b = random.uniform(0,1)
    x.append(xmin*b**(1/(1-alpha)))
x.sort()

print(x)
plt.hist(x, bins = 40) 
plt.title("p(n)")
plt.show()
