from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
from time import sleep


class ClientMODBUS():
    #Definições de class ClienteMODBUS
    
    #Contrução inicial do acesso e abertura do cliente
    def __init__(self, server_ip, porta, scan_time=1):
        self._client = ModbusClient(host=server_ip,port=porta)
        self._scan_time = scan_time

    def atendimento(self):

        try:
            
            #Comando que vai starta o cliente
            self._client.open()
        
            ate = True

            #Sistema para testar se o cliente abriu e conectou com o servidor
            #Se o servividor conectou com sucesso o menu vai abrir caso contrario vai avisar o erro
            if not self._client.is_open():
                if not self._client.open():
                    pass
            if self._client.is_open():
                
                #Aqui é onde você inicia o menu do cliente, e aprende como funciona o envio e requisição de dados
                while ate:
                    print('='*50)
                    print('Qual função deseja realizar?')
                    sel = input(f'1- Leitura \n\r2- Escrita \n\r3- Tempo de verificação \n\r4- Sair \n\rEscolha: ')
                    
                    #Menu apenas de leitura de dados
                    if sel == '1':
                        print('='*50)
                        tipo = input(f'Qual tipod de dado deseja ler? \n\r1- Registros (int) \n\r2- Registros Boleanos \n\r3- Entrada de registros \n\r4- Discret Input \n\r5- Registros Float \n\rEscolha: ')
                        print('='*50)

                        #Leitura de dados do tipo INT
                        if tipo == '1':
                            addr = input(f'Digite o endereço da tabela MODBUS: ')
                            nvezes = input(f'Digite o número de vezes que deseja ler: ')
                            for i in range(0,int(nvezes)):
                                print(f'Leitura {i+1}: {self.lerdado(int(tipo), int(addr))}')
                                sleep(self._scan_time)

                        #Leitura de dados do tipo Boleano
                        elif tipo == '2':
                            addr = input(f'Digite o endereço da tabela MODBUS: ')
                            nvezes = input(f'Digite o número de vezes que deseja ler: ')
                            for i in range(0,int(nvezes)):
                                print(f'Leitura {i+1}: {self.lerdado(int(tipo), int(addr))}')
                                sleep(self._scan_time)

                        #Leitura de registros efetuados recentemente
                        elif tipo == '3':
                            addr = input(f'Digite o endereço da tabela MODBUS: ')
                            nvezes = input(f'Digite o número de vezes que deseja ler: ')
                            for i in range(0,int(nvezes)):
                                print(f'Leitura {i+1}: {self.lerdado(int(tipo), int(addr))}')
                                sleep(self._scan_time)
                        
                        #Leitura de entrada de dados discretos
                        elif tipo == '4':
                            addr = input(f'Digite o endereço da tabela MODBUS: ')
                            nvezes = input(f'Digite o número de vezes que deseja ler: ')
                            for i in range(0,int(nvezes)):
                                print(f'Leitura {i+1}: {self.lerdado(int(tipo), int(addr))}')
                                sleep(self._scan_time)

                        #Leitura de dados do tipo Float
                        elif tipo == '5':
                            addr = input(f'Digite o endereço da tabela MODBUS: ')
                            nvezes = input(f'Digite o número de vezes que deseja ler: ')
                            r = addr
                            for i in range(0,int(nvezes)):
                                float_l = self.lerdadofloat(int(tipo), int(addr))
                                r = float(float_l[0])
                                print(f'Leitura {i+1}: {r :.2f}')
                                sleep(self._scan_time)
                        #Observe que é feita uma conversão de dados antes da impressão do mesmo, isso porque os dados do tipo float voltam como lista, então precisamos converter para float para por fim usar :.2f para rrredondar o valor, caso isso não sejá feito o valor retorna diferente do registro original
                            
                    #Menu apenas para escrita de dados
                    elif sel == '2':
                        print('='*50)
                        tipo = input(f'Qual tipo de dado deseja Escrever? \n\r1- Resgistro Inteiro \n\r2- Registro Boleano \n\r3- Registro Float \n\rEscolha: ')

                        #Escrita de valores do tipo INT
                        if tipo == '1':
                            addr = input(f'Digite o endereço da tabela MODBUS: ')
                            valor = input(f'Digite o valor que vai ser escrito: ')
                            self.escreveDado(int(tipo),int(addr),int(valor))

                        #Escrita de valores do tipo Boleano
                        elif tipo == '2':
                            addr = input(f'Digite o endereço da tabela MODBUS: ')
                            valor = input(f'Digite o valor que vai ser escrito: ')
                            self.escreveDado(int(tipo),int(addr),int(valor))

                        #Escrita de valores do tipo Float
                        elif tipo == '3':
                            addr = input(f'Digite o endereço da tabela MODBUS: ')
                            valor = input(f'Digite o valor que vai ser escrito: ')
                            z = float(valor)
                            self.escreveDadoFloat(int(tipo),int(addr), [z])
                        #Aqui se o a var. valor já for do tipo Float da erro no registro, por isso a entrada é do tipo STR e convertida na var. z para Float.

                    #Menu apenas para alteração do tempo de leitura do servidor
                    #Por padrão vem com 1 segundo entre cada leitura, nesse menu pode mudar isso
                    elif sel == '3':
                        print('='*50)
                        scant = input('Digite o tempo de varredura em segundos \n\rTempo: ')
                        self._scan_time = float(scant)

                    #Menu exclusivo para encerrar o cliente
                    elif sel == '4':
                        self._client.close()
                        ate = False
                        print('='*50)
                        print('Cliente encerrado com sucesso')
                        print('='*50)

                    #Retorno caso escolha uma opção de número não registrado nos menus
                    else:
                        print('='*50)
                        print('Erro seletor escolhido invalido')

            #Aviso de erro do cliente quando não consegue se conectar ao servidor  
            else:
                print('Servidor não abriu')

        #Caso de algum erro mais grave esse comando vai informar um erro e o tipo do erro para correção
        except Exception as e:
            print('Erro: ',e.args)

    # --------------------------------------------------------------
    # ------------------- REGISTROS E LEITURAS ---------------------
    # --------------------------------------------------------------


    # Conjunto 1 - Leitura e escrita de dados do tipo inteiros e boleanos
    
    #Método para leitura de um dado que está no servidor (menu 1)
    def lerdado(self, tipo, addr):
        if tipo == 1:
            return self._client.read_holding_registers(addr,1)[0]
        if tipo == 2:
            return self._client.read_coils(addr,1)[0]
        if tipo == 3:
            return self._client.read_input_registers(addr,1)[0]
        if tipo == 4:
            return self._client.read_discrete_inputs(addr,1)[0]

    #Método para escrita de dados (menu 2)
    def escreveDado(self, tipo, addr, valor):
        if tipo == 1:
            return self._client.write_single_register(addr,valor)
        if tipo == 2:
            return self._client.write_single_coil(addr,valor)
        

    # --------------------------------------------------------------
    # --------------------------------------------------------------

    # Conjunto 2 - Leitura e escrita de dados do tipo float e dooble

    #Método para leitura de um dado que está no servidor (menu 1)   
    def lerdadofloat(self, tipo, addr, number=1):
        if tipo == 5:
            reg_l = self._client.read_holding_registers(addr, number * 2)
            if reg_l:
                return [utils.decode_ieee(f) for f in utils.word_list_to_long(reg_l)]
            else:
                return None
                #Esse none vai retornar em caso de erro e o valor do tipo Float não seja encontrado
              
    #Método para escrita de dados (menu 2)
    def escreveDadoFloat(self, tipo, addr, floats_list):
        if tipo == 3:
            b32_l = [utils.encode_ieee(f) for f in floats_list]
            b16_l = utils.long_list_to_word(b32_l)
            return self._client.write_multiple_registers(addr, b16_l)
    