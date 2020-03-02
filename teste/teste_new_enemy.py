import os
import sys
path = '../server'
BASE_DIR = os.path.basename(path)
sys.path.append(BASE_DIR)

from src.define_enemies.new_enemy import New_Enemy

class TESTE_NEW_ENEMY:
    def __init__(self):
        add_enemy = {
            'class_name': 'wolf',
            'tier': 1,
        }

        new_enemy = New_Enemy(add_enemy)
        enemy = new_enemy.create_new_enemy()

        print(enemy)


if __name__ == "__main__":
    TESTE_NEW_ENEMY()