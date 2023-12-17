def remover_produto(nome, arrayprodutos):
    print(f"{nome}1")
    for i in range (len(arrayprodutos)):
        print(arrayprodutos[i])
        if arrayprodutos[i].nome == nome:
            arrayprodutos.remove(arrayprodutos[i])
            return True
    else: 
        return False

