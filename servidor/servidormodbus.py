from pyModbusTCP.server import DataBank, ModbusServer
import random
from time import sleep


class ServidorMODBUS:
    # Classe Servidor ModBus

    def __init__(self, host_ip, port):
        # Construtor
        self._server = ModbusServer(host=host_ip,port=port,no_block=True)
        self._db = DataBank
        print(host_ip)
        print(port)

    def run(self):
        # Execução do servidor
        try:
            self._server.start()
            print("Servidor em execução")
            while True:
                self._db.set_words(1000,[random.randint(int(0.74*400), int(1.05*400))])
                print('=' * 20)
                print("tabela Modbus")
                print(f'Holding Register \r\n R1000: {self._db.get_words(1000)} \r\n R2000: {self._db.get_words(2000)}')
                print(f'Coil \r\n C3000: {self._db.get_bits(3000)}')
                print(f'Float \r\n D4000: {self._db.get_words(4000)}')
                sleep(1)
        except Exception as e:
            print("Erro: ", e.args)
