Polytopes, Triangulations, and Toric Varieties
==============================================

These python scripts are a small part of a project of [Elizabeth Gasparim](https://sites.google.com/view/elizabethgasparim). Some sections are still a work-in-progress.

---

### Universal Quilts.

**Polygon 7:** (64 triangulations) Two different universal quilts
<br><img src="https://github.com/rashidtalha/polytope-triangulations/blob/main/quilts/quilt_7a.png">
<br><img src="https://github.com/rashidtalha/polytope-triangulations/blob/main/quilts/quilt_7b.png">

**Polygon 13:** (64 triangulations)
<br><img src="https://github.com/rashidtalha/polytope-triangulations/blob/main/quilts/quilt_13.png">

**Polygon 15:** (64 triangulations)
<br><img src="https://github.com/rashidtalha/polytope-triangulations/blob/main/quilts/quilt_15.png">

**Polygon 16:** (79 triangulations)
<br><img src="https://github.com/rashidtalha/polytope-triangulations/blob/main/quilts/quilt_16.png">

---

### Additional Section about Games.

Under construction ...

---

### Algorithm.
This script computes all the primitive triangulations of a given convex polygon on a 2D lattice. The polygon is described by giving the complete list of the 2D coordinates of its vertices in clockwise direction. The result is a list of triangulations, where each triangulation is a list of triangles of area 1/2 whose union makes the given polygon. Each triangle is described as a list of three pairs of points (the vertices of the triangle).

See the examples given within the script for more details.

<!-- Description of the algorithm. -->

---

### Usage.
At present these scripts only rely on `numpy`.

The python scripts include a demonstration of usage with particular examples. The user can modify that section of the script to make computations for specific polygons. Because of the simplicity of the scripts, it is easy to modify the output formats as needed (e.g. to visualise the polygons and their triangulations using `matplotlib`).

To get started, install the dependencies listed in [`requirements.txt`](https://github.com/rashidtalha/polytope-triangulations/blob/main/requirements.txt) (these are most likely already present on your system). Then run [`triangulations.py`](https://github.com/rashidtalha/polytope-triangulations/blob/main/triangulations.py) in the terminal.

For easy visualisation use the [`plot_triangulations.py`](https://github.com/rashidtalha/polytope-triangulations/blob/main/plot_triangulations.py) or [`plot_edges.py`](https://github.com/rashidtalha/polytope-triangulations/blob/main/plot_edges.py) script.

```bash
python3 triangulations.py
python3 plot_triangulations.py
python3 plot_edges.py
```
