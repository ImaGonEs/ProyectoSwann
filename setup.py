from setuptools import setup, find_packages

#Las dos librerias que estan comentadas no se instalan bien con el setup, hay que hacerlo a mano con
    # 'pip install pyttsx' y 'pip install Adafruit-DHT'
setup(
   name='Swann_Project',
   version='1.0',
   description='La ponemos al final',
   author='Team 13',
   packages=find_packages(), 
   install_requires=[
   	"dweepy==0.3.0",
   #	"pyttsx3",
   #	"Adafruit-DHT",
   	"requests==2.25.1",
   	"grove.py==0.6",
   	"Flask==1.1.2",
   	"picamera==1.13",
#Buzzer al 16 pin 16
#Movement al 18
#Ultrasonido 5
#Temperatura y humedad al 12
#22 el relee
   ], 
)
