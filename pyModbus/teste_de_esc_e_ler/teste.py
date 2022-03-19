from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.compat import iteritems
from collections import OrderedDict

client = ModbusClient('127.0.0.1', port=502)
client.connect()

builder = BinaryPayloadBuilder()

address = int(input('Escolha o endereço da tabela ModBus: ')) - 1
valor = int(input('Escolha 1 para True ou 0 para FALSE: '))
builder.add_16bit_int(bool(valor))
payload = builder.build()
#client.write_coils(address, payload)
client.write_coils(address, payload, skip_encode=True, unit=1)
client.write_registers(address, payload, skip_encode=True, unit=1)
