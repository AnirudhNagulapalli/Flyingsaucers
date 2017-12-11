'''
This file is used to visualise the pickup and dropoff locations
on hourly basis in a map
Reading the data from the database
@author: Anirudh Nagulapalli, Kavya Reddy Vemula
'''

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import MySQLdb

#Connecting to the Flyingsaucers database 
mysql_cn= MySQLdb.connect(host='127.0.0.1', 
                port=3306, user='root', passwd='letmein', 
                db='flyingsaucers')

cur = mysql_cn.cursor()

cur.execute("SELECT * FROM train")

numrows = cur.rowcount
plong = list()
plat = list()
dlong = list()
dlat = list()

#To display the number of rows
print "Total number of trips : " +str(numrows)

#To get and display one row at a time
for x in range(0, numrows):
  row = cur.fetchone()
  
  #To store the pickup longitudes
  plong.append(float(row[5]))

  #To store the pickup latitudes
  plat.append(float(row[6]))
  
  #To store the dropoff longitudes
  dlong.append(float(row[7]))
  
  #To store the dropoff latitudes
  dlat.append(float(row[8]))

hourlatitudes = []
hourlongitudes = []
latsArray = []
longsArray = []
temp = []

#Iterating through each hour from 0 to 23
for hours in range(0, 24):
	cur.execute("SELECT pickup_latitude, pickup_longitude FROM train WHERE HOUR(pickup_datetime)="+str(hours))
	numrows = cur.rowcount
	for x in range(0, numrows):
		temp = cur.fetchone()

		#Storing the latitudes for each hour in a list
		hourlatitudes.append(float(temp[0]))

		#Storing the longitudes for each hour in a list
		hourlongitudes.append(float(temp[1]))

	latsArray.append(hourlatitudes)
	longsArray.append(hourlongitudes)

	#Emptying the list after each hour
	hourlatitudes = []
	hourlongitudes = []

for x in range(0,24):
	#Number of pickups for the hour
	print "Number of trips for hour " +str(x) +" : " +str(len(latsArray[x]))

mysql_cn.close()

#Creating a basemap 
map = Basemap(projection='merc', lat_0 = 40.730610, lon_0 = -73.935242,
	    resolution = 'h', area_thresh = 0.1,
	    llcrnrlon=-74.025742, llcrnrlat=40.699922,
	    urcrnrlon=-73.903519, urcrnrlat=40.880315)

for x in range(0,24):	

	#Converting latitude and longitude to map projection coordinates
	plons, plats = map(longsArray[x], latsArray[x])
	
	#Drawing the outlines of the map
	map.drawcoastlines()
	map.drawcountries()
	map.fillcontinents(color = 'green', lake_color = 'blue')
	map.drawmapboundary(fill_color='aqua')
	map.drawrivers(linewidth=0.5, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
	map.drawstates()
	map.drawparallels(np.arange(-40,61.,2.))
	map.drawmeridians(np.arange(-20.,21.,2.))

	#Classifying the traffic based on the number of trips with different colors
	
	#Cyan indicates minimum traffic
	if len(latsArray[x])<15000:
		map.plot(plons, plats, 'o', color='#00ffff', markersize=5)
	
	elif len(latsArray[x])>15000 and len(latsArray[x])<20000:
		map.plot(plons, plats, 'o', color='#6600ff', markersize=5)
	
	elif len(latsArray[x])>15000 and len(latsArray[x])<30000:
		map.plot(plons, plats, 'o', color='#000066', markersize=5)
	
	elif len(latsArray[x])>15000 and len(latsArray[x])<40000:
		map.plot(plons, plats, 'o', color='#ff9900', markersize=5)
	
	elif len(latsArray[x])>15000 and len(latsArray[x])<50000:
		map.plot(plons, plats, 'o', color='#ff3300', markersize=5)
	
	elif len(latsArray[x])>15000 and len(latsArray[x])<60000:
		map.plot(plons, plats, 'o', color='#ff0000', markersize=5)
	
	#Maroon indicates maximum traffic
	elif len(latsArray[x])>60000:
		map.plot(plons, plats, 'o', color='#800000', markersize=5)

	plt.title("For H = %i hour" %x)

	#Prints the number of trips during that hour onto the map
	plt.annotate(len(latsArray[x]), xy=(0.9,-0.1), xycoords="axes fraction")

	plt.show()

