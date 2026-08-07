import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle

from triangulations import get_all_triangulations

quilt_width = 16

poly = np.array([[0,0], [2,0], [2, 2], [0,2], [0,0]])
bucket = get_all_triangulations(poly[:-1])

fig, ax = plt.subplots(figsize=(16,5), tight_layout=True)

for k in range(len(bucket)):
    col = (k % quilt_width) * 2
    row = (k // quilt_width) * 2

    # colors = cycle(['#A24A5C', '#4E5947', '#39353B', '#E8B3A9', '#1B1D17', '#4D1418', '#786D70', '#E89755'])
    # colors = cycle(['#A24A5C', '#73995C', '#39353B', '#E8B3A9', '#0E5011', '#350609', '#786D70', '#E89755'])


    for tri in bucket[k]:
        xs, ys = zip(*tri)
        xs = np.array(xs) + col
        ys = np.array(ys) + row
        ax.fill(xs, ys, closed=True, color=next(colors), alpha=0.8, edgecolor='black', linewidth=0.8, joinstyle='round')

    x = poly[:,0] + col
    y = poly[:,1] + row
    ax.plot(x, y, c='black', lw=2, solid_capstyle='round', zorder=9)

ax.set_aspect('equal')
ax.axis(False)

fig.savefig("output-quilts/polygon_15_quilt_wide_b.pdf", dpi=1200, bbox_inches='tight')
print("Saved to output-quilts/polygon_15_quilt_wide_b.pdf")

# plt.show()
plt.close()
