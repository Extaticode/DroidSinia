
def validar_ip(ip):
	a = ip.split('.')
	if (a.__len__() != 4):
		return False
	else:
		for i in range(4):
			if(int(a[i]) >= 0 & int(a[i]) <= 255):
				pass
			else:
				return False
		return True




