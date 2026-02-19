



from matplotlib.patches import Circle, Rectangle

from aptapy.plotting import plt, apply_stylesheet, setup_gca

apply_stylesheet("aptapy-xkcd")


_POS_DICT = {}
_HOR_SPACING = 1.5
_VERT_SPACING = 1.5

def put(value: int, pos: tuple[float, float], label: str = None,
        seed: bool = False, fixed: bool = False, frame_size: float = 0.34) -> None:
    """Put a value at a position on the plot and store the position in a
    dictionary for later use.
    """
    if label is None:
        label = f"{value}"
    plt.text(*pos, label, ha='center', va='center', fontsize="small")
    _POS_DICT[value] = pos
    frame_kwargs = dict(edgecolor='black', facecolor='none')
    if seed:
        circle = Circle(pos, radius=frame_size, **frame_kwargs)
        plt.gca().add_patch(circle)
    if fixed:
        frame_size *= 1.15
        square = plt.Rectangle((pos[0] - frame_size, pos[1] - frame_size),
                               width=2*frame_size, height=2*frame_size, **frame_kwargs)
        plt.gca().add_patch(square)

def arrow(src: int, dest: int, padding: float = 0.25) -> None:
    """Connect two values with an arrow.
    """
    x1, y1 = _POS_DICT[src]
    x2, y2 = _POS_DICT[dest]
    if x1 == x2:
        padding *= _VERT_SPACING
        if y1 > y2:
            padding = -padding
        y1 += padding
        y2 -= padding
    elif y1 == y2:
        padding *= _HOR_SPACING
        if x1 > x2:
            padding = -padding
        x1 += padding
        x2 -= padding
    plt.gca().annotate("", xytext=(x1, y1), xy=(x2, y2), arrowprops=dict(arrowstyle="->"))


def seq(end: int, *run: int, direction: str = "left", seed: bool = True):
    dest = end
    for value in run:
        x, y = _POS_DICT[dest]
        if direction == "left":
            x -= _HOR_SPACING
        elif direction == "right":
            x += _HOR_SPACING
        elif direction == "above":
            y += _VERT_SPACING
        elif direction == "below":
            y -= _VERT_SPACING
        else:
            raise ValueError(f"Invalid direction: {direction}")
        put(value, (x, y), seed=seed and value == run[-1])
        arrow(value, dest)
        dest = value

def put_right(value: int, reference: int, connect: bool = True, seed: bool = True):
    """
    """
    x, y = _POS_DICT[reference]
    put(value, (x + _HOR_SPACING, y), seed=seed)
    if connect: arrow(value, reference)

def put_left(value: int, reference: int, connect: bool = True, seed: bool = True):
    """
    """
    x, y = _POS_DICT[reference]
    put(value, (x - _HOR_SPACING, y), seed=seed)
    if connect: arrow(value, reference)

def put_above(value: int, reference: int, vspace: float = 1.0, connect: bool = True,
              seed: bool = True):
    """
    """
    x, y = _POS_DICT[reference]
    put(value, (x, y + vspace * _VERT_SPACING), seed=seed)
    if connect: arrow(value, reference)

def put_below(value: int, reference: int, vspace: float = 1.0, connect: bool = True,
              seed: bool = True, label: str = None):
    """
    """
    x, y = _POS_DICT[reference]
    put(value, (x, y - vspace * _VERT_SPACING), seed=seed, label=label)
    if connect: arrow(value, reference)


plt.figure("middle_square", figsize=(10, 8))

# Sequences ending with 0
put(0, (_HOR_SPACING, 0), fixed=True)
seq(0, 2, 5, 84, 29, 36, 19, 14, 12, 11, 46, 92, 77, 76, 42)
seq(0, 1, 4, 7, direction="above")
put_above(69, 76)
put_below(3, 0, vspace=6.)
seq(3, 6, 8, 9, 64, 93, 44, 21, 96, 31)
put_above(63, 96)
put_above(38, 44)
put_above(62, 84, vspace=2., seed=False)
seq(62, 25, 16, 13, 56, 81)
put_above(87, 56)
put_below(78, 8, vspace=1.)
seq(78, 28, 91, 54)
put_below(17, 28)
put_above(37, 36)
put_above(68, 62, seed=False)
put_above(41, 68)
put_below(58, 36)
put_below(32, 2, vspace=3.)
seq(32, 18, 72, 27)
put_above(61, 72)
put_right(75, 62)
put_below(82, 72)
put_above(33, 8)
put_below(43, 84)
put_right(71, 4)
put_below(73, 32)
put_above(55, 2)
x, y = _POS_DICT[55]
put(45, (x - 0.5 * _HOR_SPACING, y), seed=True)
put(95, (x + 0.5 * _HOR_SPACING, y), seed=True)

# Sequences ending with 10
put(10, (-8. * _HOR_SPACING, -4. * _VERT_SPACING), fixed=True)
seq(10, 90, 30, 48, 22, 15, 34)
put_below(35, 22, seed=False)
put_below(66, 35)
put_below(67, 48, seed=False)
put_below(26, 67)
put_above(85, 22)
xy = _POS_DICT[85]
put(85, (xy[0] - 0.5 * _HOR_SPACING, xy[1]), seed=True)
put_above(70, 90, vspace=2., seed=False)
seq(70, 52, 39, 86)
put_above(23, 52)
put_above(59, 48)

# Sequences ending with 60
put(60, (-7. * _HOR_SPACING, 5. * _VERT_SPACING), fixed=True)
seq(60, 40, 20, 47, 74, 88, 83, 94)
put_below(80, 40, seed=False)
put_below(53, 80)
put_left(99, 80)
put_above(49, 40)
xy = _POS_DICT[49]
put(97, (xy[0] - 0.5 * _HOR_SPACING, xy[1]), seed=True)
put_above(51, 60)
xy = _POS_DICT[51]
put(98, (xy[0] + 0.5 * _HOR_SPACING, xy[1]), seed=True)

# 50 is an isolated point
put(50, (-12. * _HOR_SPACING, 3. * _VERT_SPACING), fixed=True, seed=True)

# The only loop.
# 57 -> 24 (79)
put(57, (-1. * _HOR_SPACING, 6. * _VERT_SPACING), seed=True)
put_right(24, 57, connect=False)
x1, y1 = _POS_DICT[57]
x2, y2 = _POS_DICT[24]
delta = 0.25 * _VERT_SPACING
kwargs = dict(arrowstyle="->", connectionstyle="angle,angleA=30,angleB=-30,rad=20")
plt.gca().annotate("", xy=(x1, y1 - delta), xytext=(x2, y2 - delta), arrowprops=kwargs)
plt.gca().annotate("", xy=(x2, y2 + delta), xytext=(x1, y1 + delta), arrowprops=kwargs)
put_below(79, 24)


plt.axis("off")
plt.subplots_adjust(left=0., right=1., top=1., bottom=0.)
plt.gca().set_aspect("equal")
setup_gca(xmin=-14.5 * _HOR_SPACING, xmax=2.5 * _HOR_SPACING,
          ymin=-8.5 * _VERT_SPACING, ymax=6.5 * _VERT_SPACING)

plt.savefig("./figures/middle_square.png")
plt.savefig("./figures/middle_square.pdf")

plt.show()