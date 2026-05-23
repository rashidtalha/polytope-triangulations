from math import gcd, atan2
import matplotlib.pyplot as plt

from triangulations import get_all_triangulations

def get_boundary_edges(polygon):  
    closed_poly = polygon + [polygon[0]]
    
    lattice_points = []
    for i in range(len(polygon)):
        p1 = closed_poly[i]
        p2 = closed_poly[i+1]
        
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        
        n_segments = gcd(abs(dx), abs(dy))    
        for step in range(n_segments):
            curr_x = p1[0] + step * (dx // n_segments)
            curr_y = p1[1] + step * (dy // n_segments)
            lattice_points.append((curr_x, curr_y))
            
    closed_lattice_points = lattice_points + [lattice_points[0]]
    
    edges = []
    for i in range(len(lattice_points)):
        edges.append((closed_lattice_points[i], closed_lattice_points[i+1]))
        
    return edges

def bounding_vectors(v, vector_list):
    vx, vy = v
    
    smallest_pos_angle = 10
    smallest_neg_angle = -10
    
    va = None
    vb = None
    for vi in vector_list:
        vix, viy = vi
        angle = atan2(vx * viy - vy * vix, vx * vix + vy * viy)
        
        if angle > 0:
            if angle < smallest_pos_angle:
                smallest_pos_angle = angle
                va = vi
        elif angle < 0:
            if angle > smallest_neg_angle:
                smallest_neg_angle = angle
                vb = vi
                
    return va, vb

def edge_type(edge, internal_edges, polygon):
    all_edges = internal_edges + get_boundary_edges(polygon)

    ea, eb = [], []
    for e in all_edges:
        if e != edge:
            if edge[0] in e:
                ea.append( (e[0][0]+e[1][0]-2*edge[0][0], e[0][1]+e[1][1]-2*edge[0][1]) )
            elif edge[1] in e:
                eb.append( (e[0][0]+e[1][0]-2*edge[1][0], e[0][1]+e[1][1]-2*edge[1][1]) )

    eea = bounding_vectors( (edge[1][0] - edge[0][0], edge[1][1] - edge[0][1]), ea)
    eeb = bounding_vectors( (edge[0][0] - edge[1][0], edge[0][1] - edge[1][1]), eb)

    for v in eea:
        if (-v[0], -v[1]) in eea:
            return "red"
    for v in eeb:
        if (-v[0], -v[1]) in eeb:
            return "red"

    for v in eea:
        if (-v[0], -v[1]) in eeb:
            return "green"
    for v in eeb:
        if (-v[0], -v[1]) in eea:
            return "green"

    return "blue"

def plot_coloured_edges(polygon, triangulations, prefix="triangulation"):
    x = [v[0] for v in polygon] + [polygon[0][0]]
    y = [v[1] for v in polygon] + [polygon[0][1]]
        
    for idx, internal_edges in enumerate(triangulations):
        fig, ax = plt.subplots(figsize=(5,5), tight_layout=True)
        ax.plot(x, y, 'k-', linewidth=2, solid_capstyle='round', zorder=9)
        
        for edge in internal_edges:
            xs, ys = zip(*edge)
            ax.plot(xs, ys, c=edge_type(edge, internal_edges, polygon), linewidth=1, solid_capstyle='round')
        
        ax.axis(False)
        ax.set_aspect('equal')
        ax.set_title(f"{prefix}_{idx+1:>03}")
        
        fig.savefig(f"{prefix}_{idx+1:>03}.png", dpi=250, bbox_inches='tight')
        print(f"Saved to {prefix}_{idx+1:>03}.png")

        plt.close()

#########################

if __name__ == '__main__':
    # polygon = [[0,0], [3,0], [0,3]]
    # polygon = [[0,0], [4,0], [0,2]]
    # polygon = [[0,0], [3,0], [0,2]]
    # polygon = [[1,0], [2,1], [2,2], [1,2], [0,1]]
    # polygon = [[0,0], [2,1], [1,2], [0,2]]
    # polygon = [[0,0], [2,1], [1,2], [0,1]]

    examples = [
        [[0,0], [2,1], [1,2]],
        [[1,0], [2,1], [1,2], [0,1]],
        [[0,0], [2,1], [1,2], [0,1]],
        [[0,0], [3,1], [2,2]],
        [[1,0], [2,1], [2,2], [1,2], [0,1]],
        [[0,0], [2,1], [1,2], [0,2]],
        [[0,0], [1,0], [2,1], [2,2], [1,2], [0,1]],
        [[0,0], [2,0], [2,1], [0,2]],
        [[1,0], [2,1], [2,2], [0,2], [0,1]],
        [[0,0], [2,1], [0,3]],
        [[0,0], [1,0], [2,1], [0,3]],
        [[0,0], [2,0], [2,1], [1,2], [0,2]],
        [[0,0], [2,0], [0,4]] ,
        [[0,0], [2,0], [2,1], [0,3]],
        [[0,0], [2,0], [2,2], [0,2]],
        [[0,0], [3,0], [0,3]]
    ]
    for idx in range(len(examples)):
        res = get_all_triangulations(examples[idx], "edges")
        print(f"Polygon {idx+1:>2} has {len(res):>2} triangulations")
        plot_coloured_edges(examples[idx], res, f"lines_poly_{idx+1:>02}")
        print()

