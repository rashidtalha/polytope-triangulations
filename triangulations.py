from math import gcd, atan2

def complete_boundary(verts):
    N = len(verts)
    bucket = []
    for j in range(N):
        dx = verts[(j+1) % N][0] - verts[j][0]
        dy = verts[(j+1) % N][1] - verts[j][1]
        g = gcd(dx, dy)

        for k in range(g):
            bucket.append([verts[j][0] + (k * (dx // g)), verts[j][1] + (k * (dy // g))])
    return bucket

def get_all_triangulations(V, output="triangles"):
    V = complete_boundary(V)
    B = len(V)
    V_set = {tuple(v) for v in V}
    min_x = min(v[0] for v in V)
    max_x = max(v[0] for v in V)
    min_y = min(v[1] for v in V)
    max_y = max(v[1] for v in V)
    
    interior = []
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) in V_set:
                continue
            inside = True
            for i in range(B):
                v1 = V[i]
                v2 = V[(i + 1) % B]
                cross = (v2[0] - v1[0]) * (y - v1[1]) - (v2[1] - v1[1]) * (x - v1[0])
                if cross <= 0:
                    inside = False
                    break
            if inside:
                interior.append([x, y])
    
    pts = V + interior
    N = len(pts)
    
    boundary_edges = set()
    for i in range(B):
        j = (i + 1) % B
        boundary_edges.add((i, j) if i < j else (j, i))
    
    cand = []
    for i in range(N):
        for j in range(i + 1, N):
            if (i, j) in boundary_edges:
                continue
            dx = pts[j][0] - pts[i][0]
            dy = pts[j][1] - pts[i][1]
            if gcd(abs(dx), abs(dy)) == 1:
                cand.append((i, j))
    
    M = len(cand)
    K = 3 * N - 2 * B - 3
    if K < 0 or K > M:
        return []
    
    # Compute the crossing matrix
    def orient(p, q, r):
        return (q[0]-p[0])*(r[1]-p[1]) - (q[1]-p[1])*(r[0]-p[0])
    
    def intersect(e1, e2):
        a, b = e1
        c, d = e2
        if a == c or a == d or b == c or b == d:
            return False
        o1 = orient(pts[a], pts[b], pts[c])
        o2 = orient(pts[a], pts[b], pts[d])
        o3 = orient(pts[c], pts[d], pts[a])
        o4 = orient(pts[c], pts[d], pts[b])
        if o1 == 0 or o2 == 0 or o3 == 0 or o4 == 0:
            return False
        return (o1 > 0) != (o2 > 0) and (o3 > 0) != (o4 > 0)
    
    cross = [[False] * M for _ in range(M)]
    for a in range(M):
        for b in range(a + 1, M):
            if intersect(cand[a], cand[b]):
                cross[a][b] = cross[b][a] = True
    
    def extract_triangles(selected):
        # Adjacency list
        adj = [[] for _ in range(N)]
        for i in range(B):
            j = (i + 1) % B
            adj[i].append(j)
            adj[j].append(i)
        for idx in selected:
            i, j = cand[idx]
            adj[i].append(j)
            adj[j].append(i)
        
        # Sorting
        for u in range(N):
            def angle_key(v):
                dx = pts[v][0] - pts[u][0]
                dy = pts[v][1] - pts[u][1]
                return atan2(dy, dx)
            adj[u].sort(key=angle_key)
        
        visited = [[False] * N for _ in range(N)]
        triangles = []
        for u in range(N):
            for v in adj[u]:
                if not visited[u][v]:
                    face = []
                    cur_u, cur_v = u, v
                    while not visited[cur_u][cur_v]:
                        visited[cur_u][cur_v] = True
                        face.append(cur_u)
                        nbrs = adj[cur_v]
                        idx = nbrs.index(cur_u)
                        next_v = nbrs[(idx - 1) % len(nbrs)]
                        cur_u, cur_v = cur_v, next_v
                    
                    if len(face) == 3:
                        area = 0
                        for i in range(3):
                            x1, y1 = pts[face[i]]
                            x2, y2 = pts[face[(i + 1) % 3]]
                            area += x1 * y2 - x2 * y1
                        if area > 0:
                            tri = tuple(tuple(pts[v]) for v in face)
                            triangles.append(tri)
        return triangles

    # Extract edges (boundary + selected diagonals) for a given selection of diagonals
    def extract_edges(selected):
        edges = []
        # # Add boundary edges (as point coordinates)
        # for (i, j) in boundary_edges:
        #     edges.append((tuple(pts[i]), tuple(pts[j])))
        # Add selected diagonals
        for idx in selected:
            i, j = cand[idx]
            edges.append((tuple(pts[i]), tuple(pts[j])))
        return edges
    
    # DFS for finding valid subsets
    solutions = []
    selected = []
    
    def dfs(start_idx, count):
        if count == K:
            if output == 'triangles':
                solutions.append(extract_triangles(selected))
            else:
                solutions.append(extract_edges(selected)) ####
                # solutions += 1 ####
            return
        if start_idx >= M:
            return
        if count + (M - start_idx) < K:
            return
        
        dfs(start_idx + 1, count)
        
        ok = True
        for s in selected:
            if cross[start_idx][s]:
                ok = False
                break
        if ok:
            selected.append(start_idx)
            dfs(start_idx + 1, count + 1)
            selected.pop()
    
    dfs(0, 0)
    return solutions

#########################

if __name__ == '__main__':
    examples = [
        # [[0,0], [2,1], [1,2]],
        # [[1,0], [2,1], [1,2], [0,1]],
        # [[0,0], [2,1], [1,2], [0,1]],
        # [[0,0], [3,1], [2,2]],
        # [[1,0], [2,1], [2,2], [1,2], [0,1]],
        # [[0,0], [2,1], [1,2], [0,2]],
        # [[0,0], [1,0], [2,1], [2,2], [1,2], [0,1]],
        # [[0,0], [2,0], [2,1], [0,2]],
        # [[1,0], [2,1], [2,2], [0,2], [0,1]],
        # [[0,0], [2,1], [0,3]],
        # [[0,0], [1,0], [2,1], [0,3]],
        # [[0,0], [2,0], [2,1], [1,2], [0,2]],
        # [[0,0], [2,0], [0,4]],
        # [[0,0], [2,0], [2,1], [0,3]],
        [[0,0], [2,0], [2,2], [0,2]],
        # [[0,0], [3,0], [0,3]]
        # [[0,0], [1,0], [1,1], [0,1]],
    ]
    for idx in range(len(examples)):
        res = get_all_triangulations(examples[idx], "edges")
        print(f"Polygon {idx+1:>2} has {len(res):>2} triangulations")

        # with open("poly_16_tri.txt", "w") as f:
        #     f.write(str(res))
        #     f.close()
