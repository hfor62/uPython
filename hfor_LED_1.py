import time
from Maix import GPIO
from fpioa_manager import fm

fm.register(0, fm.fpioa.GPIO0, force=True)
fm.register(14, fm.fpioa.GPIO1, force=True)

led1 = GPIO(GPIO.GPIO0, GPIO.OUT)
led2 = GPIO(GPIO.GPIO1, GPIO.OUT)
status = 0
for i in range(0, 3000):

    led1.value(status)
    led2.value(status)
    time.sleep_ms(50)

    led1.value(status)
    led2.value(status)
    time.sleep_ms(50)

    status = 0 if (status == 1) else 1

   # print("LED (%d,%d)" % (led1.value(), led2.value()))


fm.unregister(0)
fm.unregister(17)
