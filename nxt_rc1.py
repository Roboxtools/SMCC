#!/usr/bin/env python
# -*- coding: latin-1 -*- 

# REMOTE NXT  
# you need programming on nxt-g or another language to receive the data on mailbox 1. This program send 1,2,3,4,5 to 
# control up,down,left,right or sound.

import pygtk
pygtk.require('2.0')
import gtk
import os, sys 
import nxt.locator


class nxt_control:

   
		
    def enter_up(self, widget, nxt):
	print "clicked"		
	nxt.message_write(0,'1')
	self.status_bar.push(1, 'Send up')
	
    
    def enter_down(self, widget, nxt):
	print "clicked"		
	nxt.message_write(0,'2')
	self.status_bar.push(1, 'Send down')
 
    def enter_left(self, widget, nxt):
	print "clicked"		
	nxt.message_write(0,'3')
	self.status_bar.push(1, 'Send left')

    def enter_right(self, widget, nxt):
	print "clicked"		
	nxt.message_write(0,'4')
	self.status_bar.push(1, 'Send right')    

    def enter_stop(self, widget, nxt):
	print "clicked"		
	nxt.message_write(0,'5')
	self.status_bar.push(1, 'Send stop')	


    def enter_sound(self, widget, nxt):
	print "clicked"		
	nxt.message_write(5,'1')
	self.status_bar.push(1, 'Send sound')

    
	#funcion principal
    def __init__(self):
	
	# create a new window
	window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_size_request(140, 150)
	window.set_border_width(3)
	window.set_title("nxt rc")
	window.set_resizable(False)        
	window.connect("delete_event", lambda w,e: gtk.main_quit())
	window.show()
	
        table = gtk.Table(5, 3, True)
	window.add(table)
	table.set_border_width(5)	
	table.show()

	self.status_bar = gtk.Statusbar()      
        table.attach(self.status_bar, 0, 3, 4, 5)
	self.status_bar.show()
	

	print "connecting ..."
	s = nxt.locator.find_one_brick()
	b = s.connect()
	print "connected"
	self.status_bar.push(1, 'connected')


	
	

#------------------------------control-----------------------------------
	
	

	
	
	#tabla  control	
	control = gtk.Table(3, 3, False)
	table.attach(control, 0, 3, 0, 3)
	control.set_border_width(12)	
	control.show()

	#marco control
	framec = gtk.Frame()	
	table.attach(framec, 0, 3, 0,4)
	framec.show()

	#boton ▲
	buttonau = gtk.Button("▲")
	buttonau.connect("clicked", self.enter_up, b)	
	control.attach(buttonau, 1,2, 0, 1)
	buttonau.show()
	
	#boton ▼
	buttonad = gtk.Button("▼")
	buttonad.connect("clicked", self.enter_down, b)		
	control.attach(buttonad, 1,2, 2,3)
	buttonad.show()	

	#boton ■
	buttonstop = gtk.Button("■")
	buttonstop.connect("clicked", self.enter_stop, b)		
	control.attach(buttonstop, 1,2, 1,2)
	buttonstop.show()	

	#boton ◀
	buttonal = gtk.Button("↶")
	buttonal.connect("clicked", self.enter_left, b)
	control.attach(buttonal, 0,1, 1, 2)
	buttonal.show()
	
	#boton ▶
	buttonar = gtk.Button("↷")
	buttonar.connect("clicked", self.enter_right, b)	
	control.attach(buttonar, 2,3, 1,2)
	buttonar.show()	


	#boton sound
	buttonsound = gtk.Button("⊚")
	buttonsound.connect("clicked", self.enter_sound, b)		
	control.attach(buttonsound, 0,1, 0,1)
	buttonsound.show()

       

	
#-------------------------------------------------------------------------
       
        
def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    nxt_control()  
    main()

