import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
from itertools import cycle

from triangulations import get_all_triangulations

quilt_width = 5

poly = np.array([[0,0], [3,0], [0,3], [0,0]])
bucket = get_all_triangulations(poly[:-1])

apex_x = ((1+np.arange(2*quilt_width)) // 2) * 3
apex_y = (np.arange(2*quilt_width) % 2) * 3

fig, ax = plt.subplots(figsize=(6,9), tight_layout=True)

for k in range(len(bucket)):
    idx = k % (2*quilt_width)
    v_shift = (k // (2*quilt_width)) * 3
    sf = 1 if k % 2 == 0 else -1
    
    colors = cycle(plt.cm.tab20.colors)
    for tri in bucket[k]:
        xs, ys = zip(*tri)
        xs = (sf * np.array(xs)) + apex_x[idx]
        ys = (sf * np.array(ys)) + apex_y[idx] + v_shift

        ax.fill(xs, ys, closed=True, color=next(colors), alpha=7/10,
            edgecolor='black', linewidth=0.8, joinstyle='round')

    x = (sf * poly[:,0]) + apex_x[idx]
    y = (sf * poly[:,1]) + apex_y[idx] + v_shift
    ax.plot(x, y, c='black', lw=2, solid_capstyle='round', zorder=99)

    if sf == 1:
        t1, t2 = 135, 180
    else:
        t1, t2 = -45, 0

    ax.add_artist( Wedge((x[1],y[1]), 0.35, t1, t2, facecolor='white', edgecolor='black', zorder=9) )

ax.set_aspect('equal')
ax.axis(False)

fig.savefig("output-quilts/polygon_16_quilt_basepoint.pdf", dpi=1200, bbox_inches='tight')
print("Saved to output-quilts/polygon_16_quilt_basepoint.pdf")

# plt.show()
plt.close()
