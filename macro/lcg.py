
import pathlib
import sys

sys.path.append(pathlib.Path(__file__).parent.parent.as_posix())


from matplotlib.patches import Circle, Rectangle
import numpy as np

from aptapy.plotting import plt, apply_stylesheet, setup_gca

apply_stylesheet("aptapy-xkcd")

from mcmep.rng import LinearCongruentialGenerator

seed = 33
lcg = LinearCongruentialGenerator(seed, modulus=100, multiplier=21, increment=11)
seq = np.array([seed] + list(value for value in lcg) + [seed])
print(seq, len(seq))

# Convert X_n to u_n
seq = np.asarray(seq, dtype=float) / lcg._modulus
# Take pairs (u_n, u_{n+1})
x = seq[:-1]
y = seq[1:]
# Scatter plot
plt.scatter(x, y)
# Annotate points with their indices
for i, (_x, _y) in enumerate(zip(x, y)):
    plt.text(_x, _y + 0.03, str(i), ha='center', va='center', fontsize="x-small")


plt.text(x[0] + 0.02, y[0], "start", ha='left', va='center', fontsize="small")
plt.text(x[-1] + 0.02, y[-1], "stop", ha='left', va='center', fontsize="small")
plt.gca().set_aspect("equal")
setup_gca(xlabel="$u_n$", ylabel="$u_{n+1}$")

plt.savefig("./figures/lcg_spectral.png")
plt.savefig("./figures/lcg_spectral.pdf")

plt.show()
