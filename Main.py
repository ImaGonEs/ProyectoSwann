#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Utils
import dweepy
import random
import time
import pyttsx3
speaker = pyttsx3.init()

#Nuestros modulos

from TempGeoMod.TemperatureandGeoModule import getTemperature_Humidity, getLocation
from UltrasonicWaterMod.ultrasonic_distance import getDistance
from UltrasonicWaterMod.Water import getDisp
from GasBuzzerMotionMod.buzzer_player import playSong
from GasBuzzerMotionMod.gas import getGasValue
from GasBuzzerMotionMod.motion import getMotion


# In[7]:

#playSong(3)



# In[2]:


def showsmt():
    return 'heyhey'
"""def showint():
    return random.randrange(40,45)
def showfloat():
    loc = []
    loc.append(round(random.uniform(42.5, 44.0),2))
    loc.append(round(random.uniform(-2.5, -3.0),2))
    return loc"""


# In[2]:


tempsum = 0.0
humsum = 0.0
c =0

while True:
    smt = showsmt()
    temphum = getTemperature_Humidity()
    loc = getLocation()
    dis = random.randint(0,1)
    tempsum += float(temphum[0])
    humsum += float(temphum[1])
    c +=1
    print(smt)
    print(temphum[0])
    print(temphum[1])
    print(loc['lat'])
    print(loc['lon'])
    print(dis)
    dweepy.dweet_for('swann_dash', {'smt': smt, 'temp': float(temphum[0]), 'hum': float(temphum[1]), 'lat': loc['lat'],
                                    'log': loc['lon'], 'disp': dis, 'tempav': round(float(tempsum/c),1), 'humav': round(float(humsum/c),1)})
    speaker.say("Data uploaded!")
    speaker.runAndWait()
    if (dis == 1):
        speaker.say("Killeeeeeer Queeeen, Bite the dustooo")
        speaker.runAndWait()
    time.sleep(1)
    #input()


# In[17]:


#dweepy.get_latest_dweet_for('prueba_daic')


# In[19]:


#dweepy.get_dweets_for('prueba_daic')


# In[ ]:




