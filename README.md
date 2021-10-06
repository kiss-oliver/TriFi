# TriFi
A distributed, scalable tool to find triangles in large directed networks

## How it works
Consider a directed network with integer node IDs and directed edges stored in a plain text file in the `source,target` format. In any triangle between nodes A, B and C there exists a strict ordering of the IDs. Let's assign A, B and C labels such that the underlying integer IDs satisfy `id(A)<id(B)<id(C)`. To find all triangles (and all triangles only once):

1. Separate all edges (u,v) in E to two files, one containing N edges where `u<v` and the other with M edges where `v<u`.
2. Parallel merge sort both files.
3. Iterate over the edges in `u<v` parallelly. For each edge (x,y):
 1. Binary search for neighbors of y in `u<v`.
 2. For each neighbor z binary search neighbors in `v<u`. If x in neighbors we have a triangle.

- Separating is O(N+M).
- Merge sort is O(N * log N) and O(M * log M) at worst.
- The nested binary search will be O(N^2/|V| * log N * log M).
- Parallelism is obvious.
- Depending on whether `N<M` or `M<N` the inverse of the algorithm can be run to reduce complexity of the nested binary search.
