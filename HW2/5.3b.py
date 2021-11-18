import numpy as np
import matplotlib.pyplot as plt

temp = 300
R = 0.000001
eta = 0.001
m = 0.0000000000000111
kB = 0.00000000000000000000001380649
gamma = 6*np.pi*eta*R
tau = m/gamma
numberOfParticles = 100

matrix = np.zeros((100,100))
t = 0.01*tau
timesteps = 100
mean = 0
newmean = []
for j in range(numberOfParticles):
    for i in range(1,timesteps):
        r = np.random.randn(1)
        matrix[j,i] = matrix[j,i-1]+np.sqrt((2*kB*temp*t)/gamma)*r

for i in range(timesteps):
    a = 0
    for j in range(numberOfParticles):
        a += (matrix[j,i])**2
    newmean.append(a/numberOfParticles)

# for j in range(numberOfParticles):
#     x = []
#     x.append(0)
#     mean = 0
#     for i in range(1,timesteps):
#         r = np.random.randn(1)
#         x.append(x[i-1]+np.sqrt((2*kB*temp*t)/gamma)*r)
#         mean += (x[i])**2
#     newmean.append(mean/numberOfParticles)

# print(newmean)



x = []
timesteps = 10000
x.append(0)
for i in range(1,timesteps):
    r = np.random.randn(1)
    x.append(x[i-1]+np.sqrt((2*kB*temp*t)/gamma)*r)
mean = []
a = 0
for i in range(100):
    a = 0
    for j in range(timesteps-i):
        a += (x[j]-x[j+i])**2
    mean.append(a/(timesteps-i))
print(mean)
timesteps100 = 100
plt.plot(range(100),newmean,"r")
plt.plot(range(100), mean)
plt.show()





