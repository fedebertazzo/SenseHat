# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:22:57 2017

@author: fbertazzo
"""

from sense_emu import SenseHat
from time import sleep

sense=SenseHat()
""" Brillo del SenseHat"""
sense.low_light = True
#while True:
##    tTEMPERATURA
#    temp = sense.get_temperature()
#    print 'Temperatura: {0:.2f} °C'.format(temp)
#    sense.show_message("Temp: {0:.2f} C".format(temp), scroll_speed=.1, text_colour=[255,255,255],back_colour=[0,0,0])
##    PRESIÓN
#    pres= sense.get_pressure()
#    print 'Pres: {0:.3f} mBar'.format(pres)
#    sense.show_message("Pres: {0:.3f} mbar".format(pres))
##    HUMEDAD
#    hum= sense.get_humidity()
#    print 'Hum: {0:.2f} %'.format(hum)
#    sense.show_message("Hum: {0:.2f} % ".format(hum))
#    print '----------------------- \n'
#    sleep(1)
#    sense.show_letter("?")
#    jmove = sense.stick.wait_for_event()
#    print 'Joystick {}'.format(jmove.direction)
    
#    mk1= 0
#    sensores=(temp, pres, hum)
#    jmove = sense.stick.wait_for_event()
#    if jmove =down:
#        sensores(mk1)
#        sense.show_message("{0}: {1:.2f} {2}".format(sensores(mk1), 
    
    
def sensor():
    sense.clear()
    pres=sense.get_pressure()
    temp=sense.get_temperature()
    hum=sense.get_humidity()
    
    
while True:
    event = sense.stick.get_event()
    if event.action in ('pressed'):
        event = sensor({'up'=pres,'down'=hum,'left'=temp,'right'=temp1}.get(event.direction))
        
#        
#        sense.show_letter("P")
#        sleep(1)
#        pres = sense.get_pressure()
#        print ('Pres: {0.2f} mBar \n',pres)
#        sense.show_message("Pres: {0} mbar",pres)
#        sleep(0.5)
#        sense.show_letter("-")
#        jmove = sense.stick.wait_for_event(emptybuffer=True)
#        
#    if jmove.direction == "down":
#        sense.show_letter("H")
#        sleep(0.5)
#        hum = sense.get_humidity()
#        print ('Hum: %0 % \n',hum)
#        sense.show_message("Hum: %0 % ",hum)
#        sense.show_letter("-")
#        jmove = sense.stick.wait_for_event(emptybuffer=True)
#        
#    if jmove.direction == "right":
#        sense.show_letter("T")
#        sleep(0.5)
#        temp = sense.get_temperature()
#        print ('Temp: %0 % \n',temp)
#        sense.show_message("Temp: %0 C ",temp)
#        sense.show_letter("-")
#        jmove = sense.stick.wait_for_event(emptybuffer=True)
#        
#    else:
#        sense.show_letter("-")
#        print ('----\n')
#        jmove = sense.stick.wait_for_event(emptybuffer=True)
#        
#            
#            
#            
#
#        