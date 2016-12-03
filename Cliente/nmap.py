from kivy.uix.screenmanager import *
import globalvar
import socket


class Nmapscan_screen(Screen):
	
	arpscan=0
	tcpscan=0
	udpscan=0
	
	
	#sn(no escanear puertos)
	#PR(arp ping)
	#PA(tcp/ack ping)
	#PU(udp ping)
		
	


	def checkbox_arp(self):
		print globalvar.ip_server
		if(self.arpscan==0):
			self.arpscan=1
		else:
			self.arpscan=0	

	def checkbox_tcp(self):
		if(self.tcpscan==0):
			self.tcpscan=1
		else:
			self.tcpscan=0
	
	def checkbox_udp(self):
		if(self.udpscan==0):
			self.udpscan=1
		else:
			self.udpscan=0

		
	def escanernmap(self):
		globalvar.lista_ips=[] 
		comando = "nmap -sn "
		
		if(self.arpscan==1):
			comando+="-PR "
		if(self.tcpscan==1):
			comando+="-PA "
		if(self.udpscan==1):
			comando+="-PU "

		comando+=self.ids['ip_escaneada'].text
		if(self.ids['netmask'].text!=""):
			comando+="/"
			comando+=self.ids['netmask'].text
		
		self.ids['ip_escaneada'].text=comando
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		
		sock.connect((globalvar.ip_server,int(globalvar.puerto_server)))
		sock.sendall(comando)
		mensaje=""
		while 1:
			data=sock.recv(1024)
			if (data=="close"):
				break			
			else:
				print data			
				mensaje+=data
				data=""
				
				

		print mensaje
			
		sock.close()
		globalvar.lista_ips=[]
		hosts_info=mensaje.split("-")
		for item in hosts_info:
			subitem = item.split()
			print (subitem)
		
		
		


		







	

			
		
