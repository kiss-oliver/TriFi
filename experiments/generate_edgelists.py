import networkx as nx
from tqdm import tqdm

N = [2**(x+5) for x in range(13)]
D = [2**(x+2) for x in range(5)]

S = range(100)

for n in N:
    for d in tqdm(D):
        for seed in S:
            m=n*d
            G = nx.gnm_random_graph(n, m, seed=seed, directed=True)
            nx.write_edgelist(G, "../edgelists/n{}_d{}_s{}.csv".format(n,d,seed), data=False, delimiter=',')
