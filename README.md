# Bancos

Catálogo de bancos associados a seus respectivos códigos de compensação.

Interface da aplicação: https://heldersrvio.github.io/Bancos/

## Back-end

O *back-end* da aplicação foi programado com o *framework* [Flask](https://flask.palletsprojects.com/en/2.0.x/) e a linguagem Python. O código-fonte encontra-se no diretório *back-end*.

O arquivo *initializeDatabase.py* não é executado em resposta a nenhuma consulta feita ao *back-end* — ele foi executado apenas uma vez para inicializar o banco de dados e seu propósito é criar no banco de dados MySQL uma tabela BANCOS e inserir nela os nomes e os códigos das instituições presentes no arquivo bancos.xls. Para a leitura do arquivo .xls, foi utilizada a biblioteca [xlrd](https://xlrd.readthedocs.io/en/latest/#) e, para a conexão com o banco, o driver [MySQL Connector Python](https://dev.mysql.com/doc/connector-python/en/).

*db.py* configura o banco de dados a ser utilizado pela aplicação com base nas variáveis de configuração, usando, para isso, a extensão [flask-mysql](https://flask-mysql.readthedocs.io/en/stable/).

Por fim, *main.py* define as rotas e as respostas JSON para a aplicação especificada em *app.py*. Um método GET na rota '/banklists' retorna um arquivo .json com um atributo 'list', cujo valor associado é um Array de Strings, representando os nomes de todos as instituições no banco de dados. Já a rota '/bankname/<bank_code>' retorna um .json com um atributo 'name' e o nome do banco associado ao código passado como parâmetro, caso existir, ou *null*, caso contrário.

O *back-end* foi hospedado por meio do serviço [Heroku](https://heroku.com).

## Front-end

Utilizou-se o *framework* [Angular](https://angular.io) para desenvolver o *front-end* da aplicação. A interface conta com duas áreas: a área de listagem de todos os bancos (implementada pelo componente 'bank-list-display') e a área de pesquisa de um determinado banco pelo código de compensação (implementada pelo componente 'bank-search').

O *deploy* do *front-end* foi feito com o [GitHub Pages](https://pages.github.com) e pode ser acessado [aqui](https://heldersrvio.github.io/Bancos/).