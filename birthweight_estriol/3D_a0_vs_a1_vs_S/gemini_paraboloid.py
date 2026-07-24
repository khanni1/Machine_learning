import matplotlib.pyplot as plt
import numpy as np

# Dataset
x_pts = np.array([1, 2, 3, 4, 5])
y_pts = np.array([1, 1, 2, 2, 4])

# Grid around optimum (a0 = -0.2, a1 = 0.73)
a0_vals = np.linspace(-3, 2.6, 100)
a1_vals = np.linspace(-0.5, 2.0, 100)
A0, A1 = np.meshgrid(a0_vals, a1_vals)

# SSE Calculation
SSE = np.sum([(y_pts[i] - (A0 + A1 * x_pts[i]))**2 for i in range(len(x_pts))], axis=0)

fig = plt.figure(figsize=(14, 6))

# --- Plot 1: Better 3D Angle ---
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
surf = ax1.plot_surface(A0, A1, SSE, cmap="viridis", alpha=0.9, edgecolor='none')
ax1.set_xlabel("a0 (Intercept)")
ax1.set_ylabel("a1 (Slope)")
ax1.set_zlabel("SSE")
ax1.set_title("3D Paraboloid (Rotated View)")
# Crucial: Adjust viewing angle (Elevation, Azimuth)
ax1.view_init(elev=30, azim=125)

# --- Plot 2: 2D Elliptical Contours ---
ax2 = fig.add_subplot(1, 2, 2)
# Draw contour rings
contours = ax2.contour(A0, A1, SSE, levels=20, cmap="viridis")
ax2.clabel(contours, inline=True, fontsize=8)
# Mark the minimum point
ax2.plot(-0.2, 0.7, 'red', marker='x', markersize=10, markeredgewidth=3, label="Minimum (OLS Solution)")

ax2.set_xlabel("a0 (Intercept)")
ax2.set_ylabel("a1 (Slope)")
ax2.set_title("Horizontal Slices = Perfect Ellipses!")
ax2.grid(True, linestyle="--", alpha=0.6)
ax2.legend()

plt.tight_layout()
plt.show()