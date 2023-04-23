# ProjetoDimDimDockerCompose

# Como clonar o repositório:

Vá em "Code" e selecione a opção de copiar o link deste repositório.
![Captura de tela 2023-04-16 153601](https://user-images.githubusercontent.com/100175547/232334382-c36d86b5-7845-41cc-b5ba-394d9ab9512c.png)
---------------------------------------------------
Abra o Visual Studio Code e cole o link do repositório na aba "Clone Repository", que fica ao lado esquerdo do software.
![Captura de tela 2023-04-16 153851](https://user-images.githubusercontent.com/100175547/232334554-40d769dc-9779-4206-8e95-f700d4754a93.png)
-----------------------------------------------------
# Desenvolvimento do projeto:

1 - Descrição do projeto e objetivos:
O projeto Dimdim é uma aplicação de gerenciamento financeiro pessoal, com o objetivo de auxiliar os usuários a controlar seus gastos e receitas de forma eficiente. A aplicação permitirá o cadastro de transações financeiras, categorização das transações, visualização de relatórios e gráficos, e terá funcionalidades de CRUD (Create, Read, Update, Delete) para as transações e categorias. O projeto será desenvolvido como um conjunto de microserviços utilizando Docker e Docker Compose para facilitar o gerenciamento dos containers.

 

2 - Arquitetura do projeto:
A arquitetura do projeto Dimdim será composta por dois microserviços: um serviço de API e um serviço de banco de dados para persistência dos dados. A API será responsável por receber as requisições dos usuários, processar as transações e categorias, e fornecer as respostas adequadas. O banco de dados será utilizado para armazenar as transações, categorias e outras informações relevantes. A API e o banco de dados serão containers Docker separados, com uma rede Docker para comunicação entre eles.

 

3 - Serviços e recursos no Docker Compose:
O Docker Compose será utilizado para orquestrar os containers Docker do projeto Dimdim. Serão definidos dois serviços no Docker Compose: um serviço para a API e outro serviço para o banco de dados. O serviço da API será baseado em uma imagem Docker de uma linguagem de programação/framework específico para o desenvolvimento da API, como Node.js, Flask ou Django. O serviço do banco de dados será baseado em uma imagem Docker de um banco de dados adequado para a aplicação, como MySQL, PostgreSQL ou MongoDB. Será utilizado um volume Docker para persistência dos dados do banco de dados, garantindo que os dados sejam mantidos mesmo que o container seja reiniciado.

 

4 - Imagens adequadas:
Serão utilizadas imagens Docker adequadas para um melhor desempenho e menor tamanho dos containers. Será dada preferência para imagens baseadas em Python e mysql, que são conhecidas por serem leves e enxutas, para reduzir o tamanho dos containers e diminuir o tempo de download e execução dos containers.

 

5 - Não utilizar usuário root:
Será criado um novo usuário no Dockerfile para executar o projeto Dimdim, evitando a utilização do usuário root nos containers Docker. Isso contribuirá para a segurança do projeto, minimizando a exposição a possíveis vulnerabilidades relacionadas à execução de processos como root.

 

6 - Utilização de diretório padrão:
Será definido um diretório padrão dentro dos containers para a execução do projeto Dimdim. Isso facilitará o gerenciamento dos arquivos e a organização dos recursos dentro dos containers, tornando mais fácil a manutenção e atualização do projeto.

 

7 - Informação de qualidade:
Os dados utilizados nos testes e nas transações da aplicação serão escolhidos de forma a fazer sentido em relação ao tema do projeto Dimdim. Serão evitados dados genéricos como "teste 123" ou "produto 1", e serão utilizados dados reais ou fictícios que estejam relacionados com as transações financeiras, categorias e relatórios gerados pela aplicação.

 

8 - Análise dos Containers pelo Terminal:
Serão utilizados comandos no terminal do host para entrar nos terminais dos containers, permitindo verificar os processos.
