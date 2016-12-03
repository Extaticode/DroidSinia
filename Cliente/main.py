from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import *
from functools import partial
from utilities import validar_ip
import socket
import subprocess
from arpspoofing import *
from nmap import *
from interfaz import *
import globalvar
from macflood import *
from netdiscover import *



Builder.load_string(ui)

class MIAPP(Screen):
	#def __init__(self, **kwargs):
	#	super(MIAPP, self).__init__(**kwargs)
 		

	def show_popup(self):
		p = CustomPopup()
		p.open()
		

class CustomPopup(Popup):
	def Recollect_data(self, ip, puerto):
		print('the Ip: %s Puerto:%s' % (ip, puerto))
		globalvar.puerto_server=puerto
		globalvar.ip_server=ip
		if validar_ip(ip):
			if puerto.isdigit():
				pass	
				
				
			else:
				self.ids['puerto'].text = 'puerto erroneo'			
		else:
			self.ids['ip'].text = 'ip erroneo'

#class Arpspoofing_screen(Screen):
#	pass

class Resultados_screen(Screen):
	pass

class MyApp(App):
	def build(self):
		return sm

	def cambiar_screen(self, title):
		sm.current=title
	


sm.add_widget(MIAPP(name='MIAPP'))
sm.add_widget(Arpspoofing_screen(name='Arpspoofing_screen'))
sm.add_widget(Nmapscan_screen(name='Nmapscan_screen'))
sm.add_widget(Resultados_screen(name='Resultados_screen'))
sm.add_widget(Macflooding_screen(name='Macflooding_screen'))
sm.add_widget(Netdiscover_screen(name='Netdiscover_screen'))

sm.current='MIAPP'

if __name__ == '__main__':
    MyApp().run()
