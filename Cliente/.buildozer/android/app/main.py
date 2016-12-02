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
#from arpspoofing import *

Builder.load_string('''
<MIAPP>:
	cabecera: Banner
	cuerpo: Body
	GridLayout:
		cols: 2
		rows: 2

		BoxLayout:
			id: Banner
			orientation: 'horizontal'
			spacing: 0
			padding: 0,0,0,0

			Label:
				font_size: 50
				text: 'EXTATI'
				color: (.98,.25,.39,1)
			Label:
				font_size: 50
				text: '<CODE>'
		BoxLayout:
			id: Body
			orientation: 'vertical'
			spacing: 2
			padding: 20,5,20,5

			Button:
				id: conect
				text: 'Connect Server'
				font_size: 22
				height: 14
				background_color: (.35,.75,.87, 1)
				on_press: root.show_popup()
			Button:
				text: 'ataque 2'
				font_size: 22
				height: 14
				background_color: (.35,.75,.87, 1)
				on_press: root.show_popup()
			Button:
				text: 'nueva screen'
				font_size: 22
				height: 14
				background_color: (.35,.75,.87, 1)
				on_press: app.cambiar_screen('Arpspoofing_screen')
			Button:
				text: 'ataque 4'
				font_size: 22
				height: 14
				background_color: (.35,.75,.87, 1)
			Button:
				text: 'ataque 5'
				font_size: 22
				height: 14
				background_color: (.35,.75,.87, 1)
			Button:
				text: 'ataque 6'
				font_size: 22
				height: 14
				background_color: (.35,.75,.87, 1)

<CustomPopup>:
	title: 'Introduce Datos'
	size_hint: (None,None)
	size: (400,400)
	content: popupcontent

	BoxLayout:
		id: popupcontent
		orientation: 'vertical'
		Label:
			text: "IP Servidor"
		TextInput:
			id: ip
			multiline: False

		Label:
			text: "Puerto Servidor"
		TextInput:
			id: puerto
			multiline: False
		Button: 
			text: "Guardar"
			on_press: root.Recollect_data(ip.text, puerto.text)
				

<Arpspoofing_screen>:
	GridLayout:
		cols: 2
		rows: 2

		BoxLayout:
			orientation: 'horizontal'
			spacing: 0
			padding: 0,0,0,0

			Label:
				font_size: 22
				text: 'IP'
				color: (.98,.25,.39,1)
			TextInput:
				id: ip_atq1
				multiline: False
			Button: 
				text: "Volver"
				on_press: app.cambiar_screen('MIAPP')

''')

class MIAPP(Screen):
	def __init__(self, **kwargs):
		super(MIAPP, self).__init__(**kwargs)
 		

	def show_popup(self):
		p = CustomPopup()
		p.open()
		

class CustomPopup(Popup):
	def Recollect_data(self, ip, puerto):
		print('the Ip: %s Puerto:%s' % (ip, puerto))
		if validar_ip(ip):
			if puerto.isdigit():
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock.connect((ip,int(args[1])))
			else:
				self.ids['puerto'].text = 'puerto erroneo'			
		else:
			self.ids['ip'].text = 'ip erroneo'

class Arpspoofing_screen(Screen):
	pass


class MyApp(App):
	def build(self):
		return sm

	def cambiar_screen(self, title):
		sm.current=title


sm = ScreenManager()
sm.add_widget(MIAPP(name='MIAPP'))
sm.add_widget(Arpspoofing_screen(name='Arpspoofing_screen'))
sm.current='MIAPP'

if __name__ == '__main__':
    MyApp().run()
