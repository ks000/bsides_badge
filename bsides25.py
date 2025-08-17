import hardware_setup
from gui.core.ugui import Screen, ssd

from gui.widgets import Button, CloseButton, Label
#from gui.widgets import Listbox
from gui.core.writer import Writer

# Font for CWriter
import gui.fonts.arial10 as font
import gui.fonts.freesans20 as freesans20
from gui.core.colors import *

import random
import machine
from machine import Pin
import neopixel
import rgbled
leds_num = 16
np = neopixel.NeoPixel(machine.Pin(3), leds_num)
np.fill(rgbled.COLOR_BLACK)
np.write()

wri = Writer(ssd, font, verbose=False)
wri20 = Writer(ssd, freesans20, verbose=False)

def cb_menu_enter(lb, s):
    print('Enter menu', menu_list[s][0])
    Screen.change(menu_list[s][1])

def cb_menu_prev(lb, s):
    print('Prev menu from', s)
    if s > 0:
        new_menu = s-1
    else:
        new_menu = len(menu_list)-1
    Screen.change(MenuScreen, mode=Screen.REPLACE, args=(new_menu,))

def cb_menu_next(lb, s):
    print('Next menu from', s)
    if s < len(menu_list)-1:
        new_menu = s+1
    else:
        new_menu = 0
    Screen.change(MenuScreen, mode=Screen.REPLACE, args=(new_menu,))

def cb_menu_back(lb, s):
    Screen.back()

def cb_leds_green(lb, s):
    np.fill(rgbled.COLOR_GREEN)
    np.write()
    
def cb_leds_random(lb, s):
    color = rgbled.hsv_to_rgb((random.random()*360, 1, 0.1))
    np.fill(color)
    np.write()
    
def cb_leds_off(lb, s):
    np.fill(rgbled.COLOR_BLACK)
    np.write()

class AboutScreen(Screen):
    def __init__(self):
        super().__init__()
        Label(wri, 2, 2, justify=Label.CENTRE, bdcolor=False, text='About')
        Label(wri, 18, 2, justify=Label.CENTRE, bdcolor=False, text='BSides 2025')
        Button(wri, 2, 90, width=10, height=10, bdcolor=False, callback=cb_menu_back, text="Back", args=(self,))

class GamesScreen(Screen):
    def __init__(self):
        super().__init__()
        Label(wri, 2, 2, justify=Label.CENTRE, bdcolor=False, text='Games')
        Label(wri, 18, 2, justify=Label.CENTRE, bdcolor=False, text='...')
        Button(wri, 2, 90, width=10, height=10, bdcolor=False, callback=cb_menu_back, text="Back", args=(self,))

class SponsorsScreen(Screen):
    def __init__(self):
        super().__init__()
        Label(wri, 2, 2, justify=Label.CENTRE, bdcolor=False, text='Sponsors')
        Label(wri, 18, 2, justify=Label.CENTRE, bdcolor=False, text='...')
        Button(wri, 2, 90, width=10, height=10, bdcolor=False, callback=cb_menu_back, text="Back", args=(self,))

class ThankyouScreen(Screen):
    def __init__(self):
        super().__init__()
        Label(wri, 2, 2, justify=Label.CENTRE, bdcolor=False, text='Thank you')
        Label(wri, 18, 2, justify=Label.CENTRE, bdcolor=False, text='...')
        Button(wri, 2, 90, width=10, height=10, bdcolor=False, callback=cb_menu_back, text="Back", args=(self,))

class LightsScreen(Screen):
    def __init__(self):
        super().__init__()
        Label(wri, 2, 2, justify=Label.CENTRE, bdcolor=False, text='Lights')
        # Label(wri, 18, 2, justify=Label.CENTRE, bdcolor=False, text='...')
        Button(wri, 18, 2, width=40, height=10, bdcolor=False, callback=cb_leds_green, text="Green", args=(self,))
        Button(wri, 30, 2, width=40, height=10, bdcolor=False, callback=cb_leds_random, text="Random", args=(self,))
        Button(wri, 42, 2, width=40, height=10, bdcolor=False, callback=cb_leds_off, text="Off", args=(self,))
        Button(wri, 2, 90, width=10, height=10, bdcolor=False, callback=cb_menu_back, text="Back", args=(self,))

menu_list = (('BSIDES 25', AboutScreen, ('1',)),
       ('Games', GamesScreen, ('2',)),
       ('Sponsors', SponsorsScreen, ('3',)),
       ('Thank you', ThankyouScreen, ('4',)),
       ('Lights', LightsScreen, ('5',)))

class MenuScreen(Screen):
    def __init__(self, menu_id):
        super().__init__()
        Label(wri, 2, 60, justify=Label.CENTRE, bdcolor=False, text=f"{menu_id+1}/{len(menu_list)}")
        Button(wri, 2, 2, width=10, height=10, bdcolor=False, callback=cb_menu_prev, text="<", args=(menu_id,))
        Button(wri, 2, 116, width=10, height=10, bdcolor=False, callback=cb_menu_next, text=">", args=(menu_id,))
        Button(wri20, 30, 11, width=110, height=30, bdcolor=False, callback=cb_menu_enter, text=menu_list[menu_id][0], args=(menu_id,))

s = """
BSsides 2025 test
"""

def test():
    print(s)
    Screen.change(MenuScreen, args=(0,))

test()
