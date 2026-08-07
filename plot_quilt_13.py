import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle

from triangulations import get_all_triangulations

quilt_width = 6

poly = np.array([[0,0], [2,0], [0,4], [0,0]])
apex_x = ((1+np.arange(2*quilt_width)) // 2) * 2
apex_y = (np.arange(2*quilt_width) % 2) * 4

bucket = get_all_triangulations(poly[:-1])

# for b in [6,7,8]:
for b in [7]:
    fig, ax = plt.subplots(figsize=(9*1.5,6*1.5), tight_layout=True)

    for k in range(len(bucket)):
        idx = k % (2*quilt_width)
        v_shift = (k // (2*quilt_width)) * 4
        sf = 1 if k % 2 == 0 else -1

        # colors = cycle(["#F2B505", "#C88F00", "#C0DC02", "#80C202", "#97D7F0", "#2FB4F5", "#CFAC96", "#948676"])
        colors = cycle(["#CFAC96", "#948676", "#C0DC02", "#80C202", "#97D7F0", "#2b77a6", "#F2B505", "#C88F00"])

        for tri in bucket[k]:
            xs, ys = zip(*tri)
            xs = (sf * np.array(xs)) + apex_x[idx]
            ys = (sf * np.array(ys)) + apex_y[idx] + v_shift

            ax.fill(xs, ys, closed=True, color=next(colors), alpha=b/10, edgecolor='black', linewidth=0.8, joinstyle='round')

        x = (sf * poly[:,0]) + apex_x[idx]
        y = (sf * poly[:,1]) + apex_y[idx] + v_shift
        ax.plot(x, y, c='black', lw=2, solid_capstyle='round', zorder=9)

    ax.set_aspect('equal')
    ax.axis(False)

    fig.savefig(f"output-quilts/polygon_13_quilt_print.pdf", dpi=1200, bbox_inches='tight')
    print(f"Saved to output-quilts/polygon_13_quilt_print.pdf")

    # plt.show()
    plt.close()
