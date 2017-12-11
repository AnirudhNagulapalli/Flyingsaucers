'''
This file is used to visualise the pickup and dropoff locations 
in the Manhattan region. 
Reading the data from a csv file
@author: Anirudh Nagulapalli, Kavya Reddy Vemula
'''

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#Reading the data from the csv file
buildingdf = pd.read_csv('/Users/Anirudh/4th Semester/data/traffic/train100rows.csv')

#Storing the pickup latitude and longitude values
plat = buildingdf['pickup_latitude'].values
plong = buildingdf['pickup_longitude'].values

#Storing the dropoff latitude and longitude values
dlat = buildingdf['dropoff_latitude'].values
dlong = buildingdf['dropoff_longitude'].values

#Using subplot to show two maps in a single window
plt.subplot(1, 2, 1)

#Creating a basemap 
map = Basemap(width=120000000, height=90000000, projection='merc', lat_0 = 40.730610, lon_0 = -73.935242,
    resolution = 'h', area_thresh = 0.1,
    llcrnrlon=-74.025742, llcrnrlat=40.699922,
    urcrnrlon=-73.903519, urcrnrlat=40.880315)

#Converting pickup latitudes and longitudes to map projection coordinates
plons, plats = map(plong, plat)

#Drawing the outlines of the map
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color = 'green', lake_color = 'blue')
map.drawmapboundary(fill_color='aqua')
map.drawrivers(linewidth=0.5, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
map.drawstates()
map.drawparallels(np.arange(-40,61.,2.))
map.drawmeridians(np.arange(-20.,21.,2.))

#Plotting the pickup locations in blue 
map.plot(plons, plats, 'bo', markersize=5)
plt.title("Flyingsaucer's pickup projection")

plt.subplot(1, 2, 2)
#Creating a basemap 
map = Basemap(width=120000000, height=90000000, projection='merc', lat_0 = 40.730610, lon_0 = -73.935242,
    resolution = 'h', area_thresh = 0.1,
    llcrnrlon=-74.025742, llcrnrlat=40.699922,
    urcrnrlon=-73.903519, urcrnrlat=40.880315)
#Converting dropoff latitudes and longitudes to map projection coordinates
dlons, dlats = map(dlong, dlat)

#Drawing the outlines of the map
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color = 'green', lake_color = 'blue')
map.drawmapboundary(fill_color='aqua')
map.drawrivers(linewidth=0.5, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
map.drawstates()
map.drawparallels(np.arange(-40,61.,2.))
map.drawmeridians(np.arange(-20.,21.,2.))

#Plotting the dropoff locations in red
map.plot(dlons, dlats, 'r+', markersize=5)
plt.title("Flyingsaucer's dropoff projection")

plt.show()