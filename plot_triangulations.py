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
        
        colors = cycle(['#27474A', '#6F8F99', '#163044', '#326EA0', '#2B4B63', '#99C1D1'])
        for tri in triangles:
            tri_vertices = list(tri) + [tri[0]]
            xs, ys = zip(*tri_vertices)
            ax.fill(xs, ys, alpha=1, color=next(colors), edgecolor='black', linewidth=0.8, joinstyle='round')
        
        ax.axis(False)
        ax.set_aspect('equal')
        # ax.set_title(title)
        
        fig.savefig(f"{title}.pdf", dpi=250, bbox_inches='tight')
        print(f"Saved to {title}.pdf")

        # plt.show()
        plt.close()

#########################

if __name__ == '__main__':
    polygon = [[0,0], [1,0], [2,1], [2,2], [1,2], [0,1]]
    res = get_all_triangulations(polygon, "triangles")
    print(f"The given polygon has {len(res):>2} triangulations")
    plot_triangulations(polygon, res, prefix=f"poly")
