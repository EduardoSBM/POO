class Personagem():
    def __init__(self, nome, musculos, velocidade, sabedoria):
        self.nome = nome
        self.musculos = musculos
        self.velocidade = velocidade
        self.sabedoria = sabedoria
        self.dano = 0

    def ataque(self):
        self.dano += 1

class Espartano(Personagem):
    def __init__(self, nome, musculos, velocidade, sabedoria):
        super().__init__(nome, musculos, velocidade, sabedoria)
        self.musculos = 2
        self.velocidade = 1
        self.sabedoria = 1

    def AtaquedoEspartano(self):
        for i in range (self.musculos):
            self.ataque()

class Suporte(Personagem):
    def __init__(self, nome, musculos, velocidade, sabedoria):
        super().__init__(nome, musculos, velocidade, sabedoria)
        self.musculos = 1
        self.velocidade = 1
        self.sabedoria = 2

    def AtaquedoSuporte(self):
        for i in range (self.sabedoria):
            self.ataque()
    
class Defesa(Personagem):
    def __init__(self, nome, musculos, velocidade, sabedoria):
        super().__init__(nome, musculos, velocidade, sabedoria)
        self.musculos = 1
        self.velocidade = 2
        self.sabedoria = 1

    def ForcaDefesa(self):
        for i in range (self.velocidade):
            self.ataque()

