import numpy as np
from matplotlib.path import Path

def get_polygon_area(vertices):
    x = vertices[:, 0]
    y = vertices[:, 1]
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

def get_lattice_points_in_polygon(vertices):
    points = np.array(vertices)
    min_x, min_y = points.min(axis=0).astype(int)
    max_x, max_y = points.max(axis=0).astype(int)
    grid_x, grid_y = np.mgrid[min_x:max_x+1, min_y:max_y+1]
    candidate_points = np.vstack([grid_x.ravel(), grid_y.ravel()]).T
    
    path = Path(points)
    mask = path.contains_points(candidate_points, radius=1e-9)
    return candidate_points[mask]

def is_primitive(p1, p2, p3):
    area = 0.5 * abs(p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1] - p2[1]))
    return np.isclose(area, 0.5)

def intersect(a, b, c, d):
    def ccw(p1, p2, p3):
        val = (p2[1]-p1[1])*(p3[0]-p2[0]) - (p2[0]-p1[0])*(p3[1]-p2[1])
        if abs(val) < 1e-9: return 0
        return 1 if val > 0 else -1

    if ccw(a, b, c) * ccw(a, b, d) < 0 and ccw(c, d, a) * ccw(c, d, b) < 0:
        return True
    return False

def find_all_triangulations(vertices):
    vertices = np.array(vertices)
    points = get_lattice_points_in_polygon(vertices)
    n_pts = len(points)
    
    possible_triangles = []
    for i in range(n_pts):
        for j in range(i + 1, n_pts):
            for k in range(j + 1, n_pts):
                if is_primitive(points[i], points[j], points[k]):
                    possible_triangles.append(frozenset([i, j, k]))

    area = get_polygon_area(vertices)
    target_count = int(round(area / 0.5))
    
    all_triangulations = []

    def backtrack(start_idx, current_triangulation, current_edges):
        if len(current_triangulation) == target_count:
            all_triangulations.append([list(t) for t in current_triangulation])
            return

        for i in range(start_idx, len(possible_triangles)):
            tri_indices = list(possible_triangles[i])
            # Potential new edges from this triangle
            new_edges = [(tri_indices[0], tri_indices[1]), 
                         (tri_indices[1], tri_indices[2]), 
                         (tri_indices[2], tri_indices[0])]
            
            collision = False
            for ne in new_edges:
                for ce in current_edges:
                    if intersect(points[ne[0]], points[ne[1]], points[ce[0]], points[ce[1]]):
                        collision = True
                        break
                if collision: break
            
            if not collision:
                backtrack(i + 1, current_triangulation + [tri_indices], current_edges + new_edges)

    backtrack(0, [], [])
    
    output = []
    for triangulation in all_triangulations:
        t_coords = [[points[idx].tolist() for idx in tri] for tri in triangulation]
        output.append(t_coords)
        
    return output

poly_coords = [[0, 0], [1, 0], [1, 1], [0, 1]]

# poly_coords = [[0,0], [2,1], [1,2]]
# poly_coords = [[1,0], [2,1], [1,2], [0,1]]
# poly_coords = [[0,0], [2,1], [1,2], [0,1]]
# poly_coords = [[0,0], [3,1], [2,2], [1,1]]
# poly_coords = [[1,0], [2,1], [2,2], [1,2], [0,1]]
# poly_coords = [[0,0], [2,1], [1,2], [0,2], [0,1]]
# poly_coords = [[0,0], [1,0], [2,1], [2,2], [1,2], [0,1]]
# poly_coords = [[0,0], [1,0], [2,0], [2,1], [0,2], [0,1]]
# poly_coords = [[1,0], [2,1], [2,2], [1,2], [0,2], [0,1]]
# poly_coords = [[0,0], [2,1], [1,2], [0,3], [0,2], [0,1]]
# poly_coords = [[0,0], [1,0], [2,1], [1,2], [0,3], [0,2], [0,1]]
# poly_coords = [[0,0], [1,0], [2,0], [2,1], [1,2], [0,2], [0,1]]
# poly_coords = [[0,0], [1,0], [2,0], [1,2], [0,4], [0,3], [0,2], [0,1]] 
# poly_coords = [[0,0], [1,0], [2,0], [2,1], [1,2], [0,3], [0,2], [0,1]]
# poly_coords = [[0,0], [1,0], [2,0], [2,1], [2,2], [1,2], [0,2], [0,1]]
# poly_coords = [[0,0], [1,0], [2,0], [3,0], [2,1], [1,2], [0,3], [0,2], [0,1]]

triangulations = find_all_triangulations(poly_coords)

print(f"Original Polygon: {poly_coords}\n")
print(f"Total Triangulations: {len(triangulations)}\n")

# for idx, tri in enumerate(triangulations):
#     print(f"Triangulation {idx + 1}:")
#     for j in tri:
#         print(f"\t{j}")