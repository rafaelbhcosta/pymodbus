from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.compat import iteritems
from collections import OrderedDict
from defs import escrita

cone = True
while cone == True:

    client = ModbusClient('127.0.0.1', port=502)
    client.connect()

    #------
    escolha = input('Faça sua escolha (1- escreve 2- fecha)')

    if escolha == '1':
        addr = int(input('Escolha o endereço da tabela ModBus: ')) - 1
        val = int(input('O valor INT que deve ser escrito: '))
        escrita(val, addr)
    elif escolha == '2':
        client.close()
        cone = False





# from defs import ms

# teste = input('Sua msg: ')
# ms(teste)
