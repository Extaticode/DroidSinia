from kivy.uix.screenmanager import *
import globalvar
import socket
class Macflooding_screen (Screen):
	def macflooding(self):
		self.ids['feedback'].text=""
		comando="comando2 "
		comando+=self.ids['interfaz_macflooding'].text+" "
		if(self.ids['iteraciones_macflooding'].text!=""):
			comando=" "+comando+self.ids['iteraciones_macflooding'].text		
		

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
	
