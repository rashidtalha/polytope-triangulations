from math import dist
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

from triangulations import get_all_triangulations

N_BLOCKS   = 8
BLOCK_W_MM = 36.0 # mm
POLY_W_DT  = 2.0 # data units
POLY_P_DT  = 0.2 # data units
AXIS_P_DT  = 0.1 # data units
LINE_G_MM  = 0.2 # mm

BLOCK_W_DT = POLY_W_DT + 2 * POLY_P_DT # data units
DATA_MIN   = -AXIS_P_DT
DATA_MAX   = N_BLOCKS*BLOCK_W_DT + AXIS_P_DT

MM_PER_IN  = 25.4
MM_PER_DT  = BLOCK_W_MM / BLOCK_W_DT

AXIS_W_IN  = (N_BLOCKS*BLOCK_W_DT + 2*AXIS_P_DT) * (MM_PER_DT/MM_PER_IN)

def setup_figure():
    fig = plt.figure(figsize=(AXIS_W_IN, AXIS_W_IN))

    ax = fig.add_axes([0, 0, 1, 1])

    ax.set_xlim(DATA_MIN, DATA_MAX)
    ax.set_ylim(DATA_MIN, DATA_MAX)
    ax.set_aspect('equal')
    ax.axis('off')

    for k in range(N_BLOCKS+1):
        ax.hlines(k*BLOCK_W_DT, 0, N_BLOCKS*BLOCK_W_DT, 'r', lw=1)
        ax.vlines(k*BLOCK_W_DT, 0, N_BLOCKS*BLOCK_W_DT, 'r', lw=1)

    return fig, ax

def get_boundary_edges(polygon):
    n_verts = len(polygon)
    return [ (polygon[idx], polygon[(idx+1) % n_verts]) for idx in range(n_verts) ]

def plot_edge_3(ax, a, b, x_shift, y_shift):
    length = dist(a, b) / ( LINE_G_MM / MM_PER_DT)
    normal = ( -(b[1]-a[1]) / length, (b[0]-a[0]) / length)

    xu = [a[0] + x_shift + normal[0], b[0] + x_shift + normal[0]]
    xm = [a[0] + x_shift, b[0] + x_shift]
    xd = [a[0] + x_shift - normal[0], b[0] + x_shift - normal[0]]
    
    yu = [a[1] + y_shift + normal[1], b[1] + y_shift + normal[1]]
    ym = [a[1] + y_shift, b[1] + y_shift]
    yd = [a[1] + y_shift - normal[1], b[1] + y_shift - normal[1]]
    
    ax.plot(xu, yu, c='k', lw=0.5)
    ax.plot(xm, ym, c='k', lw=0.5)
    ax.plot(xd, yd, c='k', lw=0.5)

polygon = [(0,0), (2,0), (2,2), (0,2)]

all_triangulations = get_all_triangulations(polygon, "edges")
boundary_edges = get_boundary_edges(polygon)

fig, ax = setup_figure()

for idx, edges in enumerate(all_triangulations):
    col = ((idx % N_BLOCKS) * BLOCK_W_DT) + POLY_P_DT
    row = ((idx // N_BLOCKS) * BLOCK_W_DT) + POLY_P_DT

    for i_edge in edges:
        plot_edge_3(ax, i_edge[0], i_edge[1], col, row)

    for b_edge in boundary_edges:
        plot_edge_3(ax, b_edge[0], b_edge[1], col, row)

    ax.add_artist( Arc((col,row), 0.30, 0.30, theta1=0, theta2=90, color='k', lw=0.5) )
    ax.add_artist( Arc((col,row), 0.32, 0.32, theta1=0, theta2=90, color='k', lw=0.5) )
    ax.add_artist( Arc((col,row), 0.34, 0.34, theta1=0, theta2=90, color='k', lw=0.5) )

fig.savefig(f"output-quilts/polygon_15_laser.pdf")
print(f"Saved to output-quilts/polygon_15_laser.pdf")
# plt.show()
plt.close()
