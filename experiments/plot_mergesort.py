import altair as alt
import numpy as np
import pandas as pd

stats = open('sort_times.txt','r').read()
statslist = stats.split('\n')
statsdicts = []
for i in range(5000):
    statsdicts.append({'n':statslist[2*i].split('_')[0].split('n')[1],'d':statslist[2*i].split('_')[1].split('d')[1],'s':statslist[2*i].split('_')[2].split('s')[1].split('.')[0],'time':statslist[2*i+1]})

df = pd.DataFrame(statsdicts)
df['log time'] = np.log2(df.time.astype(int))
df['log n'] = df['n'].astype(int).apply(np.log2)
line = alt.Chart(df).mark_line().encode(x='log n',y='mean(log time)', color='d')
band = alt.Chart(df).mark_errorband(extent='ci').encode(x='log n',y=alt.Y('log time', title='Log Runtime'), color='d')
full = band+line
full.save('mergesort.png', scale_factor=10.0)

