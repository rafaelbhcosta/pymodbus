# pymodbusTCP (client-server)
###### (Documentação básica)

![](https://logos-download.com/wp-content/uploads/2021/01/Modbus_Organization_Logo.png)

Olá sejá bem vindo(a)(x). Esse documento consiste em dois arquivos básicos para o funcionamento de um ModBus, que um servidor onde estamos gerando dados e um cliente onde estamos lendo esses dados.

Na dia a dia iremos usar apenas o cliente para fazer requisição e envio de dados para equipamentos de campo como: termometros, sensores, reguladores e outros.

## Sobre os arquivos:

+ Servidor: o servidor presente nesse arquivo tem como função gerar telemetrias falsas para que posamos usar 100% das funções do cliente, sua real função é simular um equipamento de campo gerando dados variaveis.

+ Cliente: é onde realmente trabalhamos com o ModBus, onde vamos realizar o envio e requisição de dados. Dentro do arquivo **servidormodbus.py** vamos encontrar o print de 3 linhas diferentes de uma tabela R1000, R2000, C3000.


### Nomenclaturas usadas
+ R: Usamos o R para simbolizar as linhas de registro do banco de dados (INT)

    + **R1000** - linha 1000 do banco de dados (registro de formato INT). Usando um gerador de números aleatórios para simular coleta de dados de um dispositivo de campo.

    + **R2000** - linha 2000 do banco de dados (registro de formato INT). Registo com valor nulo (0), sua função saber se o recebimento de dados (cliente -> servidor), está funcionando corretamente.

+ C: Usamos o C para simbolizar as linhas de coil do banco de dados (BOOLEAN)

    + **C3000** - linha 3000 do banco de dados (registro de formato BOOLEAN). Quando o servidor da start seu valor é nulo (0), ou seja, False. Ao sobre escrever essa linha com o valor um (1) ele é alterado para True.


    ## Garantindo o pleno funcionamento dos testes:

    Recomendamos que utize o VS Code para executar os arquivos e que abra uma janela para o cliente e uma janela para o servidor. 

    Cada arquivo vai consumir um console que ficara ativo constantemente, isso pode gerar limitações no VS Code, por esse motivo é recomendado que cliente e servidor sejam abertos em janelas difernetes.

    ###### Créditos:

    ###### ...........................

    ###### Desenvolvimento do arquivo:
    
    ###### Rafael Costa (Jr Data & IoT Enginer) [Linkedin](https://www.linkedin.com/in/rafaelbhcosta/)
    ###### Vinicius Rosa (Jr Data & IoT Enginer) [Linkedin](https://www.linkedin.com/in/vinicius-carvalho-rosa/)

    ###### ...........................

    ###### Resolução de Bugs e suporte dado a equipe:
    
    ###### Rodrigo Cruz (Senior Data & IoT Enginer) [Linkedin](https://www.linkedin.com/in/rodrigo-cruz-4b3142160/)