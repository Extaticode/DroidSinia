from kivy.uix.screenmanager import *
import socket
sm = ScreenManager()
lista_ips=[]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def init():
	global ip_server
	global puerto_server	
