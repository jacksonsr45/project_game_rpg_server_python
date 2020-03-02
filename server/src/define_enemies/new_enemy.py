__author__ = "jacksonsr45@gmail.com"

from .mountain_wolf import new_mountain_wolf
from .forest_orcs import new_forest_orcs

class New_Enemy:
    def __init__(self, new_enemy):
        self.enemy_name = new_enemy['class_name']
        self.enemy_tier = new_enemy['tier']

        self.enemies = {
            'wolf': new_mountain_wolf,
            'orcs': new_forest_orcs,
        }

        

    def create_new_enemy(self):
        add_enemy = self.enemies[f'{self.enemy_name}'][f'{self.enemy_tier}']
        return add_enemy