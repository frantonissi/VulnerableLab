from flask import Flask, render_template, request #importa a classe Flask que vai ser usada para implementar o servidor web

app = Flask(__name__)  #- Flask(__name__) cria a aplicação usando o nome do módulo Python atual como referência.
                       #Cria a instância da aplicação. O __name__ informa ao Flask o nome do módulo Python atual, 
                       #ajudando o framework a localizar recursos da aplicação.

@app.get("/") #É um decorador que associa a rota / a uma função que responde a requisições HTTP do tipo GET. (basicamente, se procurar apenas o diretorio /, ele retorna a funcao inicio)
def inicio(): #Função do python que vai ser executada quando alguem acessar essa rota
    return "<h1>VulnerableLab</h1><p>Meu laboratório de segurança web.</p>"

@app.get("/sobre") #decorador que associa a rota /sobre
def sobre():
    return "<h1>Sobre o meu projeto: </h1><p>Esse é um projeto desenvolvido por Francisco Tóro Tonissi que tem o intuito de mostrar no mundo real vulnerabilidades listadas pela OWASP e também como mitiga-las, fique a vontade para usa-lo para estudos o tanto que desejar</p>", 200
    #O Flask permite retornar  dois valores, o corpo da resposta em HTML e o código de status HTTP (200, 201, etc)
    #mas tem que ver se faz sentido, pq por exemplo, o 201 que indica que deu certo e algo foi construido, deve
    #ser usado principalmente com POST, GET serve para consultar recursos, nao crialos


@app.get("/formulario") #adiciona o diretorio com o decorador
def mostrar_formulario():
    return render_template("formulario.html") #o render_template serve para fazer o flask procurar dentro da pasta template os arquivos .html
    
@app.post("/formulario")
def receber_informacao():
    nome = request.form.get("nome")
    return render_template("resultado.html", nome = nome) #O primeiro nome define o nome pelo qual o HTML conhecerá a variável. o segundo nome representa a variável Python que contém o valor recebido.

   

