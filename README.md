--------------Python Setup after cloning ----------
após clonar você vai querer usar 
1 - python3 -m venv venv -> criar o ambiente virtual "https://docs.python.org/pt-br/3/library/venv.html"
2 - . .\venv\Scripts\activate -> acessar o ambiente virtual
3 - .\venv\Scripts\pip3 install -r requirements.txt -> instalar as dependências do projeto 

--------------DATABASE Explanation----------
para usar você teria que criar uma pasta na Pasta raiz "./MySql/mysql_data_volume:/var/lib/mysql" pasta seria essa "MySql" quando você rodar o "docker-compose up -d" 
ele vai criar a estrutura la dentro do mysql e tudo basta acessar seu "MySQL Workbench", ou outro jeito de acessar uma interface grafica para ver o banco de dados MySQL
dentro de init/schema.sql -> tem as tabelas

--------------------------------------------
Esse projeto é em conjunto com o projeto que está no meu repository "https://github.com/augustocesarsouza/Frontend-Ingresso", Python é o Backend
