import numpy as np
from fractions import Fraction

def _texify_matrix(A):
    res = " \\\\ ".join([" & ".join(map(str, row)) for row in A])
    return f"\\begin{{pmatrix}} {res} \\end{{pmatrix}}"

def _rref(matrix):
    M = np.array([[Fraction(int(x)) for x in row] for row in matrix], dtype=object)
    nrows, ncols = M.shape
    pivot_cols = []
    
    r = 0
    for c in range(ncols):
        nz = np.flatnonzero(M[r:, c])
        if not nz.size: continue

        pivot_row = r + nz[0]
        M[[r, pivot_row]] = M[[pivot_row, r]]
        pivot_cols.append(c)

        M[r] = M[r] / M[r, c]

        mask = np.arange(nrows) != r
        M[mask] = M[mask] - M[mask, c:c+1] * M[r]

        r += 1

    return M, pivot_cols

def nullspace(M):
    _, ncols = M.shape

    rref_M, pivot_cols = _rref(M)
    free_cols = [c for c in range(ncols) if c not in set(pivot_cols)]

    basis = []
    for fc in free_cols:
        vec = np.array([Fraction(0)] * ncols, dtype=object)
        vec[fc] = Fraction(1)
        for row_idx, pc in enumerate(pivot_cols):
            vec[pc] = -rref_M[row_idx, fc]

        denoms = np.array([v.denominator for v in vec], dtype=np.int64)
        lcm_den = int(np.lcm.reduce(denoms))
        int_vec = np.array([v.numerator * (lcm_den // v.denominator) for v in vec], dtype=np.int64)

        g = int(np.gcd.reduce(np.abs(int_vec[int_vec != 0])))
        int_vec //= g

        basis.append(int_vec.tolist())

    return basis

def compute_equations(pts):
    A = np.array(pts, dtype=np.int64)
    M = np.hstack([A, np.ones((len(A), 1), dtype=np.int64)]).T
    N = np.cross(M, np.roll(M, -1, axis=1), axis=0)

    sf = np.gcd.reduce(N, axis=0)
    sf[sf == 0] = 1
    N = N // sf

    ker_basis = nullspace(N)

    eqs = []
    for bv in ker_basis:
        pos_part = ""
        neg_part = ""
        for idx in range(len(bv)):
            if bv[idx] > 0:
                pos_part += f" x_{{{idx}}}"
                if bv[idx] != 1: pos_part += f"^{{{bv[idx]}}}"
            elif bv[idx] < 0:
                neg_part += f" x_{{{idx}}}"
                if bv[idx] != -1: neg_part += f"^{{{-bv[idx]}}}"

        res = f"{pos_part.strip()} - {neg_part.strip()} = 0"
        eqs.append(res)
            
    print(f"Matrix of vertices:\n{M}")
    print(_texify_matrix(M))

    print(f"\nMatrix of scaled normals:\n{N}")
    print(_texify_matrix(N))
    
    print("\nDefining equation(s):")
    if len(eqs) == 0:
        print("None")
    else:
        for eq in eqs:
            print(eq)

#########################

if __name__ == '__main__':
    examples = [
    #     [[0,0], [4,0], [3,1], [0,1]],
    #     [[0,0], [4,0], [2,1], [0,1]],
        [[-1,-1], [1,0], [0,1], [0,0]],
    ]
    # examples = [ [[1,0], [0,1], [-1,-2], [0,0]] ]
    for j in examples:
        compute_equations(j)
        print(f"\n{'-'*50}\n")
