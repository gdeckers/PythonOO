# from pessoa import Pessoa
# from produto import Produto
#
# p1 = Pessoa('Luiz', 29)
# p1.comer('maça')
#
# p2 = Pessoa('Joao', 35)
# p2.comer('melancia')
#
# pr1 = Produto('CAMISETA', 50)
# pr1.desconto(10)
# print(pr1.nome, pr1.preco)
#
# pr2 = Produto('Caneca', 'R$15')
# pr2.desconto(10)
# print(pr2.nome, pr2.preco)

# from BaseDados import BaseDeDados
#
# bd = BaseDeDados()
#
# bd.inserir_cliente(1, 'José')
# bd.inserir_cliente(2, 'João')
# bd.inserir_cliente(3, 'Maria')
# bd.lista_clientes()

from classes import CarrinhoCompra, Produto

carrinho = CarrinhoCompra()

p1 = Produto('Camiseta Preta', 15)
p2 = Produto('Camiseta Branca', 15)
p3 = Produto('Tenis', 120)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)

carrinho.listar_produto()
print(carrinho.soma_total())