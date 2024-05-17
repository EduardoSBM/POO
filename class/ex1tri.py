class Triangulo:
    def __init__(self, LadoA, LadoB, LadoC):
        self.LadoA = LadoA
        self.LadoB = LadoB
        self.LadoC = LadoC

    def calcularPerimetro(self):
        print(self.LadoA + self.LadoB + self.LadoC)

    def maior(self):
        if self.LadoA > self.LadoB and self.LadoA > self.LadoC:
            print(f"Lado A é o maior!")
        elif self.LadoB > self.LadoA and self.LadoB > self.LadoC:
            print(f"Lado B é o maior!")
        else:
            print(f"Lado C é maior!")

A = float(input(f"Digite o valor do lado A: "))
B = float(input(f"Digite o valor do lado B: "))
C = float(input(f"Digite o valor do lado C: "))
T = Triangulo(A,B,C)

print(T.calcularPerimetro())
print(T.maior())

################################################################################# o do sor é o de baixo

class Triangulo:
    def __init__(self, LadoA, LadoB, LadoC):
        self.LadoA = LadoA
        self.LadoB = LadoB
        self.LadoC = LadoC

    def calcularPerimetro(self):
        print(self.LadoA + self.LadoB + self.LadoC)

    def getMaiorlado(self):
        print(max(self.LadoA, self.LadoB, self.LadoC))
    
    def calcularArea(self):
        print((self.LadoB)/2)

a = float(input(f"Digite o valor do lado A: "))
b = float(input(f"Digite o valor do lado B: "))
c = float(input(f"Digite o valor do lado C: "))

meuTriangulo = Triangulo(a, b, c)
meuTriangulo.calcularArea()
meuTriangulo.getMaiorlado()
meuTriangulo.calcularPerimetro()