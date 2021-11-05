from pessoa import Pessoa
from produto import Produto

p1 = Pessoa('Luiz', 29)
p1.comer('maça')

p2 = Pessoa('Joao', 35)
p2.comer('melancia')

pr1 = Produto('CAMISETA', 50)
pr1.desconto(10)
print(pr1.nome, pr1.preco)

pr2 = Produto('Caneca', 'R$15')
pr2.desconto(10)
print(pr2.nome, pr2.preco)