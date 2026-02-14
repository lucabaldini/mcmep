
from matplotlib.patches import Circle, Wedge
import numpy as np

from aptapy.plotting import plt, apply_stylesheet

apply_stylesheet("aptapy-xkcd")


num_sectors = 10
radius = 1.0
text_radius = 0.8 * radius
canvas_size = 1.2 * radius
sector_span = 360. / num_sectors
wedge_kwargs = dict(edgecolor='black', facecolor='none')

plt.figure(figsize=(6, 6))
plt.subplots_adjust(left=0, right=1, top=0.925, bottom=0)
plt.title("Wheel of Fortune")
ax = plt.gca()

for i in range(num_sectors):
    theta_min = 90. - 0.5 * sector_span - i * sector_span
    theta_max = theta_min + sector_span
    theta_mid = 0.5 * (theta_min + theta_max)
    wedge = Wedge(center=(0, 0), r=radius, theta1=theta_min, theta2=theta_max, **wedge_kwargs)
    ax.add_patch(wedge)
    x = text_radius * np.cos(np.deg2rad(theta_mid))
    y = text_radius * np.sin(np.deg2rad(theta_mid))
    ax.text(x, y, f"{i}", ha='center', va='center')

ax.set_aspect('equal')
ax.axis("off")
ax.set_xlim(-canvas_size, canvas_size)
ax.set_ylim(-canvas_size, canvas_size)

plt.savefig("./figures/wheel.png")
plt.savefig("./figures/wheel.pdf")

plt.show()