import socket
import threading
from subprocess import check_output
#from .tools import *


class server(threading.Thread):
	"""docstring for server"""
	def __init__(self, interface, port):
		threading.Thread.__init__(self)
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

			try:
				print("Conexion extablecida desde: "+ client_address)
				while 1:
					data = connection.recv(19)
					print("Recivido"+data)
					if data:
						print("Hay mas datos")
					else:
						print("No hay mas datos")
						break
			finally:
				connection.close()
					
def getMyIp(inteface="eth0"):
	ifconfig = check_output(['ifconfig',inteface])
	return ifconfig.split()[5]

def run(config):
	myserver=server(config.interface,config.port)
	#print(myserver.interface+" "+myserver.port)
	myserver.run()
