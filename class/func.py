class Funcionario:
    def __init__(self, Nome, Salario):
        self.Nome = Nome
        self.Salario = Salario
    def aumentoSalario(self, porcent):
        self.Salario += self.Salario*(porcent/100)
        print(self.Salario)

nome = input(f"Digite seu nome: ")
salario = int(input(f"Digite seu salario: "))
porcent = int(input(f"Digite a porcentagem de aumento: "))

funcionario = Funcionario(nome, salario)
funcionario.aumentoSalario(porcent)