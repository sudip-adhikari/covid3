# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:16:06 2020

@author: Admin
The recently updated map of Nepal including the Byas Gaupalika of the Kalapani area is used here.
"""

import pandas as pd
import geopandas as gpd

#Loading Map of nepal with district divison
map_district = gpd.read_file(r'H:\projects\gis\npl_admbnda_nd_20190430_shp\npl_admbnda_districts_nd_20190430.shp')
map_district = map_district[['DIST_EN','geometry']]

#Loading map of Nepal with local units
map_nep = gpd.read_file(r'H:\mausam\python  ex\covid-19\nepal administ\Local Unit\local_unit.shp')
map_nep = map_nep[['Province','DISTRICT','GaPa_NaPa','geometry']]

#Extracting the geometry of Byas  Gaupalika in Darchulla district
count = 0
for district, local in zip(map_nep['DISTRICT'],map_nep['GaPa_NaPa']):
    if district == 'DARCHULA' and local == 'Byas':       
        byas_geo = map_nep['geometry'][count]
        #print(byas_geo)
    count += 1

#Appending the new Byas Gauplika 
new_map = map_district.copy()
new_map.loc[77] = ['Darchula',byas_geo]

new_map.plot(figsize = (20,9))

#map_district.plot()
