import machine

led = machine.Pin(15, machine.Pin.OUT)
sensor = machine.ADC(machine.Pin(26))


