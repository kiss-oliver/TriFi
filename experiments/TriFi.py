from tqdm import tqdm
from multiprocessing import Pool

sorted_edgelist_source = '../../sorted.csv'
vertex_source = '../../vertex.csv'
triangles = '../../triangles.csv'
cores = 50

from tqdm import tqdm
from multiprocessing import Pool

class neighbor_lookup:
    def __init__(self, filename):
        self.f = open(filename, 'r')
        self.f.seek(0,2)
        self.length = self.f.tell()
    def find_neighbors(self, string):
        low = 0
        high = self.length
        while low < high:
            mid = (low+high)//2
            p = mid
            while p >= 0:
                self.f.seek(p)
                if self.f.read(1) == '\n': break
                p -= 1
            if p < 0: self.f.seek(0)
            line = self.f.readline()
            if line < string:
                low = mid+1
            else:
                high = mid
        p = low
        while p >= 0:
            self.f.seek(p)
            if self.f.read(1) == '\n': break
            p -= 1
        if p < 0: self.f.seek(0)
        result = []
        while True:
            line = self.f.readline()
            if not line or not line.startswith(string): break
            if line[-1:] == '\n': line = line[:-1]
            result.append(line[len(string):])
        return result

def check_triangle(u):
    u = u.replace('\n','')
    tri = []
    W = edgelist.find_neighbors(u+',')
    for z in W:
        for x in edgelist.find_neighbors(z+","):
            if x in W:
                tri.append('{},{},{}\n'.format(u, x, z))
    return tri

def init_worker(se):
    global edgelist
    edgelist = neighbor_lookup(se)

with open(triangles,'w') as output:
    with open(vertex_source, 'r') as input:
        with Pool(cores, initializer=init_worker, initargs=(sorted_edgelist_source,)) as client:
            for tri in tqdm(client.imap_unordered(check_triangle, input)):
                for x in tri:
                    output.write(x)
