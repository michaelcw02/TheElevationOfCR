import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd

fp = "data/limite_cantonal/limite_cantonal.shp"
data = gpd.read_file(fp)

#data.crs = {'init': 'epsg:5367'}
data = data.to_crs({'init': 'epsg:4326'})

#fig, ax = plt.subplots(figsize=(15, 15))
#data.plot(ax=ax)


data.plot()

plt.show()