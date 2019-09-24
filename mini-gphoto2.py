#!/usr/bin/env python
#programa de importe automatico para gphoto utilizable para stopmotion 

import pygtk
pygtk.require('2.0')
import gtk
import os

class gphoto_shot:

	#funcion del boton y del area de texto
    def enter_callback(self, widget, entry, spint):
	spin = spint.get_text()	
	entry_text = entry.get_text()
        print "Directorio: %s\n" % entry_text
	scene = "sc-%s" %spin	
	print "spint: %s" %scene
	name = 	"_frame-%H%M%S.jpg"
	comando = "gphoto2 --set-config capturetarget=0 && gphoto2 --frames=1 --interval=1 		--capture-image --filename=%s" % entry_text + scene + name
	os.system(comando) 

 

    	#funcion del boton editable
    def entry_toggle_editable(self, checkbutton, entry):
        entry.set_editable(checkbutton.get_active())

	#funcion principal
    def __init__(self):
        # create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_size_request(200, 130)
	window.set_border_width(3)
	window.set_title("mini gphoto")
        window.connect("delete_event", lambda w,e: gtk.main_quit())

       	table = gtk.Table(4, 4, True)
	window.add(table)
	
	table.set_border_width(5)	
	table.show()

	label = gtk.Label("scene")
	table.attach(label, 0, 1, 2,3)	
	label.show()	

	label = gtk.Label("Directory:      ")
	table.attach(label, 0, 2, 0,1)	
	label.show()
	
	adj = gtk.Adjustment(1, 1, 60, 1, 1, 0)
        spinner2 = gtk.SpinButton(adj, 0.0, 0)
        spinner2.set_wrap(True)
	table.attach(spinner2, 1, 2, 2,3)
        spinner2.show()
	
	entry = gtk.Entry()
        entry.set_max_length(50)
        entry.connect("activate", self.enter_callback, entry)
        #directorio por defecto
        entry.insert_text("/home/jorge/camara/", len(entry.get_text()))
        entry.select_region(0, len(entry.get_text()))
	table.attach(entry, 0, 4, 1,2)
        entry.show()

	        
	check = gtk.CheckButton("unlock")
        table.attach(check, 2, 4, 0,1)
        check.connect("toggled", self.entry_toggle_editable, entry)
        check.set_active(True)
        check.show()
    
        
	button1 = gtk.Button("Shot")
        button1.connect("clicked", self.enter_callback, entry, spinner2)
	table.attach(button1, 2, 4, 2,4)
        button1.show()
       
        #boton salida                          
        #button = gtk.Button("salir")
        #button.connect("clicked", lambda w: gtk.main_quit())
        #table.attach(button, 3, 4, 4,5)
        #button.set_flags(gtk.CAN_DEFAULT)
        #button.grab_default()
        #button.show()
        window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    gphoto_shot()
    main()

