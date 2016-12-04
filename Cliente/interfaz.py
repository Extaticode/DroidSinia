ui='''
<MIAPP>:
	cabecera: Banner
	cuerpo: Body
	GridLayout:
		cols: 2
		rows: 2

		BoxLayout:
			id: Banner
			orientation: 'horizontal'
			spacing: 0
			padding: 0,0,0,0

			Label:
				font_size: 50
				text: 'EXTATI'
				color: (.98,.25,.39,1)
			Label:
				font_size: 50
				text: '<CODE>'
		BoxLayout:
			id: Body
			orientation: 'vertical'
			spacing: 2
			padding: 20,5,20,5

			Button:
				id: conect
				text: 'Connect Server'
				font_size: 22
				height: 14
				background_color: (.35,.75,.87, 1)
				on_press: root.show_popup()
			Button:
				text: 'hosts-up scan'
				font_size: 22
				height: 14
				background_color: (.35,.75,.87, 1)
				on_press: app.cambiar_screen('Nmapscan_screen')
			Button:
				text: 'arp spoofing'
				font_size: 22
				height: 14
				background_color: (.35,.75,.87, 1)
				on_press: app.cambiar_screen('Arpspoofing_screen')
			Button:
				text: 'pasive scan'
				font_size: 22
				height: 14
				background_color: (.35,.75,.87, 1)
				on_press: app.cambiar_screen('Netdiscover_screen')
				
			Button:
				text: 'mac flooding'
				font_size: 22
				height: 14
				background_color: (.35,.75,.87, 1)
				on_press: app.cambiar_screen('Macflooding_screen')
			Button:
				text: 'get sniff'
				font_size: 22
				height: 14
				background_color: (.35,.75,.87, 1)

<CustomPopup>:
	title: 'Introduce Datos'
	size_hint: (None,None)
	size: (400,400)
	content: popupcontent

	BoxLayout:
		id: popupcontent
		orientation: 'vertical'
		Label:
			text: "IP Servidor"
		TextInput:
			id: ip
			multiline: False

		Label:
			text: "Puerto Servidor"
		TextInput:
			id: puerto
			multiline: False
		Button: 
			text: "Guardar"
			on_press: root.Recollect_data(ip.text, puerto.text)



	

				

<Arpspoofing_screen>:
	GridLayout:
		cols: 3
		BoxLayout:
			orientation: 'vertical'
			spacing: 0
			padding: 0,0,0,0	
			
			Label:
				font_size: 22
				
				color: (.98,.25,.39,1)
			Label:
				font_size: 22
				
				color: (.98,.25,.39,1)

			Label:
				font_size: 22
				
				color: (.98,.25,.39,1)
			Label:
				font_size: 22
				
				color: (.98,.25,.39,1)

			Button: 
				text: "Atacar"
				height: 14
				on_press: root.iniciar_ataque()
		BoxLayout:
			orientation: 'vertical'
			spacing: 0
			padding: 0,0,0,0

			Label:
				font_size: 22
				text: 'IP Maquina atacada'
				color: (.98,.25,.39,1)
			TextInput:
				id: ip_atacada
				multiline: False

			Label:
				font_size: 22
				text: 'IP Maquina a suplantar'
				color: (.98,.25,.39,1)
			TextInput:
				id: ip_suplantada
				multiline: False

			
			Label:
				font_size: 22
				text: 'Interfaz'
				color: (.98,.25,.39,1)
			TextInput:
				id: interfaz
				multiline: False
			Label:
				font_size: 22
				text: 'Feedback'
				color: (.98,.25,.39,1)
			TextInput:
				id: feedback
				multiline: True
			
				
			
			
			Button: 
				text: "Volver"
				on_press: app.cambiar_screen('MIAPP')
		BoxLayout:
			orientation: 'vertical'
			spacing: 0
			padding: 0,0,0,0
			
			Label:
				font_size: 22
				
				color: (.98,.25,.39,1)
			Label:
				font_size: 22
				
				color: (.98,.25,.39,1)

			Label:
				font_size: 22
				
				color: (.98,.25,.39,1)
			Label:
				font_size: 22
				
				color: (.98,.25,.39,1)	
			
			Button: 
				text: "Parar ataque"
				height: 14
				on_press: root.parar_ataque()

<Nmapscan_screen>:
	GridLayout:
		cols: 2
		row : 2	
		
		BoxLayout:
			orientation: 'vertical'
			spacing: 0
			padding: 0,0,0,0

			Label:
				font_size: 22
				text: 'IP a escanear'
				color: (.98,.25,.39,1)
			TextInput:
				id: ip_escaneada
				multiline: False

			Label:
				font_size: 22
				text: 'numeros de bits de red'
				color: (.98,.25,.39,1)
			TextInput:
				id: netmask
				text:''
				multiline: False
			Label:
				font_size: 22
				text: 'Feedback'
				color: (.98,.25,.39,1)
			TextInput:
				id: feedback
				text:''
				multiline: False


			Button: 
				text: "Ecanear"
				on_press: root.escanernmap()


			
		BoxLayout:
			orientation: 'vertical'
			spacing: 0
			padding: 0,0,0,0

			Label:
				font_size: 22
				text: 'ARP/SCAN'
				color: (.98,.25,.39,1)
			CheckBox :
				on_active : root.checkbox_arp()


			Label:
				font_size: 22
				text: 'TCP/ACK/SCAN'
				color: (.98,.25,.39,1)
			CheckBox :
				on_active : root.checkbox_tcp()


			Label:
				font_size: 22
				text: 'UDP/SCAN'
				color: (.98,.25,.39,1)
			CheckBox :
				on_active : root.checkbox_udp()
				

			Button: 
				text: "Volver"
				on_press: app.cambiar_screen('MIAPP')
			
			


<Resultados_screen>
	GridLayout:
		cols: 1
		row : 1
		TextInput:	
			id: resultado
			font_size: 22
			text: ''
			multiline: True
		Button:
			text: 'actualizar'
			font_size: 22
			height: 9
			background_color: (.35,.75,.87, 1)
			on_press : root.actualiza_ips()
		Button:
			text: 'menu princial'
			font_size: 22
			height: 9
			background_color: (.35,.75,.87, 1)
			on_press : app.cambiar_screen('MIAPP')


<Netdiscover_screen>
	GridLayout:
		cols: 1
		row : 1
		Label:
			font_size: 22
			text: 'Interfaz'
			color: (.98,.25,.39,1)
		TextInput:
			id: interfaz_netdiscover
			multiline: False
		Button:
			text: 'start scan'
			font_size: 22
			height: 14
			background_color: (.35,.75,.87, 1)
			on_press : root.netdiscover_scan()
			
			
		Button: 
			text: "Volver"
			on_press: app.cambiar_screen('MIAPP')
				

<Macflooding_screen>
	GridLayout:
		cols: 1
		row : 1
		Label:
			font_size: 22
			text: 'Interfaz'
			color: (.98,.25,.39,1)
		TextInput:
			id: interfaz_macflooding
			multiline: False

		Label:
			font_size: 22
			text: 'Iteraciones'
			color: (.98,.25,.39,1)
		TextInput:
			id: iteraciones_macflooding
			multiline: False
			text:''
		
		Label:
			font_size: 22
			text: 'Feedback'
			color: (.98,.25,.39,1)
		TextInput:
			id: feedback
			multiline: True
					
		
		Button:
			text: 'attack'
			font_size: 22
			height: 14
			background_color: (.35,.75,.87, 1)
			on_press : root.macflooding()						
		Button: 
			text: "Volver"
			on_press: app.cambiar_screen('MIAPP')
		
	
			


'''
