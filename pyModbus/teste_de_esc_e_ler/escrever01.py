from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.compat import iteritems
from collections import OrderedDict

#---------------------------------------------------------
#-----------------------Conexão---------------------------
#---------------------------------------------------------

client = ModbusClient('127.0.0.1', port=502)
client.connect()

combos = [(wo, bo) for wo in [Endian.Big, Endian.Little] for bo in [Endian.Big, Endian.Little]]

#---------------------------------------------------------
#---------------------------------------------------------
#---------------------------------------------------------

print('=' *70)
if not client.connect():
    if not client.connect():
        pass
if client.connect():
    
    builder = BinaryPayloadBuilder()

    print('Qual função deseja escrever?')
    print('-' *15)
    func = input('1- String \n2-Int \n3-Float \n4-Boleano \nEscolha: ')

    if func == '1':
        print('=' * 70)
        addr = input('Escolha o endereço da tabela ModBus: ')
        address = int(addr) - 1
        valor = input('O que deve ser escrito: ')
        builder.add_string(valor)
        payload = builder.to_registers()
        payload = builder.build()
        client.write_registers(address, payload, skip_encode=True, unit=1)

    elif func == '2':
        print('=' * 70)
        addr = input('Escolha o endereço da tabela ModBus: ')
        address = int(addr) - 1
        val = input('O valor que deve ser escrito: ')
        valor = int(val)
        builder.add_16bit_int(valor)
        payload = builder.to_registers()
        payload = builder.build()
        client.write_registers(address, payload, skip_encode=True, unit=1)

    elif func == '3':
        print('=' * 70)
        addr = input('Escolha o endereço da tabela ModBus: ')
        address = int(addr) - 1
        val = input('O valor float que deve ser escrito: ')
        valor = float(val)
        builder.add_16bit_int(valor)
        payload = builder.to_registers()
        payload = builder.build()
        client.write_registers(address, payload, skip_encode=True, unit=1)

else:
    print('Erro: Não foi possivel estabelecer conexão com o servidor')