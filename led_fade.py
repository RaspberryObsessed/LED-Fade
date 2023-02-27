import machine
import utime

led_pin = machine.Pin(15, machine.Pin.OUT)
pwm = machine.PWM(led_pin)

pwm.duty_u16(32768)

while True:
    for duty_cycle in range(0, 65535, 1000):
        pwm.duty_u16(duty_cycle)
        utime.sleep_ms(10)

    for duty_cycle in range(65535, 0, -1000):
        pwm.duty_u16(duty_cycle)
        utime.sleep_ms(10)
