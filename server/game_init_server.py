__author__ = "jacksonsr45@gmail.com"

from src.define_player.new_player import New_Player
from src.teste import teste_new_player

class Main:
    def __init__(self):
        server = {
            'new_player': New_Player,
            'teste_new_player': teste_new_player,
        }

        
if __name__ == "__main__":
    Main()