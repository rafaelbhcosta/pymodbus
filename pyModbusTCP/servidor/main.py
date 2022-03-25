from servidormodbus import ServidorMODBUS

s = ServidorMODBUS(host_ip='127.0.0.1',port=502)
s.run()

# O endereço a cima (127....) é o endereço de local host, ou seja só vai funcionar no seu computador
# Caso esse endereço apresente erro de conexão pode ser tocado por 
# 'localhost'
# ou
# '0.0.0.0'
# Esse sistema de endereçamento vária de sitema para sitema (windows, linux, mac...) 