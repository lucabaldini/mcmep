
import pathlib
import sys

sys.path.append(pathlib.Path(__file__).parent.parent.as_posix())


from matplotlib.patches import Circle, Rectangle
import numpy as np

from aptapy.plotting import plt, apply_stylesheet, setup_gca

apply_stylesheet("aptapy-xkcd")

from mcmep.rng import LinearCongruentialGenerator


seed = 33
# With m = 100, we need a = 1 mod 20 (a in {21, 41, 61, 81}) and c coprime with 100
# i.e., c odd and not a multiple of 5.
# m = 21, c = 11 -> the second digit increases by one at each step.
# This is a consequence of the fact that the modulus is equal to the word size.
lcg = LinearCongruentialGenerator(seed, modulus=99, multiplier=67, increment=79)
seq = np.array([seed] + list(value for value in lcg))
print(seq, len(seq))
#for val in seq:
#    print(val % 10)
x = seq[:-1]
y = seq[1:]
plt.scatter(x, y)
plt.scatter([seed, seq[-1]], [seq[0], seed])
plt.text(seed, seq[0] + 3, "start", ha='center', va='center', fontsize="small")
plt.text(seq[-1], seed + 3, "stop", ha='center', va='center', fontsize="small")
plt.gca().set_aspect("equal")
setup_gca(xlabel="$X_n$", ylabel="$X_{n+1}$")
plt.show()