import numpy as np
import matplotlib.pyplot as plt
import random
x = []
xmin = 1
for i in range(100):
    b = random.uniform(0,1)
    x.append(xmin*b**(1/(1-2)))


plt.hist(x, bins = 100) 
plt.title("p(n)")
plt.show()


C = []
for i in range(len(x)):
    C.append(((len(x)-i)/len(x)))

# for i in range(len(x)):
#     C.append(i/len(x))

x.sort()
print(x)
newC = []
newx = []

#plt.plot(x,C)
plt.scatter(x, C)
plt.title("C(n)")
plt.show()
print(max(x))
for j in range(len(C)):
    x[j] = x[j]/max(x)
    newC.append(np.log10(C[j]))
    newx.append(np.log10(x[j]))   

plt.scatter(x,C)
plt.show()

plt.scatter(newx,newC)
plt.title("C(n)")
plt.show()

