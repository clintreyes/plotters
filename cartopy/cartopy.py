# -*- coding: utf-8 -*-
"""
Created on Tue May  5 14:45:17 2020

Plot GIS trial using cartopy
look how to import shapefiles
and modify the plot to your liking

@author: coastal
"""


import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np

proj = ccrs.Mercator()

plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)
#ax.set_extent((5.0, 25.0, 100.0, 130.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')


lat = [6.89015, 19.344341]
long = [116.208216, 128.621277]
ax.plot(long, lat, 'r-', transform=ccrs.Geodetic(), label='test')
#plt.legend(loc="upper left")
plt.savefig("map.pdf")