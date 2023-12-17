def verificar_produto(nome, arrayprodutos):
    for i in range (len(arrayprodutos)):
        if arrayprodutos[i] == nome:
            arrayprodutos.remove(i)
            return True
    else: 
        False

