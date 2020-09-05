'''
	U and V velocity plotter in python code
    ver 01 - basic horizontal plotting
    ver 02 - basic vertical plottig (uv_plot_v02 and stick_plot_v02)

    add if else that checks if angles are near 90 and 270 (from azimuth), plot should be switched to vertical
            note: must edit stick_plot not this code... to swith t with u and v
'''

import matplotlib.pyplot as plt
import numpy as np
import csv

#ask for user input of filename
#search how to input string and read
f = open('uv30.csv','rt')
reader = csv.reader(f)
headers = next(reader,None)
column = {}
for h in headers:
	column[h] = []
for row in reader:
	for h, v in zip(headers, row):
		column[h].append(v)
u = np.zeros(len(column['u']))
v = np.zeros(len(column['u'])) # can optimize like d
d = np.array([i for i in column['Date']])
for i in range(len(column['u'])):
	u[i] = column['u'][i]
	v[i] = column['v'][i]

from stick_plot import stick_plot
from datetime import datetime, timedelta

start = datetime(2018,1,1,0,0,0)
time = [start + timedelta(hours=n/2) for n in range(len(u))]
#fix date - it has to ask for user input for the start time, 
#or take it from the file

fig, ax = plt.subplots(figsize=(11, 2))

q = stick_plot(time, u, v, ax=ax, width=0.0005, color='green')
ref = 0.1
qk = plt.quiverkey(q, 0.1, 0.7, ref, "%s m/s" % ref, \
                  labelpos='N', coordinates='axes')
_ = plt.xticks(rotation = 70)

#ax.minor_ticks_on()
major_ticks = np.arange(-0.1, 0.15, 0.05)
#minor_ticks = np.arange(0, 2, 0.1)
ax.set_yticks(major_ticks)
#ax.set_xticks(minor_ticks, minor = True)
#ax.set_yticks(major_ticks)
#ax.set_yticks(minor_ticks, minor = True)

ax.grid(which = 'both')

plt.show()
plt.savefig('uv30.png')
#fix size of plot (check stick plot code)