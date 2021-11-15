import numpy as np
from matplotlib import pyplot as plt 
import math
fig, ax = plt.subplots(1,4)

temp = 300
R = 0.000001
eta = 0.001
m = 0.0000000000000111
kB = 0.00000000000000000000001380649
gamma = 6*np.pi*eta*R
tau = m/gamma
kx = 1e-6             # Stiffness of the optical trap along x
ky = 0.25e-6              # Stiffness of the optical trap along y
t = 0.01
N = int(1e5)
x = np.zeros(N)    # Initiated trajectory array x
y = np.zeros(N)    # Initiated trajectory array y

Wx=np.random.randn(N)  # Gaussian distributed random numbers 
Wy=np.random.randn(N)  # Gaussian distributed random numbers 


a = 0
g = []
b = [1,2,3,5,10]
for j in b:
    a = 0
    x = []
    x.append(0)
    for i in range(N-1):
        x.append(x[i] - j*1e-9*x[i]*t/gamma + np.sqrt(2*kB*temp*t/gamma)*Wx[i])
        a += abs(x[i])*1e-1
    g.append(a**2/(N-1))
    #     a += (x[i+1]-x[i])
    # g.append((a/(N-1))**2*1e12)

ax[3].scatter(b,g)
s = []
v = []
for i in range(1,100):
    k = i*0.1
    s.append(k)
    v.append(1e12*kB*temp/k)
ax[3].plot(s,v)

plt.show()