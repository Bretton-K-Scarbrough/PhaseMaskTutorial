import numpy as np
import matplotlib.pyplot as plt

# Phyiscal constants
Lx = 15.36e-3  # length of SLM
Ly = 8.64e-3
dx = 8e-6  # pixel pitch
dy = dx
Nx = int(Lx / dx)  # number of pixels
Ny = int(Ly / dy)

x = np.linspace(-Lx / 2, Lx / 2 - dx, Nx)
y = np.linspace(-Ly / 2, Ly / 2 - dy, Ny)

X, Y = np.meshgrid(x, y)

grating = np.cos(2 * np.pi * X / 1e-3) + np.cos(2 * np.pi * Y / 1e-3)
# grating = np.transpose(grating)
# print(np.shape(grating))
plt.imshow(grating, cmap="jet", extent=(-Lx / 2, Lx / 2, -Ly / 2, Ly / 2))
plt.show()
