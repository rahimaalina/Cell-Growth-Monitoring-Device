import machine

button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin(15, machine.Pin.OUT)

while True:
    if button.value():
        led.off()
    else:
        led.on()