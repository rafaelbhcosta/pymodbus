from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.compat import iteritems
from collections import OrderedDict

client = ModbusClient('127.0.0.1', port=502)
client.connect()

builder = BinaryPayloadBuilder()

#------

print('Qual função deseja escrever?')
print('-' *15)
func = input('1- INT \n2- FLOAT \n3- STR \n4- BOLEANO \n5- DOOBLE \nEscolha: ')

#Função para escrita de números inteiros
if func == '1':
    print('=' * 70)
    address = int(input('Escolha o endereço da tabela ModBus: ')) - 1
    valor = int(input('O valor INT que deve ser escrito: '))
    builder.add_64bit_int(valor)
    payload = builder.to_registers()
    payload = builder.build()
    client.write_registers(address, payload, skip_encode=True, unit=1)




# from defs import ms

# teste = input('Sua msg: ')
# ms(teste)
