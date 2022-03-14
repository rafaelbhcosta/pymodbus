# from pyModbusTCP.client import ModbusClient
# from time import sleep

# client = ModbusClient('localhost',502)

# client.open()

# # client.read_holding_registers(1000,1)


# print(client.is_open())


# addr = 1000


# var1 = client.read_holding_registers(addr,1)

# var2 = client.read_coils(addr,1)

# var3 = client.read_input_registers(addr,1)

# var4 = client.read_discrete_inputs(addr,1)

# print(f'var1: {var1}')
# print(f'var2: {var2}')
# print(f'var3: {var3}')
# print(f'var4: {var4}')

# -----------------------------

from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils


class FloatModbusClient(ModbusClient):
    def read_float(self, address, number=1):
        reg_l = self.read_holding_registers(address, number * 2)
        if reg_l:
            return [utils.decode_ieee(f) for f in utils.word_list_to_long(reg_l)]
        else:
            return None

    def write_float(self, address, floats_list):
        b32_l = [utils.encode_ieee(f) for f in floats_list]
        b16_l = utils.long_list_to_word(b32_l)
        return self.write_multiple_registers(address, b16_l)


c = FloatModbusClient(host='127.0.0.1', port=502, auto_open=True)

x = input('Escolha um valor para registro: ')
z = float(x)

c.write_float(2000, [z])

float_l = c.read_float(2000)
print(type(float_l))

r = float(float_l[0])
print(type(r))

print(f'{r :.2f}')

c.close()