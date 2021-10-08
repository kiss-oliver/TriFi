# TriFi
A distributed, scalable tool to find triangles in large directed networks

## How it works
Consider a directed network with integer node IDs and directed edges stored in a plain text file in the `source,target` format. In any triangle between nodes A, B and C there exists a strict ordering of the IDs. Let's assign A, B and C labels such that the underlying integer IDs satisfy `id(A)<id(B)<id(C)`. To find all triangles (and all triangles only once):

1. Parallel merge sort E.
2. Separate all edges (u,v) in E to two files, one containing N edges where `u<v` and the other with M edges where `v<u`.
3. To find Type A triangles iterate over the edges in `u<v` parallelly. For each edge (x,y):
  - Binary search for neighbors of y in `u>v`.
  - For each neighbor z binary search neighbors in E. If x in neighbors we have a triangle.
4. To find Type B triangles iterate over edges (u, v) in E. For each source node u:
  - Collect all target nodes (they are already sorted) to V. Iterate over target nodes v in V from lowest to largest.
  - For each v binary search v in `u<v`. If any neighbor z is in V we have a triangle.

- Merge sort is quasi-linear O(|E| * log |E|) at worst.
- Separating is linear O(|E|)
- The nested binary search will be approximately O(N * d * log M * log |E|) where d is the average out-degree of a node, N is the number of edges where `u<v` and M is the number of edges where `u>v`.
- The intersection search will be approximately O((N+M) * d * log N * log d)
- Parallelism is obvious.
- Since node ids are integers, interpolation search is also potentially possible. That can reduce complexity to O(N * d * log log M * log log |E|)
- Depending on whether `N<M` or `M<N` the inverse of the algorithm can be run to reduce complexity of the nested binary search.
