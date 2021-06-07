# Desafio Urbano

Este sistema é destinado ao desafio proposto pela Urbano Vitalino Advogados.

### Requisitos

Python 3.6 ou superior, Django 2.0 ou superior.

Para saber se já tem o python instalado no seu computador abra o terminal e digite python.
Se abrir o shell do python sem nenhum erro significa que o python já está instalado. Caso dê erro e o terminal informe que python não é reconhecido, é preciso instalar no site https://www.python.org/

Com o python instalado é só instalar o django utilizando o seguinte comando no terminal:
`pip install django`

### Executando

Para rodar o sistema e poder utilizar é só acessar o diretório do projeto pelo terminal e executar o comando `python manage.py migrate` para fazer as migrações necessárias do sistema e em seguida `python manage.py runserver`.
Pronto, agora é só acessar pelo navegador o seguinte caminho: `http://127.0.0.1:8000` e fazer o cadastro do processo na página como a da imagem abaixo:
![alt text](http://github.com/matheusfs99/desafio_urbano/blob/master/imgs/print.png?raw=true)


### Visualizando os processos cadastrados

Para visualizar os dados é preciso criar inicialmente um usuário. Para isso você precisa, pelo terminal, digitar o comando `python manage.py createsuperuser` e informar seu username, email e senha.
Feito isso, é só rodar novamente o sistema e acessar a rota admin, ou seja, o caminho `http://127.0.0.1:8000/admin` e fazer login com seu username e senha cadastrado.
No admin, é só clicar no modelo desejado, Cadastro_Processo ou Processo, que vai listar todos os registros salvos.
![alt text](http://github.com/matheusfs99/desafio_urbano/blob/master/imgs/print2.png?raw=true)
![alt text](http://github.com/matheusfs99/desafio_urbano/blob/master/imgs/print3.png?raw=true)