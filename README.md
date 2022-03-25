# PyModbus<br>(client-server)

<img src="https://logos-download.com/wp-content/uploads/2021/01/Modbus_Organization_Logo.png" alt="logo do modbus">

###### (Documentação básica do repositório)

<br>

Olá, seja bem vindo(a)(x). <br>
Esse documento consiste em um material básico para introdução a biblioteca pymodbus.

#

### Programas recomendados
<div>
    <img height="30" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" /> ou  
    <img height="30"src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pycharm/pycharm-original.svg" />
</div>
Particularmente preferimos usar o vscode por ter mais ferramentas, e como usamos uma VM do Azure o vscode também fornece suporte para uma conexão direta e controle da VM por ele mesmo.

#

### Observações

Existem duas formas de estudar o protocolo ModBus, que é pela biblioteca pymodbusTCP ou a pymodbus. 

* A biblioteca pymodbusTCP é bastante limitada para ler informações, ela vai servir básicamente para leituras de INT, BOOLEAN e FLOAT.
* A biblioteca pymodbus é a mais completa podendo ler até mesmo STR e valores alfanuméricos, fora que seu código é mais resumido e simples.

#

### Pastas

Nesse repositório estamos colocando um modelo TCP apenas para fins de comparação entre os códigos, reforçando o que foi dito que recomendamos apenas a pymodbus.

* OBS: mesmo que o servidor de um cliente seja do modelo pymodbusTCP a biblioteca pymodbus faz as leituras sem problemas, apenas vai ser preciso configurar o cliente para leituras do tipo 32 BIT.

Dentro de cada pasta poderá ser encontrado instruções de como funciona cada documento. É recomendado que para simular o servidor seja usado um simulador de servidor Modbus da empresa [Elipse Software](https://www.elipse.com.br/downloads/), que deve ser baixado no site da mesma.

#

###### Créditos:

###### ...........................

###### Desenvolvimento do arquivo:

###### Rafael Costa (Jr Data & IoT Enginer) [Linkedin](https://www.linkedin.com/in/rafaelbhcosta/)
###### Vinicius Rosa (Jr Data & IoT Enginer) [Linkedin](https://www.linkedin.com/in/vinicius-carvalho-rosa/)

###### ...........................

###### Supervisão, resolução de Bugs e suporte dado a equipe:

###### Rodrigo Cruz (Senior Data & IoT Enginer) [Linkedin](https://www.linkedin.com/in/rodrigo-cruz-4b3142160/)