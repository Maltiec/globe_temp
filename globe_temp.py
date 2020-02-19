#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:54:34 2020
Getting weather over the globe by coordinates
@author: evgeniy
"""

import pyowm
import time

coord_list=[]
temperature_list=[]
temp_list=[]
longitude = -180
latitude = -90
i=0

while latitude <= 90:
    while longitude<=180:
        temp_list=[latitude,longitude]
        coord_list.append(temp_list)
        temp_list=[]
        longitude = longitude+10
    longitude = -180    
    latitude = latitude + 10
    

owm = pyowm.OWM('03730ab5ecad7256cbf0cd4e4ba95d0e')

temp_list=[]
while i<len(coord_list):
    observation = owm.weather_at_coords(coord_list[i][0],coord_list[i][1])
    w = observation.get_weather()
    temp_list=w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    temperature_list.append(temp_list['temp'])
    time.sleep(1)
    temp_list=[]
    i = i+1
    