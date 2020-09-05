from windrose import WindroseAxes
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd

'''
    v02 try this with offshore bc data
    make an alternative for non-raw data
'''

# Create wind speed and direction variables

sd = pd.read_csv('sd.csv')

df = pd.DataFrame(sd)
ws = np.array(df['SPEED'])
wd = np.array(df['DIRECTION'])

ax = WindroseAxes.from_ax()
ax.bar(wd, ws, normed=True, opening=0.8, edgecolor='white')
ax.set_legend()

plt.show()