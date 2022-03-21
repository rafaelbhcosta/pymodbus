from enum import auto
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

client = ModbusClient('127.0.0.1', port=502)

def ms(msg):
    val = len(msg)
    print('-' * val)
    print(msg)
    print('-' * val)

def escrita(valor, address):
    builder = BinaryPayloadBuilder()
    builder.add_64bit_int(valor)
    payload = builder.to_registers()
    payload = builder.build()
    client.write_registers(address, payload, skip_encode=True, unit=1)
