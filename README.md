# Desafio Beck-end API <a id="titulo"></a>
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

## Índice <a id="indice"></a>
* [Título](#titulo)
* [Índices](#indice)
* [Descrição do Projeto](#descricao-do-projeto)
* [Executando a API](#executando-api)
* [Observações](#observacao)

## Descrição do Projeto <a id="descricao-do-projeto"></a>
Este projeto, trata-se de um desafio de construção de API que faça operações CRUD, tendo como modelo de metadados com os seguintes parâmetros:
   
    id - (string de 16 dígitos)
    name - (string)
    company - (string)
    created_at - (datetime)
    amount_products - (int)

Para o desinvolvimento do projeto foi utilizado o framework Django, mais especificamente sua extensão Django Rest Framework,
o formato de arquivo utilizado foi Json(JavaScript Object Notation), visto que é um formato de fácil manipulação e o mais utilizado atualmente,
no desenvolvimento do projeto foi utilizado também o Venv, ambiente virtual para o python, para executar localmente a API.

Como falado acima esta API retorna um Json, no seguinte formato: 
      
      {
         id: "TESTE000001TESTE"
         name: "Usertest1"
         company: "Companytest1"
         created_at: 2022-03-28
         amount_products: 1
      }
      

## Executando a API <a id="executando-api"></a>
  Antes de executar os comandos abaixo é necessário certificar que você tenha instalado o Python 3 em sua máquina, caso não tenha, você 
  pode instalar pelo seguinte link: https://www.python.org/downloads/, após instalar você pode se certificar que foi instalado corretamente
  pelo comando "python --version"
  
  ### Feito isso você pode seguir o passo a passo abaixo:
  
  -Clonar o repositorio
  
  -Abrir o repositorio com alguma IDE, recomendado VSCode
  
  -Após aberto o repositório executar no terminal da IDE o comando "python -m venv ./nomedoambientevirtual"
  
  -Após para ativar o ambiente virtual:
  
    No Linux e Mac: "source venv/bin/activate"
  
    NO windows pelo cmd: "cd nomedoambientevirtual/Scripts", após abrir a pasta Scripts "activate.bat"
  
    NO windows pelo shell: "cd nomedoambientevirtual/Scripts", após abrir a pasta Scripts "activate.ps1", pode ser necessário configurar o shell
  
  -Feito isso o ambiente virtual estará sendo executado, sendo assim volte a pasta api, e digite o comando "pip install -r requirements.txt"
  
  -Feito pode ser pedido para atualizar o pip
  
  -Após isso execute o comando "python manage.py makemigrations"
  
  -Em seguida digite "python manage.py migrate"
  
  -Feito tudo isso já é possível subir o servidor com o comando "python manage.py runserver"
  
  -Assim a API já estará rodando localmente, para testa-la voce pode abrir o navegador e digitar "http://localhost:8000/registros/"
  
  -Pode ser utilizado também a ferramenta Postman para verificar a API "https://www.postman.com/"
  
## Observações<a id="observacao"></a>

   *Este projeto foi feito com o objetivo de cumprir um desafio, sendo assim é importante ressaltar que esta API não deve ser utilizada para
   integração em outros projetos. Uma vez que ela se encontra em fase de protótipo e não está totalmente finalizada, como uma API profissional*
  
