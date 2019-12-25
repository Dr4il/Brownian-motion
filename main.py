import numpy as npy
import matplotlib.pyplot as plot

npy.random.seed(20)

N = 501
T = 1
dt = T / (N - 1)
t = npy.linspace(dt, T, N)
dX = npy.sqrt(dt) * npy.random.rand(1, N)
X = npy.cumsum(dX, axis=1)
dY = npy.sqrt(dt) * npy.random.rand(1, N)
Y = npy.cumsum(dY, axis=1)
fix, ax = plot.subplots()
ax.set_title("Brownian motion")
# generating X,Y point at chart
ax.plot(X[0, :], Y[0, :])
ax.plot(X[0, 0], Y[0, 0], 'ro')
ax.plot(X[0, -1], Y[0, -1], 'yo')
plot.tight_layout()
plot.show()
