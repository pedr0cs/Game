from classes import *

def main(player, enemy):
    while enemy.position > 0:
        enemy.position -= 1
        print(f"{enemy.nome} se moveu para a posição {enemy.position}")
        if enemy.position <= 3:
            enemy.hp -= player.dano
            print(f"{enemy.nome} tem {enemy.hp} HP")
            if enemy.hp <= 0:
                print(f"{enemy.nome} foi derrotado.")
                break   

if __name__ == "__main__":
    main(Player(), Enemy())