from sense_emu import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

    
def up1():
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
      O,O,O,G,G,O,O,O,
      O,O,G,G,G,G,O,O,
      O,G,G,G,G,G,G,O,
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O
    ]
    return logo
    
def up2():
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
      O,O,G,G,G,G,O,O,
      O,G,G,G,G,G,G,O,
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,O,O,O,O,O
    ]
    return logo

def up3():
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
      O,G,G,G,G,G,G,O,
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O,
    ]
    return logo


def up4():
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O
    ]
    return logo
    
    
def up5():
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O
    ]
    return logo
    
def up6():
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O
    ]
    return logo

def up7():
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
      O,O,O,G,G,O,O,O,
      O,O,O,G,G,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O
    ]
    return logo


def up8():
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
      O,O,O,G,G,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O,
      O,O,O,O,O,O,O,O
    ]
    return logo
    
"""def vacio():
  O = nothing
  logo= [
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O
    ]
    return  logo
   """ 

  
images = [up1, up2, up3, up4, up5, up6, up7, up8]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.20)
    count += 1
    print count
    
    