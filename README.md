# pymodbusTCP (client-server)
###### (Documentação básica)

Olá sejá bem vindo(a)(x). Esse documento consiste em dois arquivos básicos para o funcionamento de um ModBus, que um servidor onde estamos gerando dados e um cliente onde estamos lendo esses dados.

Na dia a dia iremos usar apenas o cliente para fazer requisição e envio de dados para equipamentos de campo como: termometros, sensores, reguladores e outros.

## Sobre os arquivos:

+ Servidor: o servidor presente nesse arquivo tem como função gerar telemetrias falsas para que posamos usar 100% das funções do cliente, sua real função é simular um equipamento de campo gerando dados variaveis.

+ Cliente: é onde realmente trabalhamos com o ModBus, onde vamos realizar o envio e requisição de dados. Dentro do arquivo **servidormodbus.py** vamos encontrar o print de 3 linhas diferentes de uma tabela R1000, R2000, C1000.


### Nomenclaturas usadas
