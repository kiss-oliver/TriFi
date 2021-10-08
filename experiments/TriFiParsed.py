from tqdm import tqdm
from multiprocessing import Pool
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()


sorted_edgelist_source = args.filename
ularger_source = '../../ularger.csv'
vlarger = '../../vlarger.csv'
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

def check_triangle(edge):
    tri = []
    u, v = edge.replace('\n','').split(',')
    X = ularger.find_neighbors(v+',')
    for z in X:
        if u in edgelist.find_neighbors(z+","):
            tri.append('{},{},{}\n'.format(u, v, z))
    return tri

def init_worker(se,ul):
    global edgelist
    global ularger
    edgelist = neighbor_lookup(se)
    ularger = neighbor_lookup(ul)

with open(triangles,'w') as output:
    with open(vlarger, 'r') as input:
        with Pool(cores, initializer=init_worker, initargs=(sorted_edgelist_source,ularger_source,)) as client:
            for tri in tqdm(client.imap_unordered(check_triangle, input)):
                for x in tri:
                    output.write(x)
