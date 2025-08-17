# BSides 25 badge

## Hardware

ESP32-C3FH4 (4MB flash)

## Device preparation

Install `esptool` and `mpremote`
```
pip install --user esptool mpremote
```

Install MicroPython v1.25.0
```
wget https://micropython.org/resources/firmware/ESP32_GENERIC_C3-20250415-v1.25.0.bin
esptool --port <port> erase_flash
esptool --port <port> --baud 921600 write_flash 0 ESP32_GENERIC_C3-20250415-v1.25.0.bin
```

## Software

Install micropython-micro-gui

```
git clone https://github.com/peterhinch/micropython-micro-gui.git
mpremote mip install("github:peterhinch/micropython-micro-gui")
mpremote fs mkdir :lib/drivers
mpremote fs mkdir :lib/drivers/ssd1306
mpremote fs cp lib/rgbled.py :lib
mpremote fs cp micropython-micro-gui/drivers/boolpalette.py :lib/drivers/boolpalette.py
mpremote fs cp micropython-micro-gui/drivers/ssd1306/ssd1306.py :lib/drivers/ssd1306/ssd1306.py
mpremote fs cp micropython-micro-gui/gui/fonts/freesans20.py :lib/gui/fonts
mpremote fs cp hardware_setup.py :lib
mpremote fs cp bsides25.py :lib
mpremote fs cp boot.py :
```