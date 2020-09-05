import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import date2num


def stick_plot(time, u, v, **kw):
    width = kw.pop('width', 0.002)
    headwidth = kw.pop('headwidth', 3)
    headlength = kw.pop('headlength', 5)
    headaxislength = kw.pop('headaxislength', 4.5)
    angles = kw.pop('angles', 'uv')
    ax = kw.pop('ax', None)
    
    if angles != 'uv':
        raise AssertionError("Stickplot angles must be 'uv' so that"
                             "if *U*==*V* the angle of the arrow on"
                             "the plot is 45 degrees CCW from the *x*-axis.")

    time, u, v = map(np.asanyarray, (time, u, v))
    if not ax:
        fig, ax = plt.subplots()
    
    q = ax.quiver( [[0]*len(time)], date2num(time), u, v, # varying if else
                  angles='uv', width=width, headwidth=headwidth,
                  headlength=headlength, headaxislength=headaxislength,
                  **kw)

    ax.axes.get_xaxis().set_visible(True)     # varying if else
    ax.yaxis_date()                           # varying if else
    return q

#to optimize for horizontal arrows, change x and y axes
#add if/else for angles near horizontal