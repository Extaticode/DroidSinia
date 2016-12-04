import threading 
import os
from subprocess import *


class Macflood(threading.Thread):
	def __init__(self, interface, iteraciones):
		threading.Thread.__init__(self)
		self.interface = interface
		self.iteraciones= iteraciones

	def run(self):
		try:
			from subprocess import DEVNULL
		except ImportError:
			DEVNULL = open(os.devnull, 'wb')
		try:
			self.p=Popen(['macof','-i',self.interface,'-n',self.iteraciones],
				stdin=PIPE,
				stdout=DEVNULL,
				stderr=STDOUT)
		except KeyboardInterrupt:
			raise

	def killer(self):
		self.p.kill()