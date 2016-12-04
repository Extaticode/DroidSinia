from subprocess import check_output

def getMyIp(inteface="eth0"):
	ifconfig = check_output(['ifconfig',inteface])
	return ifconfig.split()[5]

def getMyInterface():
	interfaces=[]
	ifconfig = check_output(["ifconfig"])
	respuesta = ifconfig.split()
	for item in respuesta:
		i=1
		longitud=len(item)
		for caracter in item:
			if(i==longitud and caracter==":"):
				interfaces.append(item.replace(":",""))
			i+=1
	return interfaces

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

def validacion_nmap(par_entrada):
	num = 0
	comando=["-PR","-PA","-PU"]
	
	for parametro in par_entrada:
		if parametro in comando:
			num+=1
		if validar_ip(parametro):
			num+=1
	
	if len(par_entrada)==num:
		return 1

	return 0

def validacion_arpmim(par_entrada, interfaz):
    if(len(par_entrada)!=3):
        return 0   
    if(validar_ip(par_entrada[1]) & validar_ip(par_entrada[2]) & (par_entrada[0] in interfaz)):
        return 1
 
def validacion_macflood(par_entrada, interfaz):
    if(len(par_entrada)!=2):
        return 0
    try:
        int(par_entrada[1])
        return 1
    except:
        return 0