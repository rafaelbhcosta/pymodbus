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

client = ModbusClient('23.102.109.123',502)
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
    escolha = input('1- INT \n2- FLOAT \n3- BOLEANO \n4- STR \n5- ALFANUMERICO \nEscolha: ')

    # Tipo de escrita INT
    if escolha == '1':
        linha()
        tipo = input('Tipo de bit para escrita:\n1- 16\n2- 32\n3- 64\n')

        # Escrita de valores do tipo 16 bit
        if tipo == '1':
            linha()
            address = int(input('Escolha o endereço da tabela ModBus: ')) - 1
            valor = int(input('O valor INT que deve ser escrito: '))
            builder.add_16bit_int(valor)
            payload = builder.to_registers()
            payload = builder.build()
            client.write_registers(address, payload, skip_encode=True, unit=1)

        # Escrita de valores do tipo 32 bit
        elif tipo == '2':
            linha()
            address = int(input('Escolha o endereço da tabela ModBus: ')) - 1
            valor = int(input('O valor INT que deve ser escrito: '))
            builder.add_32bit_int(valor)
            payload = builder.to_registers()
            payload = builder.build()
            client.write_registers(address, payload, skip_encode=True, unit=1)

        # Escrita de valores do tipo 64 bit
        elif tipo == '3':
            linha()
            address = int(input('Escolha o endereço da tabela ModBus: ')) - 1
            valor = int(input('O valor INT que deve ser escrito: '))
            builder.add_64bit_int(valor)
            payload = builder.to_registers()
            payload = builder.build()
            client.write_registers(address, payload, skip_encode=True, unit=1)

    # Tipo de escrita FLOAT
    elif escolha == '2':
        linha()
        tipo = input('Tipo de bit para escrita:\n1- 16\n2- 32\n3- 64\n')

        # Escrita de valores do tipo 16 bit
        if tipo == '1':
            linha()
            address = int(input('Escolha o endereço da tabela ModBus: ')) - 1
            valor = float(input('O valor FLOAT que deve ser escrito: '))
            builder.add_16bit_float(valor)
            payload = builder.to_registers()
            payload = builder.build()
            client.write_registers(address, payload, skip_encode=True, unit=1)

        # Escrita de valores do tipo 32 bit
        elif tipo == '2':
            linha()
            address = int(input('Escolha o endereço da tabela ModBus: ')) - 1
            valor = float(input('O valor FLOAT que deve ser escrito: '))
            builder.add_32bit_float(valor)
            payload = builder.to_registers()
            payload = builder.build()
            client.write_registers(address, payload, skip_encode=True, unit=1)

        # Escrita de valores do tipo 64 bit
        elif tipo == '3':
            linha()
            address = int(input('Escolha o endereço da tabela ModBus: ')) - 1
            valor = float(input('O valor FLOAT que deve ser escrito: '))
            builder.add_64bit_float(valor)
            payload = builder.to_registers()
            payload = builder.build()
            client.write_registers(address, payload, skip_encode=True, unit=1)
    
    # Tipo de escrita BOLEANO
    elif escolha == '3':
        linha()
        address = int(input('Escolha o endereço da tabela ModBus: ')) - 1
        valor = int(input('Escolha 1 para True ou 0 para FALSE: '))
        builder.add_bits([valor])
        payload = builder.build()
        client.write_registers(address, payload, skip_encode=True, unit=1)

    # Tipo de escrita STR
    elif escolha == '4':
        linha()
        address = int(input('Escolha o endereço da tabela ModBus: ')) - 1
        valor = input('O que deve ser escrito (max. 4 letras): ')
        builder.add_string(valor) # Valor pré determinado pelo servidor, aqui é só para teste
        payload = builder.to_registers()
        payload = builder.build()
        client.write_registers(address, payload, skip_encode=True, unit=1)

    else:
        print('Erro: Opção selecionada inválida')

else:
    print('Erro: Não foi possivel estabelecer conexão com o servidor')
