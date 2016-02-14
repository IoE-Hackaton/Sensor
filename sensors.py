from pyfirmata import Arduino
from pyfirmata import util

import math
from threading import Timer

counter = None
a = None
temp = None

def setBoard(boardType, port):
  if boardType == 'arduino':
    board = Arduino(port)
  else:
    board = ArduinoMega(port)
  return board
board=setBoard('arduino', '/dev/ttyACM0')
reader = util.Iterator(board)
reader.start()

pin_var = board.get_pin("a:0:i")

pin_var2 = board.get_pin("d:11:i")

pin_var3 = board.get_pin("d:2:i")

pin_var4 = board.get_pin("d:3:i")

pin_var5 = board.get_pin("d:4:i")

pin_var6 = board.get_pin("d:5:i")

pin_var7 = board.get_pin("d:6:i")

pin_var8 = board.get_pin("d:7:i")

pin_var9 = board.get_pin("d:8:i")

pin_var10 = board.get_pin("d:9:i")

pin_var11 = board.get_pin("d:10:i")


print('Hello from PL-Cloud')
counter = 0
a = [False, False, False, False, False, False, False, False, False, False, False]
def loopCode():
  global counter, a, temp
  counter = counter + 1
  if counter == 100:
    counter = 0
    temp = round((pin_var.read() or 0) * 1023)
    temp = temp * 0.004882814
    temp = temp - 0.5
    temp = temp * 100
    print(round(temp))
  if (pin_var2.read()) == True:
    if a[0] == False:
      a[0] = True
      print('Tag 1 ON')
  else:
    if a[0] == True:
      a[0] = False
      print('Tag 1 OFF')
  if (pin_var3.read()) == True:
    if a[1] == False:
      a[1] = True
      print('Tag 2 ON')
  else:
    if a[1] == True:
      a[1] = False
      print('Tag 2 OFF')
  if (pin_var4.read()) == True:
    if a[2] == False:
      a[2] = True
      print('Tag 3 ON')
  else:
    if a[2] == True:
      a[2] = False
      print('Tag 3 OFF')
  if (pin_var5.read()) == True:
    if a[3] == False:
      a[3] = True
      print('Tag 4 ON')
  else:
    if a[3] == True:
      a[3] = False
      print('Tag 4 OFF')
  if (pin_var6.read()) == True:
    if a[4] == False:
      a[4] = True
      print('Tag 5 ON')
  else:
    if a[4] == True:
      a[4] = False
      print('Tag 5 OFF')
  if (pin_var7.read()) == True:
    if a[5] == False:
      a[5] = True
      print('Tag 6 ON')
  else:
    if a[5] == True:
      a[5] = False
      print('Tag 6 OFF')
  if (pin_var8.read()) == True:
    if a[6] == False:
      a[6] = True
      print('Tag 7 ON')
  else:
    if a[6] == True:
      a[6] = False
      print('Tag 7 OFF')
  if (pin_var9.read()) == True:
    if a[7] == False:
      a[7] = True
      print('Tag 8 ON')
  else:
    if a[7] == True:
      a[7] = False
      print('Tag 8 OFF')
  if (pin_var10.read()) == True:
    if a[8] == False:
      a[8] = True
      print('Tag 9 ON')
  else:
    if a[8] == True:
      a[8] = False
      print('Tag 9 OFF')
  if (pin_var11.read()) == True:
    if a[9] == False:
      a[9] = True
      print('Tag 10 ON')
  else:
    if a[9] == True:
      a[9] = False
      print('Tag 10 OFF')
  Timer(0.001, loopCode).start()
loopCode()
