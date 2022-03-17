from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.compat import iteritems

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

client = ModbusClient('127.0.0.1', port=502)
client.connect()

builder = BinaryPayloadBuilder()
#builder.add_string('teste aa')
#builder.add_32bit_float(22.34)
#builder.add_16bit_uint(0x1234)
#builder.add_16bit_uint(0x5678)
#builder.add_8bit_int(0x12)
builder.add_bits([1])
payload = builder.build()
address = 0
result  = client.write_registers(address, payload, skip_encode=True, unit=1)

