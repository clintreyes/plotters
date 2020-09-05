'''
	U and V velocity plotter in python code
'''

import matplotlib.pyplot as plt
import numpy as np
import csv

x = np.arange(100, 110, 0.1)
u, v = np.sin(x), np.cos(x)

from stick_plot import stick_plot
from datetime import datetime, timedelta

start = datetime.now()
time = [start + timedelta(days=n) for n in range(len(u))]

fig, ax = plt.subplots(figsize=(11, 2.75))

q = stick_plot(time, u, v, ax=ax, width=0.002, color='green')
ref = 0.1
qk = plt.quiverkey(q, 0.1, 0.85, ref, "%s m/s" % ref, \
                  labelpos='N', coordinates='axes')
_ = plt.xticks(rotation = 70)
plt.show()