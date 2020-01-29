# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

class Pessoa():
    def __init__(self,nome,cidade,telefone,email):

        print('Pessoa criada')
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return 'Meu nome é {}, sou de {}, meu telefone é {}, meu email é {}'.format(self.nome, self.cidade, self.telefone, self.email)
    
pessoa1 = Pessoa('Gabriel', 'Rio de Janeiro', 21924589674, 'gabrielnascimento@hotmail.com')

print(str(pessoa1))
