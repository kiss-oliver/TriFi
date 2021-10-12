# TriFi
A distributed, scalable tool to find triangles in large networks

## Usage

Make sure that your python environment contains the packages listed in `requirements.txt`. Then run

```
. run.sh edgelist.csv
```

Where `edgelist.csv` is a headerless comma separated edgelist. To modify number of cores used edit `TriFi.py`. The current implementation relies on `sort`, `cut` and `uniq` from  GNU coreutils.

## How it works
Consider a network with alphanumeric node IDs and edges stored in a plain text file in the `source,target` format. In any triangle between nodes A, B and C there exists a strict ordering of the IDs. Let's assign A, B and C labels such that the underlying integer IDs satisfy `id(A)<id(B)<id(C)`. To find all triangles (and all triangles only once):

1. Rearrange edgelist such that target id is larger than source id. This way all triangles will be trust triangles with lowest id as source and largest id as sink.
2. Parallel merge sort and deduplicate E.
3. Create a list of all unique source node ids.
4. Iterate over the unique source node ids. For each node u:
 1. Binary search for neighbors of u. Call them W.
 2. For each neighbor w in W binary search neighbors in E. Call them Z.
 3. For z in Z if z in W we have an u,w,z triangle.

- Merge sort is quasi-linear O(|E| * log |E|) at worst.
- Separating is linear O(|E|)
- The nested binary search will be approximately O(|E| * log |E| * log |E|).
- Parallelism is obvious.
- If node ids are integers, interpolation search is also potentially possible. That can reduce complexity to O(|E| * log log |E| * log log |E|)
