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
kx = 1e-6             # Stiffness of the optical trap along x
ky = 0.25e-6              # Stiffness of the optical trap along y
t = 0.01
N = int(1e5)
x = []
y = []

x.append(0)
y.append(0)
Wx=np.random.randn(N)  # Gaussian distributed random numbers 
Wy=np.random.randn(N)  # Gaussian distributed random numbers 

for i in range(N-1):
    x.append((x[i] - kx*x[i]*t/gamma + np.sqrt(2*kB*temp*t/gamma)*Wx[i]))     # Overdamped Langevin equation x
    y.append((y[i] - ky*y[i]*t/gamma + np.sqrt(2*kB*temp*t/gamma)*Wy[i]))      # Overdamped Langevin equation y 

avgxList = []
avgyList = []
axisList = []
for j in range(300):
    axisList.append(j*t)
    avgx = 0
    avgy = 0
    for i in range(N-j):
        avgx += (x[i]-x[i+j])^2
        avgy += (y[i]-y[i+j])^2
    avgxList.append(abs(avgx/(N-j)))
    avgyList.append(abs(avgy/(N-j)))



plt.plot(axisList,avgxList)
plt.plot(axisList,avgyList)




k = np.linspace(0, 3,300)
o1 = []
o2 = []
# for i in range(len(k)):
#     o1.append((kB*temp)/kx*math.exp((-kx*k[i])/gamma))
#     o2.append((kB*temp)/ky*math.exp((-ky*k[i])/gamma))
for i in k:
    o1.append((kB*temp)/kx*math.exp((-kx*i)/gamma))
    o2.append((kB*temp)/ky*math.exp((-ky*i)/gamma))

    
# ax[2].plot(k,o1,"k--")
# ax[2].plot(k,o2,"k--")
# ax[2].set_xlim([0,0.3])