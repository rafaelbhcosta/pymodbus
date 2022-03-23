from servidormodbus import ServidorMODBUS

s = ServidorMODBUS(host_ip='127.0.0.1',port=502)
s.run()