# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class Smartphone():
	def __init__(self,tamanho, interface):
		self.tamanho = tamanho
		self.interface = interface


class MP3player(Smartphone):
	def __init__(self, capacidade, tamanho = 'pequeno', interface = 'LED'):
		self.capacidade = capacidade
		Smartphone.__init__(self, tamanho, interface)

	def imprimir(self):
		print('Valores para o objeto criado {} {} {}'.format(self.capacidade, self.tamanho, self.interface))

device1 = MP3player('64GB')

device1.imprimir()

