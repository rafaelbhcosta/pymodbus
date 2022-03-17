from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.compat import iteritems
from collections import OrderedDict

client = ModbusClient('127.0.0.1', port=502)
client.connect()

combos = [(wo, bo) for wo in [Endian.Big, Endian.Little] for bo in [Endian.Big, Endian.Little]]

    
builder = BinaryPayloadBuilder()
strng = "abcde"
builder.add_string(strng)
builder.add_bits([0, 1, 0, 1, 1, 0, 1, 0])
builder.add_8bit_int(12)
builder.add_8bit_uint(0x12)
builder.add_16bit_int(-0x5678)
builder.add_16bit_uint(0x1234)
builder.add_32bit_int(1234)
builder.add_32bit_uint(0x12345678)
builder.add_16bit_float(12.34)
builder.add_16bit_float(-12.34)
builder.add_32bit_float(22.34)
builder.add_32bit_float(-22.34)
builder.add_64bit_int(0xDEADBEEF)
builder.add_64bit_uint(0x12345678DEADBEEF)
builder.add_64bit_uint(0x12345678DEADBEEF)
builder.add_64bit_float(123.45)
builder.add_64bit_float(-123.45)
payload = builder.to_registers()
print("-" * 60)
print("Writing Registers")
print("-" * 60)
print(payload)
print("\n")
payload = builder.build()
address = 0
# registers = builder.to_registers()
# client.write_registers(address, registers, unit=1)
client.write_registers(address, payload, skip_encode=True, unit=1)
