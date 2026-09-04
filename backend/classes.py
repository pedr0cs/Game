class Player :
    def __init__(self): 
        self.nome = input("Digite o nome do jogador: ")
        self.dano = 50
        self.position = 0

class Enemy :
    def __init__(self):
        self.nome= "Aranha"
        self.hp = 100
        self.position = 10
