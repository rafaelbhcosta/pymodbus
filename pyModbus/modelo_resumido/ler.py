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

address = 0x00
count   = 8
result  = client.read_holding_registers(address, count,  unit=1)
decoder = BinaryPayloadDecoder.fromRegisters(result.registers)
decoded = {
    'string': decoder.decode_string(8),
    'float': decoder.decode_32bit_float(),
    '16uint': decoder.decode_16bit_uint(),
    'ignored': decoder.skip_bytes(2),
    #'8int': decoder.decode_32bit_int(),
    'bits': decoder.decode_bits(),
}

print("-" * 60)
print("Decoded Data")
print("-" * 60)
for name, value in iteritems(decoded):
    print ("%s\t" % name, value)