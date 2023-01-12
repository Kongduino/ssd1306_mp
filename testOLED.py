import machine, random, time
from ssd1306 import SSD1306_I2C
from machine import Timer

def centerText(screen, txt, py):
  px = int((128-(len(txt)*8))/2)
  screen.text(txt, px, py)

i2c = machine.I2C(sda=machine.Pin(16), scl=machine.Pin(17), id=0)
oled = SSD1306_I2C(128, 64, i2c)
oled.fill(1)
oled.show()
time.sleep(1)
oled.fill(0)
oled.show()

oled.text('Hello', 1, 4)
oled.show()
time.sleep(0.5)
oled.text('World!', 45, 4)
oled.show()
time.sleep(1)
oled.poweroff()
time.sleep(1)
oled.poweron()
time.sleep(1)
oled.invert(1)
time.sleep(1)
oled.invert(0)
time.sleep(1)
for i in range(0, 256, 16):
  oled.fill_rect(0, 50, 128, 63, 0)
  oled.text(f'Contrast {i}', 0, 50)
  oled.show()
  oled.contrast(i)
  time.sleep(0.1)
oled.fill_rect(0, 50, 128, 63, 0)
oled.text(f'Contrast 255', 0, 50)
oled.show()
oled.contrast(255)
time.sleep(1)

oled.fill(0)
centerText(oled, "LINES", 5)
oled.show()
for i in range(0, 128, 3):
  oled.line(i, 16, 127-i, 63, 1)
  if (i / 2) > 15 and i % 2 == 0:
    oled.line(0, int(i/2), 127, 63 - int(i / 2) + 16, 1)
  oled.show()
time.sleep(2)

oled.fill(0)
lines = []
for i in range(0, 100):
  lines.append(random.randrange(128))
  lines.append(random.randrange(64))
oled.drawConnectedLines(lines)
oled.show()
time.sleep(2)

oled.fill(0)
lines = []
for i in range(0, 100):
  lines.append(random.randrange(128))
  lines.append(random.randrange(64))
oled.drawLines(lines)
oled.show()
time.sleep(2)

oled.fill(0)
oled.show()
oled.fill_rect(0, 16, 32, 48, 1)
oled.fill_rect(2, 18, 28, 44, 0)
oled.vline(9, 24, 38, 1)
oled.vline(16, 18, 38, 1)
oled.vline(23, 24, 36, 1)
oled.fill_rect(26, 56, 2, 4, 1)
oled.text('MicroPython', 40, 16, 1)
oled.text('SSD1306', 40, 28, 1)
oled.text('OLED 128x64', 40, 40, 1)
oled.show()
time.sleep(2)
#oled.rotate180()
oled.rotate=True
oled.show()
time.sleep(2)
#oled.rotate180()
oled.rotate=False
oled.show()
time.sleep(1)
oled.fill(0)
oled.drawCircle(64, 32, 15)
oled.show()
time.sleep(0.5)
clr = 1
rd = 15
for i in range(0, 5):
  oled.fillOval(64, 32, rd, rd-2, clr)
  oled.show()
  time.sleep(0.5)
  clr = 1 - clr
  rd -= 3

clr = 1
maxrd = 9
rd = maxrd
space = 2
oled.fill(0)
oled.show()

def drc(timer):
  global clr, rd, maxrd, oled, space
  oled.fillCircle(15, 32, rd, clr)
  if clr == 1:
    oled.drawCircle(15, 32, rd + space, clr)
  clr = 1 - clr
  if clr == 1:
    rd -= space
    if rd < 3:
      rd = maxrd
  oled.show()

timer = Timer(period=500, mode = Timer.PERIODIC, callback=drc)
rd0 = 24
for i in range(0, 5):
  oled.drawOval(64, 38, rd0, rd0-4, 1)
  rd0 -= 4
  oled.show()
  time.sleep(0.75)
