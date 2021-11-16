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
W=np.random.randn(timesteps)
for i in range(2,timesteps+2):
    x1.append((2+t*(gamma/m))/(1+t*(gamma/m))*x1[i-1]-x1[i-2]/(1+t*(gamma/m))+ np.sqrt(2*kB*temp*gamma)/(m*(1+t*(gamma/m)))*np.power(t,3/2)*W[i-2])
    x2.append(x2[i-1]+np.sqrt((2*kB*temp*t)/gamma)*W[i-2])
    x1new.append(x1[i]*1e9)
    x2new.append(x2[i]*1e9)
xaxis = []
for i in range(timesteps):
    xaxis.append(i*0.01)

ax[0].plot(xaxis,x1new, "k--")
ax[0].plot(xaxis,x2new)

t = 0.01*tau

timesteps = int(100*tau/t)
x1 = []
x2 = []
x1new = []
x2new = []

W=np.random.randn(timesteps)
x1.append(0)
x1.append(0)
x2.append(0)
x2.append(0)
for i in range(2,timesteps+2):
    x1.append((2+t*(gamma/m))/(1+t*(gamma/m))*x1[i-1]-x1[i-2]/(1+t*(gamma/m))+ np.sqrt(2*kB*temp*gamma)/(m*(1+t*(gamma/m)))*np.power(t,3/2)*W[i-2])
    x2.append(x2[i-1]+np.sqrt((2*kB*temp*t)/gamma)*W[i-2])
    x1new.append(x1[i]*1e9)
    x2new.append(x2[i]*1e9)
xaxis = []
for i in range(timesteps):
    xaxis.append(i*0.01)

ax[1].plot(xaxis,x1new, "k--")
ax[1].plot(xaxis,x2new)




numberOfParticles = 1000
bigList1 = []
bigList2 = []
for j in range(numberOfParticles):
    x1 = []
    x2 = []
    x1new = []
    x2new = []
    x1.append(0)
    x1.append(0)
    x2.append(0)
    x2.append(0)
    for i in range(2,timesteps+2):
        r = np.random.randn(1)
        x1.append((2+t*(gamma/m))/(1+t*(gamma/m))*x1[i-1]-x1[i-2]/(1+t*(gamma/m))+ np.sqrt(2*kB*temp*gamma)/(m*(1+t*(gamma/m)))*np.power(t,3/2)*r)
        x2.append(x2[i-1]+np.sqrt((2*kB*temp*t)/gamma)*r)
        x1new.append(x1[i])
        x2new.append(x2[i])
    bigList1.append(x1new)
    bigList2.append(x2new)
    
mean1 = []
mean2 = []    
for j in range(timesteps):
    tempmean1 = 0
    tempmean2 = 0
    for i in range(numberOfParticles):
        tempmean1 += (bigList1[i][j]-bigList1[i][0])**2
        tempmean2 += (bigList2[i][j]-bigList2[i][0])**2
        print(bigList1[i][0])
    mean1.append(tempmean1/numberOfParticles)    
    mean2.append(tempmean2/numberOfParticles)


xaxis = []
for i in range(timesteps):
    xaxis.append(np.log10(i/100))
    mean1[i] = np.log10(mean1[i]*1e18)
    mean2[i] = np.log10(mean2[i]*1e18)

ax[2].plot(xaxis,mean1, "k--")
ax[2].scatter(xaxis,mean2)




plt.show()

