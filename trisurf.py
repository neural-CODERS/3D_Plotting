from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# reverse of Laplacian of Gaussian (LoG) filter to generate intresting shape
def LoG(x, y, sigma):
    temp = (x ** 2 + y ** 2) / (2 * sigma ** 2)
    return -1 / (np.pi * sigma ** 4) * (1 - temp) * np.exp(-temp)

# setting plot size to 12.8, 9.6
plt.rcParams["figure.figsize"] = 12.8, 9.6

# gerenerate test data all x2, y2, z2 are 2D arrays of size 49x49 
N = 49
half_N = N // 2
X2, Y2 = np.meshgrid(range(N), range(N))
Z2 = -LoG(X2 - half_N, Y2 - half_N, sigma=8)

# resaping 2D array into 1D array
X1 = np.reshape(X2, -1)
Y1 = np.reshape(Y2, -1)
Z1 = np.reshape(Z2, -1)

# creating 3D axes
ax = plt.axes(projection='3d')

#for trisurf 
ax.plot_trisurf(X1, Y1, Z1, cmap='twilight_shifted')

# show the 3D projection
plt.show()
