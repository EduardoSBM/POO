class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada ):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__horas_trabalhadas = 0
        self.__salario = 0


    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, __novo_salario):
        raise ValueError("impossivel alterar o saario diratamente, use a metedo")


    def registrar_hora_rabalhada(self):
        self.__horas_trabalhadas += 1

    def Dormir(self):
        self.salario = self.valor_hora_trabalhada * self.__horas_trabalhadas