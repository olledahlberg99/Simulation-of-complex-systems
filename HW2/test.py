import numpy as np
T = 300
R = 0.000001
eta = 0.001
m = 0.0000000000000111
kB = 0.00000000000000000000001380649
gamma = 6*np.pi*eta*R
tau = m/gamma
numberOfParticles = 1000
t = 0.01*tau
timesteps = int(100*tau/t)
k = t*gamma/m


# Calculating time-average and ensemble-average
nTimeStepsLong = 10**6
xTrajTime = np.zeros(nTimeStepsLong)
w = np.random.randn(nTimeStepsLong)
# Time average, with mass, time steps = 1 000 000, particle = 1
x1 = [0,0]
for i in range(2,nTimeStepsLong+2):
    x1.append((2+k)/(1+k)*x1[i-1] - 1/(1+k)*x1[i-2] + np.sqrt(2*kB*T*gamma)/m*(1+k)*t**(3/2)*w[i-2])
    xTrajTime[i-2] = x1[i]
    
# Ensemble average, with mass, time steps = 1 000, particles = 1000
nTimeStepsShort = 1000    
nParticles = 1000
xTrajEnsemble = []

for i in range(nParticles):
    x2 = [0,0]
    x2Temp = []
    w = np.random.randn(nTimeStepsLong)
    for j in range(2,nTimeStepsShort+2):
        x2.append((2+k)/(1+k)*x2[j-1] - 1/(1+k)*x2[j-2] + np.sqrt(2*kB*T*gamma)/m*(1+k)*t**(3/2)*w[i-2])
        x2Temp.append(x2[j])
    xTrajEnsemble.append(x2Temp)

# MSD Calculation
MSDTime = []
MSDEnsemble = []

for i in range(len(xTrajTime)):
    dr = ((xTrajTime[i]-xTrajTime[0])**2)
    MSDTime.append(dr/(nTimeStepsLong))

for i in range(nTimeStepsShort):
    MSDETemp = 0
    for j in range(nParticles):
        MSDETemp += (xTrajEnsemble[j][i]-xTrajEnsemble[j][0])**2
    MSDEnsemble.append(MSDETemp/nParticles)

print(np.sum(MSDEnsemble)/nTimeStepsShort)
print(np.sum(dr))