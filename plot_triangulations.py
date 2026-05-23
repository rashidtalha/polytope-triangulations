from itertools import cycle
import matplotlib.pyplot as plt

from triangulations import get_all_triangulations

def plot_triangulations(polygon, triangulations, prefix="triangulation"):
    x = [v[0] for v in polygon] + [polygon[0][0]]
    y = [v[1] for v in polygon] + [polygon[0][1]]
        
    for idx, triangles in enumerate(triangulations):
        title = f"{prefix}_{idx+1:>003}"

        fig, ax = plt.subplots(figsize=(5, 5), tight_layout=True)
        ax.plot(x, y, 'k-', linewidth=2, solid_capstyle='round', zorder=9)
        
        colors = cycle(plt.cm.tab20.colors)
        for tri in triangles:
            tri_vertices = list(tri) + [tri[0]]
            xs, ys = zip(*tri_vertices)
            ax.fill(xs, ys, alpha=0.5, color=next(colors), edgecolor='black', linewidth=0.8, joinstyle='round')
        
        ax.axis(False)
        ax.set_aspect('equal')
        ax.set_title(title)
        
        # fig.savefig(f"{title}.png", dpi=250, bbox_inches='tight')
        # print(f"Saved to {title}.png")

        plt.show()
        plt.close()

#########################

if __name__ == '__main__':
    polygon = [[0,0], [2,1], [1,2], [0,1]]
    res = get_all_triangulations(polygon, "triangles")
    print(f"The given polygon has {len(res):>2} triangulations")
    plot_triangulations(polygon, res, prefix=f"poly")
