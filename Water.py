import time
from grove.gpio import GPIO

__all__ = ['Water', 'GPIO']

class Water(GPIO):
   
    def __init__(self, pin):
        super(Water, self).__init__(pin, GPIO.OUT)

    def on(self):
        
        self.write(1)

    def off(self):
        
        self.write(0)


Grove = Water


def main():
    from grove.helper import SlotHelper
    sh = SlotHelper(SlotHelper.GPIO)
    pin = 22

    water = Water(pin)

    while True:
        water.on()
        time.sleep(1)
        water.off()
        time.sleep(1)


if __name__ == '__main__':
    main()
