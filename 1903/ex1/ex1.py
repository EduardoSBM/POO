class Funcionario:
    def __init__(self, Nome, Idade, salario ):
        self.Nome = Nome
        self.Idade = Idade
        self.salario = salario

    def calcularBonus(self, a):
        self.salario += a/100 * self.salario

    
class Gerente(Funcionario):
    def __init__(self, nome, Idade, salario):
        super().__init__(nome, Idade, salario)
        self.calcularBonus(5)


class Programador(Funcionario):
    def __init__(self, nome, Idade, salario):
        super().__init__(nome, Idade, salario)
        self.calcularBonus(3)

class Analista(Funcionario):
    def __init__(self, nome, Idade, salario):
        super().__init__(nome, Idade, salario)
        self.calcularBonus(1)

