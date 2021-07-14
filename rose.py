from numpy import pi, linspace, meshgrid, exp, sin, cos, mod
import matplotlib.pyplot as plt
import matplotlib


n = 1000
A, B, C = 2.0, 1.27, 8.0
R, THETA = meshgrid(linspace(0, 1, n), linspace(-2, 20 * pi, n))
petalNum = 3.6

# Ugly maths https://www.facebook.com/MATLAB
x = 1 - 0.50 * (1.25 * (1 - mod(petalNum * THETA, 2 * pi) / pi) ** 2 - 0.25) ** 2
phi = (pi / 2) * exp(-THETA / (C * pi))
y = A * (R ** 2) * (B * R - 1) ** 2 * sin(phi)
R2 = x * (R * sin(phi) + y * cos(phi))
X = R2 * sin(THETA)
Y = R2 * cos(THETA)
Z = x * (R * cos(phi) - y * sin(phi))

# plotting
matplotlib.rcParams["text.usetex"] = False
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, Z, cmap="OrRd", antialiased=True)
plt.axis("off")
plt.savefig("rose.jpg", dpi=500, bbox_inches="tight", pad_inches=0)
plt.show()
