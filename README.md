Polytopes, Triangulations, and Toric Varieties
==============================================

These python scripts are a small part of a project of [Elizabeth Gasparim](https://sites.google.com/view/elizabethgasparim). Some sections are still a work-in-progress.

### Triangulations.
This script computes all the primitive triangulations of a given convex polygon on a 2D lattice. The polygon is described by giving the complete list of the 2D coordinates of its vertices in clockwise direction. The result is a list of triangulations, where each triangulation is a list of triangles of area 1/2 whose union makes the given polygon. Each triangle is described as a list of three pairs of points (the vertices of the triangle).

See the examples given within the script for more details.

<!-- Description of the algorithm. -->

### Defining Equations.
Each convex polygon on a 2D lattice corresponds to a toric variety. The defining equations of this variety can be obtained from the given polygon. The polygon is described by giving the complete list of the 2D coordinates of its vertices in clockwise direction. The result is a list of polynomial equations that define the variety corresponding to the polygon.

See the examples given within the script for more details.

<!-- Description of the algorithm. -->

---

### Usage.
At present these scripts only rely on `numpy`.

Both of the python scripts include a demonstration of usage with particular examples. The user can modify this section to make computations for specific polygons. Because of the simplicity of the scripts, it is easy to modify the output formats as needed (e.g. to visualise the polygons and their triangulations using `matplotlib`).

To get started, install the dependencies listed in [`requirements.txt`](https://github.com/rashidtalha/polytope-triangulations/blob/main/requirements.txt) (these are most likely already present on your system). Then run [`triangulations.py`](https://github.com/rashidtalha/polytope-triangulations/blob/main/triangulations.py) and/or [`toric_equations.py`](https://github.com/rashidtalha/polytope-triangulations/blob/main/toric_equations.py) in the terminal.

```bash
python3 triangulations.py
```

```bash
python3 toric_equations.py
```
