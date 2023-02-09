import matplotlib.pyplot as plt
import numpy as np

def f(x,r):
    return x+r -x**2

#initial condition

X0 = np.arange(0.1,0.2,0.1)

#a = 1.0

for x0 in X0:
    r = 1
    N= 20

    i = np.arange(0,N,1)
    x = x0
    X = []
    for _ in i:
        X.append(x)
        x = f(x,r)
    plt.plot(X)

#plt.ylim([0,5])
#¿plt.yscale('log')
plt.show()