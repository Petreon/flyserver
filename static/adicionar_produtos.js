// adicionar_produtos.js

function realizarRequisicao() {
    // Capturar os valores dos inputs
    var nome = document.getElementById("nome").value;
    var preco = document.getElementById("preco").value;
    var quantidade = document.getElementById("quantidade").value;

    // Realizar a requisição usando fetch
    fetch(`http://192.168.1.21:5000/produto/adicionar/?nome=${nome}&preco=${preco}&quantidade=${quantidade}`)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error))
    .finally(() => console.log("fetch finalizado"))

}
