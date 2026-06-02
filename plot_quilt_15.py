import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle

from triangulations import get_all_triangulations

quilt_width = 8

poly = np.array([[0,0], [2,0], [2, 2], [0,2], [0,0]])
bucket = get_all_triangulations(poly[:-1])

for b in [6,7,8]:
    fig, ax = plt.subplots(figsize=(9,9), tight_layout=True)

    for k in range(len(bucket)):
        col = (k % quilt_width) * 2
        row = (k // quilt_width) * 2

        colors = cycle([
            '#eb3477', '#4934eb', '#48417d', '#b87783', '#4f2026',
            '#bf9399', '#d62728', '#ff9896', '#9467bd', '#c5b0d5',
            '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f'
        ])

        for tri in bucket[k]:
            xs, ys = zip(*tri)
            xs = np.array(xs) + col
            ys = np.array(ys) + row
            ax.fill(xs, ys, closed=True, color=next(colors), alpha=b/10,
                edgecolor='black', linewidth=0.8, joinstyle='round')

        x = poly[:,0] + col
        y = poly[:,1] + row
        ax.plot(x, y, c='black', lw=2, solid_capstyle='round', zorder=9)

    ax.set_aspect('equal')
    ax.axis(False)

    fig.savefig(f"output-quilts/polygon_15_quilt_{b}.pdf", dpi=1200, bbox_inches='tight')
    print(f"Saved to output-quilts/polygon_15_quilt_{b}.pdf")

    # plt.show()
    plt.close()
