from windrose import WindroseAxes
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd
import pkg_resources.py2_warn

'''
    v02 of wave_rose_raw.py 
    plot data from a hindcast spreadsheet output (freq,Hs,dir)
'''

# Create wind speed and direction variables

data = pd.read_csv('wave_dat.csv')

df = pd.DataFrame(data)
wf = np.array(df['freq'])
wh = np.array(df['Hs'])
wd = np.array(df['dir'])


# Pre-process data
wf = wf*100

ht_arr = np.array([])
dir_arr = np.array([])

for i in range(len(wf)):
    ht_arr = np.append(ht_arr, np.ones(int(wf[i]))*wh[i])
    dir_arr = np.append(dir_arr, np.ones(int(wf[i]))*wd[i])

# zero = list()

# for i in range(len(ht_arr)):
#     if ht_arr[i] == 0.0:
#         zero.append(i)

# ht_arr2 = np.delete(ht_arr, zero, None)
# dir_arr2 = np.delete(dir_arr, zero, None)

# def set_legend(ax):
#     l = ax.legend(axespad=-0.10)
#     plt.setp(l.get_texts(), fontsize=8)

# Plotting 
ax = WindroseAxes.from_ax()
ax.bar(dir_arr, ht_arr, normed=True, opening=0.8, edgecolor='white', bins=np.arange(0.0,5,1))
ax.set_legend()

plt.savefig("waveRose_noCalm.png")

ax = WindroseAxes.from_ax()
ax.bar(dir_arr, ht_arr, normed=True, opening=0.8, edgecolor='white', bins=np.arange(0.01,5,1))
ax.set_legend()

plt.savefig("waveRose.png")
