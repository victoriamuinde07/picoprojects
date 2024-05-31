from machine import Pin ,PWM
import utime

def set_servo_angle(angle,pwm):
    duty = int((angle/180) * 8000+1000)
    pwm.duty_u16(duty)
    
servo_pin = Pin(16)
servo_pwm = PWM(servo_pin)
servo_pwm.freq(50)
desired_angle = 100
set_servo_angle(desired_angle,servo_pwm)
utime.sleep(0.01)