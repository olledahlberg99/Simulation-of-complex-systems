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

for i in range(N-1):
    x[i+1] = x[i] - kx*x[i]*t/gamma + np.sqrt(2*kB*temp*t/gamma)*Wx[i]     # Overdamped Langevin equation x
    y[i+1] = y[i] - ky*y[i]*t/gamma + np.sqrt(2*kB*temp*t/gamma)*Wy[i]      # Overdamped Langevin equation y 

avgxList = []
avgyList = []
axisList = []
for j in range(300):
    axisList.append(j*t)
    avgx = 0
    avgy = 0
    for i in range(N-j):
        avgx += x[i]*x[i+j]
        avgy += y[i]*y[i+j]
    avgxList.append(abs(avgx/(N-j)))
    avgyList.append(abs(avgy/(N-j)))



ax[2].plot(axisList,avgxList)
ax[2].plot(axisList,avgyList)




k = np.linspace(0, 3,300)
o1 = []
o2 = []
# for i in range(len(k)):
#     o1.append((kB*temp)/kx*math.exp((-kx*k[i])/gamma))
#     o2.append((kB*temp)/ky*math.exp((-ky*k[i])/gamma))
for i in k:
    o1.append((kB*temp)/kx*math.exp((-kx*i)/gamma))
    o2.append((kB*temp)/ky*math.exp((-ky*i)/gamma))

    
ax[2].plot(k,o1,"k--")
ax[2].plot(k,o2,"k--")
ax[2].set_xlim([0,0.3])










ax[0].plot(x*1e9,y*1e9,'.',markersize=0.6)



val, axis, _ = ax[1].hist(x, bins = 100, density = True, color = "lightblue", histtype = "step", linewidth = 2)
a = np.linspace(max(axis),min(axis),100)
b = []
for i in range(len(a)):
    b.append(math.exp(((kx*a[i]**2)/2)/(-kB*temp))*max(val))    
    a[i] = a[i]
ax[1].plot(a,b, "k--")

val = []
axis = []
a = []
val, axis, _ = ax[1].hist(y, bins = 100, density = True,  color = "g", histtype = "step", linewidth = 2)
a = np.linspace(max(axis),min(axis),100)
b = []
for i in range(len(a)):
    b.append(math.exp(((ky*a[i]**2)/2)/(-kB*temp))*max(val))
    a[i] = a[i]
ax[1].plot(a,b,"k--")


a = 0
g = []
b = [1,2,3,5,10]
for j in b:
    a = 0
    x = []
    x.append(0)
    for i in range(N):
        x.append(x[i] - j*1e-9*x[i]*t/gamma + np.sqrt(2*kB*temp*t/gamma)*Wx[i])
        a += abs(x[i])
    g.append(a**2/(N))
    #     a += (x[i+1]-x[i])
    # g.append((a/(N-1))**2*1e12)

ax[3].scatter(b,g)
s = []
v = []
xaxis = np.linspace(0.1,10,N)
for i in range(N):
    v.append(1e14*kB*temp/xaxis[i])
ax[3].plot(xaxis,v)



plt.show() 
