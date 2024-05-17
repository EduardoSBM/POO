class Livro:
    def __init__(self, Nome, Qtdpag, Autor, Preco):
        self.Nome = Nome
        self.Qtdpag = Qtdpag
        self.Autor = Autor
        self.Preco = Preco

    def getPreco(self):
        print(f"{self.Preco}")

    def setPreco(self, Preco2):
        self.Preco = Preco2

nome = input(f"Digite seu nome: ")
Qtdpag = int(input(f"Digite a quantidade de páginas: "))
Autor = input(f"Digite o nome do autor do livro: ")
Preco = int(input(f"Digite o Preço do livro: "))

liv = Livro(nome, Qtdpag, Autor, Preco)
liv.getPreco()
Preco2 = int(input(f"Digite o novo Preço do livro: "))
liv.getPreco()
print(f"{Preco2}")


