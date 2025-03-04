###### Dia 26/02
O design de código nos ensina a deixar o código mais limpo, e eu certamente irei utilizar isso. Hoje vimos que é sempre bom inferir tipos de retorno nas funções ou parâmetros. Também aprendemos que é bom encapsular métodos dentro de classes, pois isso deixa o nosso código mais organizado.

###### Dia 27/02
Criamos pastas, e sempre que criarmos pastas é importante criarmos arquivos __init__.py, pois isso facilita a importação de um arquivo para outro.

###### Dia 28/02 
Criamos a nossa primeira calculadora, aplicando boas práticas de design de código e a testamos no Postman. Também fizemos a introdução ao pytest (novamente).

###### Dia 01/03
Terminamos os testes unitários na calculadora1, iniciamos a calculadora2, passando todas as bibliotecas externas para drivers e criando um "façade". Toda vez que formos instalar uma biblioteca externa, ela terá que passar pelos drivers, onde faremos o "façade". Instalamos uma nova biblioteca chamada numpy, que recebe N números e faz a derivação de números.

###### Dia 02/03
Terminamos os testes de integração na calculadora 2, aprendemos mais sobre interfaces e como elas funcionam no Python. Elas são bem parecidas com as do TypeScript. Vimos a injeção de dependências e herança, finalizando assim a calculadora 2.

###### Dia 04/03
Demos início à calculadora 3, onde tivemos que adicionar um método da biblioteca numpy chamado `variance`. Fizemos a calculadora e o teste dela, utilizando um único mock de `variance`, sem usar o `NumpyHandler`. Depois, adicionamos na rota. Após isso, criamos nossos erros personalizados (que ficaram muito bons) e os adicionamos nas rotas de todas as calculadoras.