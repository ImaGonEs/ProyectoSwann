#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Utils
import dweepy
import random
import time
import pyttsx3
speaker = pyttsx3.init()
import requests
import json

#Nuestros modulos

from TempGeoMod.TemperatureandGeoModule import getTemperature_Humidity, getLocation
from UltrasonicWaterMod.ultrasonic_distance import getDistance
from UltrasonicWaterMod.Water import getDisp
from GasBuzzerMotionMod.buzzer_player import playSong, buzzS
from GasBuzzerMotionMod.gas import getGasValue
from GasBuzzerMotionMod.motion import getMotion


# In[ ]:





# In[5]:


def showsmt(lat, lon):
    api_key = "478b53fcd3d9654fee664923e3a2ed82"
    url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    return data['weather'][0]['description']


# In[4]:


tempsum = 0.0
humsum = 0.0
c =0
dis = 0
while True:
    
    temphum = getTemperature_Humidity()
    loc = getLocation()
    tempsum += float(temphum[0])
    humsum += float(temphum[1])
    c +=1
    
    
    distan = getDistance() 
    water = getDisp()
    gas = getGasValue(0)
    smt = showsmt(loc['lat'], loc['lon'])
    
    
    print(smt)
    print(temphum[0])
    print(temphum[1])
    print(loc['lat'])
    print(loc['lon'])
    print(dis)
    print(distan)
    print(gas)
    
    
    
    
    if(distan > 40.0 and gas > 20 and float(temphum[0]) > 20.0 and float(temphum[1]) > 20.0):
        dis = 1
       
    else:
        dis = 0
    
    if (dis==1):
        speaker.say("Shooting!")
        speaker.runAndWait()
        #playSong(1)
        buzzS()
        water.on()
        time.sleep(0.5)
        water.off()
        
    
    dweepy.dweet_for('swann_dash', {'smt': smt, 'temp': float(temphum[0]), 'hum': float(temphum[1]), 'lat': loc['lat'],
                                    'log': loc['lon'], 'disp': dis, 'gas': gas, 'distan': distan, 'tempav': round(float(tempsum/c),1), 'humav': round(float(humsum/c))})
    speaker.say("Data uploaded!")
    speaker.runAndWait()
    time.sleep(1)


# In[17]:





# In[19]:





# In[13]:





# In[9]:





# In[19]:





# In[7]:





# In[3]:





# In[4]:





# In[ ]:




