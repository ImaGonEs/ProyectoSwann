# Proyecto Swann
El proyecto Swann consiste en la construcción de un módulo capaz de reconocer e identificar situaciones en las que sea necesaria la desinfección del aire y actúe enconsecuencia. Es por ello que contará con diferentes sensores (tales como cámaras de infrarrojos)para la detección de aglomeraciones, y dispondrá de un dispensador para la propagación de cualquier desinfectante no dañino. El módulo podría ser acoplado a varios drones de vigilanciaautomáticos que “patrullarían” por las grandes ciudades en busca de situaciones de riesgo donde intervenir.


## Instalación

A continuación, explicaremos la instalación del software necesario para que una vez este el modulo montado puedas ponerlo a funcionar. 


### Prerequisitos

Para poner en marcha el módulo necesitarás:
   -   Python
   -   Grove.py,
   -   Requests

   
Adémas, necesitaras unas pocas librerias más para su correcto funcionamiento. Para instalarlas tan solo debes ejecutar:
```
python setup.py install
```

Hará falta que instales manualmente dos de estas librerias ya que Setuptools no las soporta, para ello:
```
pip install pyttsx
```
```
pip install Adafruit-DHT
```


### Uso
Clona nuestro repositiorio con:
```
git clone https://github.com/ImaGonEs/ProyectoSwann
```
Tran haber instalado las librerias necesarias navega hasta el directorio y ejecuta el Main.py con:
```
python Main.py
```

Una vez hecho esto, el modulo comenzara a recoger y enviar datos para su análisis. Estos datos pueden ser vistos en forma de Dashboard en:

https://freeboard.io/board/uuCpfr



## Creado con
* [Grove.py](https://github.com/Seeed-Studio/grove.py) 
* [SetupTools](https://setuptools.readthedocs.io/en/latest/)
* [Python Libraries](https://pypi.org/):
   
   -   Adafruit-DHT
   
   -   Dweepy
   
   -   Flask
   
   -   Picamera
   
   -   Pyttsx3
   
   -   Requests

## Authores

* **Marta de Madariaga** - (https://github.com/martademadariaga)
* **Imanol González** - (https://github.com/ImaGonEs/)
* **Enrique Lopez** - (https://github.com/Kike00)

