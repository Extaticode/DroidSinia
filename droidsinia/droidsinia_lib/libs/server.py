import socket
import re
import threading
from subprocess import check_output
#from .tools import *


class server(): #threading.Thread
	"""docstring for server"""
	def __init__(self, interface, port):
		#threading.Thread.__init__(self)
		self.interface = interface
		self.port=port

	def run(self):
		server_addres=(getMyIp(self.interface),int(self.port))
		self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("Levantando servidor")
		self.sock.bind(server_addres)
		print("Espera Cliente")
		self.sock.listen(1)
		while 1:
			print ('Esperando para conectarse')
			connection, client_address = self.sock.accept()
			print('----------------------------------------------------')
			try:
				print("Conexion extablecida desde: "+ client_address[0])
				while 1:
					data = connection.recv(1024)
					
					if data:
						comando = data.split()
						print("Ejecutando Comando: "+data)
						
						if(comando[0]=="nmap"):
							ip=""
							send=""
							nmap = check_output(comando)
							respuesta = nmap.split()
							for item in respuesta:
								vec = item.split('.')
								if(len(vec)==4):
									ip=item
								vec = item.split(':')
								if(len(vec)==6):
									send+=ip+" "+item+"-"
							print("Enviando resultado:")
							print(send)
							connection.sendall(send)
							connection.sendall("close")
							print("Ha terminado: "+data)

							
						elif (comando[0]=="interfaz"):
							send=""
							ifconfig = check_output(["ifconfig"])
							respuesta = ifconfig.split()
							for item in respuesta:
								i=1
								longitud=len(item)
								for caracter in item:
									if(i==longitud and caracter==":"):
										send+=item+"-"
									i+=1
							print(send)
						
					else:
						break
			finally:
				connection.close()
			print('----------------------------------------------------')
			#break
					
def getMyIp(inteface="eth0"):
	ifconfig = check_output(['ifconfig',inteface])
	return ifconfig.split()[5]

def run(config):
	myserver=server(config.interface,config.port)
	#print(myserver.interface+" "+myserver.port)
	myserver.run()
