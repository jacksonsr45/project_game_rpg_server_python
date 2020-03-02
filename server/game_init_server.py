__author__ = "jacksonsr45@gmail.com"

from src.define_player.new_player import New_Player
from src.define_enemies.new_enemy import New_Enemy


class Main:
    def __init__(self):
        objects_server = {
            'new_player': New_Player,
            'new_enemy': New_Enemy,
        }
        

        
if __name__ == "__main__":
    Main()