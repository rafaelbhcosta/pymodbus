from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.compat import iteritems
from collections import OrderedDict

#-------------------------Conexão-------------------------

client = ModbusClient('127.0.0.1', port=502)
client.connect()

#---------------------------------------------------------


addr = input('Endereço da tabela: ')
#contador = input('Quantidade de leituras: ')

address = int(addr) - 1
count   = 20
result  = client.read_holding_registers(address, count,  unit=1)
decoder = BinaryPayloadDecoder.fromRegisters(result.registers)

decoded = {
    'int': decoder.decode_16bit_int(),
}

print("-" * 60)
print("Decoded Data")
print("-" * 60)
for name, value in iteritems(decoded):
    print("%s\t" % name, value)
