import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle

from triangulations import get_all_triangulations

quilt_width = 5
base = 3
poly = np.array([[0,0], [base,0], [0,base], [0,0]])

bucket = get_all_triangulations(poly[:-1])

apex_x = ((1+np.arange(2*quilt_width)) // 2) * base
apex_y = (np.arange(2*quilt_width) % 2) * base

fig, ax = plt.subplots(figsize=(6,9), tight_layout=True)

for k in range(len(bucket)):
    idx = k % (2*quilt_width)
    v_shift = (k // (2*quilt_width)) * base
    sf = 1 if k % 2 == 0 else -1
    
    colors = cycle(plt.cm.tab20.colors)
    for tri in bucket[k]:
        xs, ys = zip(*tri)
        xs = (sf * np.array(xs)) + apex_x[idx]
        ys = (sf * np.array(ys)) + apex_y[idx] + v_shift

        ax.fill(xs, ys, closed=True, alpha=0.5, color=next(colors), edgecolor='black', linewidth=0.8, joinstyle='round')

    x = (sf * poly[:,0]) + apex_x[idx]
    y = (sf * poly[:,1]) + apex_y[idx] + v_shift
    ax.plot(x, y, c='black', lw=2, solid_capstyle='round', zorder=9)

ax.set_aspect('equal')
ax.axis(False)

fig.savefig(f"polygon_16_quilt.pdf", dpi=1200, bbox_inches='tight')
print(f"Saved to polygon_16_quilt.pdf")

plt.show()
plt.close()
