import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,3)
temp = 300
R = 0.000001
eta = 0.001
m = 0.0000000000000111
kB = 0.00000000000000000000001380649
gamma = 6*np.pi*eta*R
tau = m/gamma
numberOfParticles = 1000


t = 10*tau
timesteps = 1000
mean = 0
for j in range(numberOfParticles):
    x = []
    x.append(0)
    for i in range(1,timesteps):
        r = np.random.randn(1)
        x.append(x[i-1]+np.sqrt((2*kB*temp*t)/gamma)*r)
        mean += (x[i]-x[0])**2
print(mean/(timesteps*numberOfParticles))


x = []
mean = 0
timesteps = 1000000
x.append(0)
for i in range(1,timesteps):
    r = np.random.randn(1)
    x.append(x[i-1]+np.sqrt((2*kB*temp*t)/gamma)*r)
    mean += (x[i]-x[0])**2

print(mean/timesteps)


