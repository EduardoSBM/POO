class Pessoa:
    def __init__(self, altura, idade):
        self.altura = altura
        self.idade = idade

class Aluno:
    def __init__(self, altura, idade):
        self.altura = altura
        self.idade = idade

    @classmethod
    def construir_aluno_pessoa(cls, pessoa):
        return cls(pessoa.altura ,pessoa.idade)
    
    def estudar(self):
        print("estou estudando")

joao = Pessoa(1.85, 35)
MariaAluna = Aluno(1.90,15)
MariaAluna.estudar()

joaoAluno = Aluno.construir_aluno_pessoa(joao)
joaoAluno.estudar()