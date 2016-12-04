import globalvar
from kivy.uix.screenmanager import *

class Resultados_screen(Screen):
	def actualiza_ips(self):
		for (item in globalvar.lista_ips):
			self.ids['resultado'].text+=item+"/n"	
