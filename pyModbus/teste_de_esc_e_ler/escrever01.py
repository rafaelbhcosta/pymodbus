from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.compat import iteritems
from collections import OrderedDict

def linha():
    print('=' * 70)

#---------------------------------------------------------
#-----------------------Conexão---------------------------
#---------------------------------------------------------

client = ModbusClient('127.0.0.1', port=502)
client.connect()

#---------------------------------------------------------
#---------------------Teste de Conexão--------------------
#---------------------------------------------------------

print('=' *70)
if not client.connect():
    if not client.connect():
        pass
if client.connect():
    
#---------------------------------------------------------
#---------------------Funções-----------------------------
#---------------------------------------------------------

    builder = BinaryPayloadBuilder()

    print('Qual função deseja escrever?')
    print('-' *15)
    escolha = input('1- INT \n2- FLOAT \n3- STR \n4- BOLEANO \n5- DOOBLE \nEscolha: ')

    # Tipo de leitura INT
    if escolha == '1':
        linha()
        tipo = input('Tipo de bit para escrita:\n1- 16\n2- 32\n3- 64\n')

        if tipo == '1':
            linha()
            address = int(input('Escolha o endereço da tabela ModBus: ')) - 1
            valor = int(input('O valor INT que deve ser escrito: '))
            builder.add_16bit_int(valor)
            payload = builder.to_registers()
            payload = builder.build()
            client.write_registers(address, payload, skip_encode=True, unit=1)

        if tipo == '2':
            linha()
            address = int(input('Escolha o endereço da tabela ModBus: ')) - 1
            valor = int(input('O valor INT que deve ser escrito: '))
            builder.add_32bit_int(valor)
            payload = builder.to_registers()
            payload = builder.build()
            client.write_registers(address, payload, skip_encode=True, unit=1)

        if tipo == '3':
            linha()
            address = int(input('Escolha o endereço da tabela ModBus: ')) - 1
            valor = int(input('O valor INT que deve ser escrito: '))
            builder.add_64bit_int(valor)
            payload = builder.to_registers()
            payload = builder.build()
            client.write_registers(address, payload, skip_encode=True, unit=1)

#     #Função para escrita de números inteiros
#     if func == '1':
#         print('=' * 70)
#         address = int(input('Escolha o endereço da tabela ModBus: ')) - 1
#         valor = int(input('O valor INT que deve ser escrito: '))
#         builder.add_16bit_int(valor)
#         payload = builder.to_registers()
#         payload = builder.build()
#         client.write_registers(address, payload, skip_encode=True, unit=1)

#     #Função para escrita de números float
#     elif func == '2':
#         print('=' * 70)
#         address = int(input('Escolha o endereço da tabela ModBus: ')) - 1
#         valor = float(input('O valor FLOAT que deve ser escrito: '))
#         builder.add_32bit_float(valor)
#         payload = builder.to_registers()
#         payload = builder.build()
#         client.write_registers(address, payload, skip_encode=True, unit=1)

#     #Função para escrita de string
#     elif func == '3':
#         print('=' * 70)
#         address = int(input('Escolha o endereço da tabela ModBus: ')) - 1
#         valor = input('O que deve ser escrito: ')
#         builder.add_string(valor)
#         payload = builder.to_registers()
#         payload = builder.build()
#         client.write_registers(address, payload, skip_encode=True, unit=1)

#     #Função para escrita de boleano
#     elif func == '4':
#         print('=' * 70)
#         address = int(input('Escolha o endereço da tabela ModBus: ')) - 1
#         valor = int(input('Escolha 1 para True ou 0 para FALSE: '))
#         builder.add_bits([valor])
#         payload = builder.build()
#         client.write_registers(address, payload, skip_encode=True, unit=1)

# else:
#     print('Erro: Não foi possivel estabelecer conexão com o servidor')
