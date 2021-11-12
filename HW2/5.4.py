import numpy as np
from matplotlib import pyplot as plt 

### Coefficients of the simulation ###


temp = 300
R = 0.000001
eta = 0.001
m = 0.0000000000000111
kB = 0.00000000000000000000001380649
gamma = 6*np.pi*eta*R
tau = m/gamma
kx = 1e-6              # Stiffness of the optical trap along x
ky = 5e-7              # Stiffness of the optical trap along y
t = 0.01
print(t)
N = int(1e5)

x = np.zeros(N)    # Initiated trajectory array x
y = np.zeros(N)    # Initiated trajectory array y
Wx=np.random.randn(N)  # Gaussian distributed random numbers 
Wy=np.random.randn(N)  # Gaussian distributed random numbers 

for i in range(N-1):
    x[i+1] = x[i] - kx*x[i]*t/gamma + np.sqrt(2*kB*temp*t/gamma)*Wx[i]      # Overdamped Langevin equation x
    y[i+1] = y[i] - ky*y[i]*t/gamma + np.sqrt(2*kB*temp*t/gamma)*Wy[i]      # Overdamped Langevin equation y 


plt.figure(figsize=(10,10))
plt.plot(x*1e9,y*1e9,'.',markersize=0.6)
plt.axis('equal')
plt.show()

plt.hist(x,bins = 30)
plt.show()

plt.hist(y,bins = 30)
plt.show()