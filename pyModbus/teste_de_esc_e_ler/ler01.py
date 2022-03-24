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

linha()
if not client.connect():
    if not client.connect():
        pass
if client.connect():
    
#---------------------------------------------------------
#---------------------Funções-----------------------------
#---------------------------------------------------------


# int16, 32 e 64
# float16, 32 e 64
# Uint16, 32 e 64
# bit
# string 

    print('Escolha o tipo que você deseja ler: ')
    escolha = input('1- INT\n2- FLOAT\n3- BOLEANO\n4- STR \n5- DOOBLE\nEscolha:')
    
    # Tipo de leitura INT
    if escolha == '1':
        linha()
        tipo = input('Tipo de bit para leitura:\n1- 16\n2- 32\n3- 64\n')

        # Leitura de valores do tipo 16 bit
        if tipo == '1':
            linha()
            address = int(input('Endereço da tabela: ')) - 1
            count   = 1
            result = client.read_holding_registers(address, count, unit=1)
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers)
            print(decoder.decode_16bit_int())

        # Leitura de valores do tipo 32 bit
        if tipo == '2':
            linha()
            address = int(input('Endereço da tabela: ')) - 1
            count   = 2
            result = client.read_holding_registers(address, count, unit=1)
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers)
            print(decoder.decode_32bit_int())

        # Leitura de valores do tipo 32 bit
        if tipo == '3':
            linha()
            address = int(input('Endereço da tabela: ')) - 1
            count   = 4
            result = client.read_holding_registers(address, count, unit=1)
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers)
            print(decoder.decode_64bit_int())
    
    # Tipo de leitura FLOAT
    if escolha == '2':
        linha()
        tipo = input('Tipo de bit para leitura:\n1- 16\n2- 32\n3- 64\n')
        
        # Leitura de valores do tipo 16 bit
        if tipo == '1':
            linha()
            address = int(input('Endereço da tabela: ')) - 1
            count   = 1
            result = client.read_holding_registers(address, count, unit=1)
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers)
            print(decoder.decode_16bit_float())

        # Leitura de valores do tipo 32 bit
        if tipo == '2':
            linha()
            address = int(input('Endereço da tabela: ')) - 1
            count   = 2
            result = client.read_holding_registers(address, count, unit=1)
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers)
            print(decoder.decode_32bit_float())

        # Leitura de valores do tipo 64 bit
        if tipo == '3':
            linha()
            address = int(input('Endereço da tabela: ')) - 1
            count   = 4
            result = client.read_holding_registers(address, count, unit=1)
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers)
            print(decoder.decode_64bit_float())

    # Tipo de leitura BOLEANO
    if escolha == '3':
        linha()
        address = int(input('Endereço da tabela: ')) - 1
        count   = 1
        result = client.read_holding_registers(address, count, unit=1)
        decoder = BinaryPayloadDecoder.fromRegisters(result.registers)
        print(decoder.decode_bits()[0])

    # if escolha == '3':
    #     print('=' * 70)
    #     address = int(input('Endereço da tabela: ')) - 1
    #     count   = 3
    #     result  = client.read_holding_registers(address, count,  unit=1)
    #     decoder = BinaryPayloadDecoder.fromRegisters(result.registers)

    #     # Função para leitura de strings
    #     decoded = {
    #         'string': decoder.decode_string(6),
    #     }

    #     print("-" * 70)
    #     print("Decoded Data")
    #     print("-" * 70)
    #     for name, value in iteritems(decoded):
    #         print("%s\t" % name, value)

    # if escolha == '4':
    #     print('=' * 70)
    #     address = int(input('Endereço da tabela: ')) - 1
    #     count   = 1
    #     result  = client.read_holding_registers(address, count,  unit=1)
    #     decoder = BinaryPayloadDecoder.fromRegisters(result.registers)

    #     # Função para leitura de valores boleanos
    #     decoded = {
    #         'boleano': decoder.decode_bits()[0],
    #     }

    #     print("-" * 70)
    #     print("Decoded Data")
    #     print("-" * 70)
    #     for name, value in iteritems(decoded):
    #         print("%s\t" % name, value)

    #---------------------------------------------------------

    #Destinado para o dooble
    # if escolha == '5':
    #     print('=' * 70)
    #     address = int(input('Endereço da tabela: ')) - 1
    #     count   = 20