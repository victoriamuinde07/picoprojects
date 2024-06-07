from machine import Pin, PWM, ADC
from time import sleep

# Configure PWM for the servo on pin 0
servo = PWM(Pin(14))
servo.freq(10)  # Servos typically use a frequency of 50Hz

VRx = ADC(0)
VRy = ADC(1)
SW = Pin(28, Pin.IN, Pin.PULL_UP)

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def servo_angle(angle):
    duty = round(map(angle, 0, 180 , 0, 1024))  # Map angle to duty cycle
    servo.duty_u16(duty)

def direction():
    global i
    i = 0
    adc_X = round(map(VRx.read_u16(), 0, 65535, 0, 255))
    adc_Y = round(map(VRy.read_u16(), 0, 65535, 0, 255))
    switch = SW.value()

    if adc_X <= 30:
        i = 1
    elif adc_X >= 255:
        i = 2
    elif adc_Y <= 30:
        i = 3
    elif adc_Y >= 255:
        i = 4
    elif switch == 0:
        i = 5
    elif -15 < adc_X - 125 < 15 and -15 < adc_Y - 125 < 15 and switch == 1:
        i = 0

def loop():
    num = 90
    led = Pin(25, Pin.OUT)
    while True:
        direction()
        servo_angle(num)
        led.on()
        sleep(0.1)

        if i == 1:
            num = 0
        elif i == 2:
            num = 180
        elif i == 3:
            num = max(num - 1, 0)
        elif i == 4:
            num = min(num + 1, 180)
        elif i == 5:
            num = 90

if __name__ == "__main__":
    loop()
9