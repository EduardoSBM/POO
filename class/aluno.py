class Aluno:
    def __init__(self, Nome, Curso, TempoSemDormir ):
        self.Nome = Nome
        self.Curso = Curso
        self.TempoSemDormir = TempoSemDormir

    def estudar(self,QtdEst):
        self.TempoSemDormir = self.TempoSemDormir + QtdEst

    def Dormir(self,Qtdsono):
        self.QtdQtdsono = Qtdsono
        self.TempoSemDormir = self.TempoSemDormir - Qtdsono

dudu = Aluno("dudu", "informática", 12)
dudu.estudar(6) 
dudu.Dormir(8)
print(f"{dudu.TempoSemDormir}")