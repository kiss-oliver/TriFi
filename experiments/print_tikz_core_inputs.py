import pandas as pd
import numpy as np

files = ['search_times.txt']
dfs = []
for file in files:
    stats = open(file,'r').read()
    statslist = stats.split('\n')
    statsdicts = []
    for i in range(len(statslist)//2):
        statsdicts.append({'n':statslist[2*i].split('_')[0].split('n')[1],'d':statslist[2*i].split('_')[1].split('d')[1],'s':statslist[2*i].split('_')[2].split('s')[1].split('.')[0],'time':statslist[2*i+1]})
    df = pd.DataFrame(statsdicts)
    df['log time'] = np.log2(df.time.astype(int))
    df['log n'] = df['n'].astype(int).apply(np.log2)
    dfs.append(df)

cated = pd.concat(dfs)
cated['time'] = cated['time'].astype(int)
cated = cated.reset_index()
fin = cated.groupby(['n','d','s'])['time'].apply(sum).reset_index()
fin['log time'] = np.log2(fin.time.astype(int))
fin['log n'] = fin['n'].astype(int).apply(np.log2)

for i, g in fin.groupby(['d','log n'])['log time'].apply(np.mean).reset_index().groupby('d'):
    print(i)
    for z in [x for x in zip(g['log n'].tolist(),g['log time'].tolist())]:
        print(z)
