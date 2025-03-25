import time
import machine

# led = machine.Pin(15, machine.Pin.OUT)

pwm = machine.PWM(machine.Pin(15))
sensor = machine.ADC(machine.Pin(26))
pwm.freq(60)
q = 0.002

# led.on()
# time.sleep(1)
# led.off()
# time.sleep(1)

for i in range(1024):
    list = []
    for j in range(10):
        pwm.duty(i)
        if sensor.read() != 4095:
            list.append(sensor.read())
    time.sleep(q)
    print(sum(list)/len(list))
# led.off()
