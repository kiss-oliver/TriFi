import pandas as pd
import numpy as np

files = ['mergesort_times.txt', 'search_times.txt', 'separate_times.txt', 'vertex_times.txt']
dfs = []
for file in files:
    stats = open(file,'r').read()
    statslist = stats.split('\n')
    statsdicts = []
    for i in range(len(statslist)//2):
        statsdicts.append({'c':statslist[2*i].split('_')[0].split('c')[1],'n':statslist[2*i].split('_')[1].split('n')[1],'d':statslist[2*i].split('_')[2].split('d')[1],'s':statslist[2*i].split('_')[3].split('s')[1].split('.')[0],'time':statslist[2*i+1]})
    df = pd.DataFrame(statsdicts)
    df['log time'] = np.log2(df.time.astype(int))
    df['log n'] = df['n'].astype(int).apply(np.log2)
    dfs.append(df)

cated = pd.concat(dfs)
cated['time'] = cated['time'].astype(int)
cated = cated.reset_index()
fin = cated.groupby(['c','n','d','s'])['time'].apply(sum).reset_index()
fin['log time'] = np.log2(fin.time.astype(int))
fin['log n'] = fin['n'].astype(int).apply(np.log2)

for i, g in fin.groupby(['c','log n'])['log time'].apply(np.mean).reset_index().groupby('log n'):
    print(i)
    for z in [x for x in zip(g['c'].astype(int).tolist(),g['log time'].tolist())]:
        print(z)
