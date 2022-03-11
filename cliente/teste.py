from pyModbusTCP.client import ModbusClient
from time import sleep

client = ModbusClient('localhost',502)

client.open()

# client.read_holding_registers(1000,1)


print(client.is_open())


addr = 1000


var1 = client.read_holding_registers(addr,1)

var2 = client.read_coils(addr,1)

var3 = client.read_input_registers(addr,1)

var4 = client.read_discrete_inputs(addr,1)

print(f'var1: {var1}')
print(f'var2: {var2}')
print(f'var3: {var3}')
print(f'var4: {var4}')

# oi