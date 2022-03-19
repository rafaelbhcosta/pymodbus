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

    print('Escolha o tipo que você deseja ler: ')
    escolha = input('1- INT\n2- FLOAT\n3- STR\n4- BOLEANO \n5- DOOBLE\nEscolha:')

    if escolha == '1':
        print('=' * 70)
        address = int(input('Endereço da tabela: ')) - 1
        count   = 20
        result  = client.read_holding_registers(address, count,  unit=1)
        decoder = BinaryPayloadDecoder.fromRegisters(result.registers)

        # Função para leitura de números inteiros
        decoded = {
            'int': decoder.decode_64bit_int(),
        }

        print("-" * 70)
        print("Decoded Data")
        print("-" * 70)
        for name, value in iteritems(decoded):
            print("%s\t" % name, value)

    if escolha == '2':
        print('=' * 70)
        address = int(input('Endereço da tabela: ')) - 1
        count   = 20
        result  = client.read_holding_registers(address, count,  unit=1)
        decoder = BinaryPayloadDecoder.fromRegisters(result.registers)

        # Função para leitura de números com ponto flutuante
        decoded = {
            'float': decoder.decode_32bit_float(),
        }

        print("-" * 70)
        print("Decoded Data")
        print("-" * 70)
        for name, value in iteritems(decoded):
            print("%s\t" % name, value)

    if escolha == '3':
        print('=' * 70)
        address = int(input('Endereço da tabela: ')) - 1
        count   = 20
        result  = client.read_holding_registers(address, count,  unit=1)
        decoder = BinaryPayloadDecoder.fromRegisters(result.registers)

        # Função para leitura de strings
        decoded = {
            'string': decoder.decode_string(4),
        }

        print("-" * 70)
        print("Decoded Data")
        print("-" * 70)
        for name, value in iteritems(decoded):
            print("%s\t" % name, value)

    if escolha == '4':
        print('=' * 70)
        address = int(input('Endereço da tabela: ')) - 1
        count   = 20
        result  = client.read_holding_registers(address, count,  unit=1)
        decoder = BinaryPayloadDecoder.fromRegisters(result.registers)

        # Função para leitura de valores boleanos
        decoded = {
            'boleano': decoder.decode_bits()[0],
        }

        print("-" * 70)
        print("Decoded Data")
        print("-" * 70)
        for name, value in iteritems(decoded):
            print("%s\t" % name, value)