from pyModbusTCP.client import ModbusClient
from time import sleep

# atendimento = True
# print('atendimento: ', atendimento)

class ClientMODBUS():
    #Definições de class ClienteMODBUS
    
    def __init__(self, server_ip, porta, scan_time=1):
        #constructor
        self._client = ModbusClient(host=server_ip,port=porta)
        self._scan_time = scan_time

    def atendimento(self):

        try:
            #Inicialização do cliente
            self._client.open()
        
            ate = True

            # open or reconnect TCP to server
            if not self._client.is_open():
                if not self._client.open():
                    pass
            # if open() is ok, read coils (modbus function 0x01)
            if self._client.is_open():
            
                while ate:
                    print('='*50)
                    print('Qual função deseja realizar?')
                    sel = input(f'1- Leitura \n\r2- Escrita \n\r3- Tempo de verificação \n\r4- Sair) \n\rEscolha: ')
                    
                    if sel == '1':
                        print('='*50)
                        tipo = input(f'Qual tipod de dado deseja ler? \n\r1- Registros 1 (int) \n\r2- Registros Boleanos \n\r3- Entrada de registros \n\r4- Discret Input \n\rEscolha: ')
                        print('='*50)
                        addr = input(f'Digite o endereço da tabela MODBUS: ')
                        nvezes = input(f'Digite o número de vezes que deseja ler: ')
                        for i in range(0,int(nvezes)):
                            print(f'Leitura {i+1}: {self.lerdado(int(tipo), int(addr))}')
                            sleep(self._scan_time)
                            
                    elif sel == '2':
                        print('='*50)
                        tipo = input(f'Qual tipo de dado deseja Escrever? \n\r1- Resgistro Inteiro \n\r2- Registro Boleano \n\rEscolha: ')
                        addr = input(f'Digite o endereço da tabela MODBUS: ')
                        valor = input(f'Digite o valor que vai ser escrito: ')
                        self.escreveDado(int(tipo),int(addr),int(valor))

                    elif sel == '3':
                        print('='*50)
                        scant = input('Digite o tempo de varredura em segundos \n\rTempo: ')
                        self._scan_time = float(scant)

                    elif sel == '4':
                        self._client.close()
                        ate = False

                    else:
                        print('Erro seletor escolhido invalido')
                
            else:
                print('Servidor não abriu')

        except Exception as e:
            print('Erro: ',e.args)
    
    def lerdado(self, tipo, addr):
        # leitura de um dado da tabela
        if tipo == 1:
            return self._client.read_holding_registers(addr,1)[0]
        if tipo == 2:
            return self._client.read_coils(addr,1)[0]
        if tipo == 3:
            return self._client.read_input_registers(addr,1)[0]
        if tipo == 4:
            return self._client.read_discrete_inputs(addr,1)[0]

    def escreveDado(self, tipo, addr, valor):
        #metodo para escrita de dados
        if tipo == 1:
            return self._client.write_single_register(addr,valor)
        if tipo == 2:
            return self._client.write_single_coil(addr,valor)