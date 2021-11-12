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


t = 0.01*tau
timesteps = int(1*tau/t)
x1 = []
x2 = []
x1new = []
x2new = []


x1.append(0)
x1.append(0)
x2.append(0)
x2.append(0)
for i in range(2,timesteps+2):
    x1.append((2+t*(gamma/m))/(1+t*(gamma/m))*x1[i-1]-x1[i-2]/(1+t*(gamma/m))+ np.sqrt(2*kB*temp*gamma)/(m*(1+t*(gamma/m)))*np.power(t,3/2)*np.random.normal(0,1))
    x2.append(x2[i-1]+np.sqrt((2*kB*temp*t)/gamma)*np.random.normal(0,1))
    x1new.append(x1[i])
    x2new.append(x2[i])
xaxis = range(timesteps)


ax[0].plot(xaxis,x1new, "k--")
ax[0].plot(xaxis,x2new)

t = 0.01*tau
timesteps = int(100*tau/t)
x1 = []
x2 = []
x1new = []
x2new = []


x1.append(0)
x1.append(0)
x2.append(0)
x2.append(0)
for i in range(2,timesteps+2):
    x1.append((2+t*(gamma/m))/(1+t*(gamma/m))*x1[i-1]-x1[i-2]/(1+t*(gamma/m))+ np.sqrt(2*kB*temp*gamma)/(m*(1+t*(gamma/m)))*np.power(t,3/2)*np.random.normal(0,1))
    x2.append(x2[i-1]+np.sqrt((2*kB*temp*t)/gamma)*np.random.normal(0,1))
    x1new.append(x1[i])
    x2new.append(x2[i])
xaxis = range(timesteps)


ax[1].plot(xaxis,x1new, "k--")
ax[1].plot(xaxis,x2new)

plt.show()

