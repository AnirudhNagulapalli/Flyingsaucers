'''
This file is used to visualise the pickup and dropoff locations
in a map reading the data from a csv file
@author: Anirudh Nagulapalli, Kavya Reddy Vemula
'''

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Reading the data from a csv file
buildingdf = pd.read_csv('/Users/Anirudh/4th Semester/data/traffic/train.csv')

#Storing the pickup latitude and longitude values
plat = buildingdf['pickup_latitude'].values
plong = buildingdf['pickup_longitude'].values

#Storing the dropoff latitude and longitude values
dlat = buildingdf['dropoff_latitude'].values
dlong = buildingdf['dropoff_longitude'].values

#Creating a basemap 
map = Basemap(projection='merc', lat_0 = 40.730610, lon_0 = -73.935242,
    resolution = 'h', area_thresh = 0.1,
    llcrnrlon=-74.279739, llcrnrlat=40.480744,
    urcrnrlon=-73.664783, urcrnrlat=40.928996)

#Converting latitudes and longitudes to map projection coordinates
plons, plats = map(plong, plat)
dlons, dlats = map(dlong, dlat)

#Drawing the outlines of the map
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color = 'green', lake_color = 'blue')
map.drawmapboundary(fill_color='aqua')
map.drawrivers(linewidth=0.5, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
map.drawstates()
map.drawparallels(np.arange(-40,61.,0.125))
map.drawmeridians(np.arange(0,360,0.5))

#Plotting the pickup locations in blue and dropoff locations in red
map.plot(plons, plats, 'bo', markersize=5)
map.plot(dlons, dlats, 'r+', markersize=5)
plt.title("Flyingsaucer's projection")
plt.show()