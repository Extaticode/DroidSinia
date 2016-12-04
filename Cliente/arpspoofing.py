from kivy.uix.screenmanager import *
import globalvar
import socket

class Arpspoofing_screen(Screen):	
	def iniciar_ataque(self):
		self.ids['feedback'].text=""
		comando="comando3 "
		comando+=self.ids['interfaz'].text+" "
		comando+=self.ids['ip_atacada'].text+" "
		comando+=self.ids['ip_suplantada'].text

		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		
		sock.connect((globalvar.ip_server,int(globalvar.puerto_server)))
		sock.sendall(comando)
		mensaje=""
		while 1:
			data=sock.recv(1024)
			if (data=="close"):
				break			
			else:
							
				mensaje= mensaje+data
				data=""
				
				

		self.ids['feedback'].text=mensaje
		sock.close()

	def parar_ataque(self):
		comando="comando3 kill"
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		
		sock.connect((globalvar.ip_server,int(globalvar.puerto_server)))
		sock.sendall(comando)
		mensaje=""
		while 1:
			data=sock.recv(1024)
			if (data=="close"):
				break			
			else:
							
				mensaje+=data
				data=""
				
				

		self.ids['feedback'].text=mensaje
		sock.close()

