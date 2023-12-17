from flask import Flask, request, jsonify, render_template
import produto
import adicionarproduto
import removerproduto

app = Flask(__name__)


arrayprodutos = []

@app.route("/produto/adicionar/")
## /produto/adicionar?nome=alo&preco=300&quantidade=1000
def adicionar_produto():
    nome = request.args.get("nome",None)
    preco = request.args.get("preco",None)
    quantidade = request.args.get("quantidade", None)
    ##implementar função para verificar se todos os argumentos não são None


    ## crianda o objeto produtos e fazendo sua instancia local
    local_product = produto.Produto(len(arrayprodutos),nome,preco,quantidade)

    #adicionando o protudo em arrayprodutos na memoria
    adicionarproduto.adicionar_produto(local_product,arrayprodutos)

    print(arrayprodutos)

    return f"<h1>{nome,preco,quantidade}</h1>"

##criar a rota home que 

@app.route("/")
def index():
    return render_template("index.html",produtos=arrayprodutos)



@app.route("/produto/remover/")
def remover_produto():
    nome = request.args.get("nome",None)
    print(nome)
    if removerproduto.remover_produto(nome,arrayprodutos) == True:
        return f"Produto removido"
    else:
        return f"Esse produto não existe"

