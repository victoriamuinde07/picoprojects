from machine import I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16
i2c =I2C (0,sda=machine.Pin(0) , scl = machine.Pin(1),freq=400000)
lcd = i2cLcd(i2c,I2C_ADDR,totalRows,totalColumns)
def greeting():
    lcd.clear()
    lcd.move_to(5,0)
    lcd.putstr("Hello")
    lcd.move_to(3,1)
    lcd.putstr("vickie")
    utime.sleep(2)
    lcd.clear()
greeting()
while True:
    pass
    
