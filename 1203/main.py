from funcionario import Funcionario

joao = Funcionario("joao","gari",55)
print(joao.__dict__)
joao.salario = 1000
print(joao.__dict__)
