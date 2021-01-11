#!/usr/bin/env python
# coding: utf-8

# In[19]:


import Adafruit_DHT as ad
#from grove_rgb_lcd import *

import requests as re
import json
import time
from datetime import datetime


import pyttsx3
speaker = pyttsx3.init()


# In[20]:


def getTemperature_Humidity():
    #setRGB(0,0,0)
    sensor = ad.DHT11
    gpio=12

    humidity, temp = ad.read_retry(sensor, gpio)

    hey = 'Temp={0:0.1f}*C Hum={1:0.1f}%'.format(temp, humidity)
    print(hey)
    ret = []
    
    ret.append('{0:0.1f}'.format(temp))
    ret.append('{0:0.1f}'.format(humidity))
    if humidity is not None and temp is not None:
        #print('Temp={0:0.1f}*C Hum={1:0.1f}%'.format(temp, humidity))
        #setText('Temp={0:0.1f}*C Hum={1:0.1f}%'.format(temp, humidity))
        #setRGB(128, 128, 128)
        return ret
    else:
        print("Pues no ha skereado")


# In[21]:


def getLocation():
    url = 'https://extreme-ip-lookup.com/json/'
    r = re.get(url)
    locData = json.loads(r.content.decode())
    
    #print("Latitud: "+locData['lat']+ " Longitud: "+ locData["lon"])
    return locData


# In[17]:


"""r = getTemperature_Humidity()
print(float(r[0]))"""


# In[6]:


"""getLocation()"""


# In[7]:


"""while True:
    temphum = getTemperature_Humidity()
    locData = getLocation()
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(now)
    print(temphum)
    print("Latitud: "+locData['lat']+ " Longitud: "+ locData['lon'])
    speaker.say(str("Latitud: "+locData['lat']+ " Longitud: "+ locData['lon']))
    speaker.runAndWait()
    time.sleep(1)"""


# In[ ]:




