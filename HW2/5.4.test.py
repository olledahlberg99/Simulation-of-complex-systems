import numpy as np
from matplotlib import pyplot as plt 
import math

temp = 300
R = 0.000001
eta = 0.001
m = 0.0000000000000111
kB = 0.00000000000000000000001380649
gamma = 6*np.pi*eta*R
tau = m/gamma
kx = 1e-7              # Stiffness of the optical trap along x
ky = 0.25e-7              # Stiffness of the optical trap along y
t = 0.01
N = int(1e5)


x = np.zeros(N)    # Initiated trajectory array x
y = np.zeros(N)    # Initiated trajectory array y

Wx=np.random.randn(N)  # Gaussian distributed random numbers 
Wy=np.random.randn(N)  # Gaussian distributed random numbers 
b = []
c = []
for j in range(10):
    a = 0
    k = j*1e-7
    c.append(j)
    for i in range(N-1):
        x[i+1] = x[i] - k*x[i]*t/gamma + np.sqrt(2*kB*temp*t/gamma)*Wx[i] 
        a += abs(x[i+1]-x[i])
    b.append(a/N-1)
plt.plot(c,b)
plt.show()