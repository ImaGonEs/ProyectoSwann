import math
import sys
import time
from grove.adc import ADC

 
class GroveGasSensorMQ2:
 
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()
 
    @property
    def MQ2(self):
        value = self.adc.read(self.channel)
        return value
 
Grove = GroveGasSensorMQ2
sensor = GroveGasSensorMQ2(0)  
 
def getGasValue(port):
  
    return(sensor.MQ2)

 
"""def main():
    # client = InfluxDBClient(host='localhost', port=8086, database='home')
    if len(sys.argv) < 2:
        print('Usage: {} adc_channel'.format(sys.argv[0]))
        sys.exit(1)
 
    sensor = GroveGasSensorMQ2(int(sys.argv[1]))
 
    print('Detecting...')
    while True:
        print('Gas value: {0}'.format(sensor.MQ2))
        # json_body = [
        # {
        #     "measurement": "gas_value",
        #     "fields": {
        #         "value": sensor.MQ2
        #     }
        # }
        # ]
        # client.write_points(json_body)
        time.sleep(5)
 
if __name__ == '__main__':
    main()"""
