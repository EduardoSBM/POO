from ex3 import Suporte, Defesa, Espartano

beloni = Espartano('beloni', 3, 2, 1)
print(beloni.__dict__)
beloni.AtaquedoEspartano()
print(beloni.__dict__)

mari = Suporte('mari', 3, 2, 1)
print(mari.__dict__)
mari.AtaquedoSuporte()
print(mari.__dict__)

CristianePavei = Defesa('CristianePavei', 3, 2, 1)
print(CristianePavei.__dict__)
CristianePavei.ForcaDefesa()
print(CristianePavei.__dict__)