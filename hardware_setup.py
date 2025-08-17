from machine import Pin, I2C
import gc

from drivers.ssd1306.ssd1306 import SSD1306_I2C as SSD
# Create and export an SSD instance
i2c = I2C(scl=Pin(1), sda=Pin(0))
gc.collect()  # Precaution before instantiating framebuf
# Instantiate display and assign to ssd. For args see display drivers doc.
ssd = SSD(128, 64, i2c, 0x3D)
# The following import must occur after ssd is instantiated.
from gui.core.ugui import Display
# # quiet()
# # Define control buttons
nxt = Pin(5, Pin.IN, Pin.PULL_UP)  # Move to next control
prev = Pin(8, Pin.IN, Pin.PULL_UP)  # Move to previous control
sel = Pin(4, Pin.IN, Pin.PULL_UP)  # Operate current control
increase = Pin(7, Pin.IN, Pin.PULL_UP)  # Increase control's value
decrease = Pin(9, Pin.IN, Pin.PULL_UP)  # Decrease control's value
# # Create a Display instance and assign to display.
display = Display(ssd, nxt, sel, prev, increase, decrease)