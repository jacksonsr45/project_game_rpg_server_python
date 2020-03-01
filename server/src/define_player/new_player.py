__author__ = "jacksonsr45@gmail.com"

from .configs import values_init_player as set_player

class New_Player:
    def __init__(self, new_player):
        self.player_name = new_player['player_name']
        self.player_world = new_player['player_world']
        self.player_type = new_player['player_type']
        


    def create_new_player(self):
        if self.player_type == 'KNIGHT':
            self.value_life = set_player['player_knight']['life']
            self.value_mana = set_player['player_knight']['mana']
            self.value_heal = set_player['player_knight']['heal']
            self.value_armor = set_player['player_knight']['armor']
            self.value_speels = set_player['player_knight']['knight_speels']
            self.value_skills = set_player['player_knight']['knight_skills']
            self.value_set = set_player['player_knight']['knight_set']
            self.value_init_map = set_player['player_knight']['knight_init_map']
            self.value_inventary = set_player['player_knight']['inventary']
        elif self.player_type == 'MAGE':
            self.value_life = set_player['player_mage']['life']
            self.value_mana = set_player['player_mage']['mana']
            self.value_heal = set_player['player_mage']['heal']
            self.value_armor = set_player['player_mage']['armor']
            self.value_speels = set_player['player_mage']['mage_speels']
            self.value_skills = set_player['player_mage']['mage_skills']
            self.value_set = set_player['player_mage']['mage_set']
            self.value_init_map = set_player['player_mage']['mage_init_map']
            self.value_inventary = set_player['player_mage']['inventary']
        elif self.player_type == 'PALADIN':
            self.value_life = set_player['player_paladin']['life']
            self.value_mana = set_player['player_paladin']['mana']
            self.value_heal = set_player['player_paladin']['heal']
            self.value_armor = set_player['player_paladin']['armor']
            self.value_speels = set_player['player_paladin']['paladin_speels']
            self.value_skills = set_player['player_paladin']['paladin_skills']
            self.value_set = set_player['player_paladin']['paladin_set']
            self.value_init_map = set_player['player_paladin']['paladin_init_map']
            self.value_inventary = set_player['player_paladin']['inventary']
        elif self.player_type == 'RANGER':
            self.value_life = set_player['player_ranger']['life']
            self.value_mana = set_player['player_ranger']['mana']
            self.value_heal = set_player['player_ranger']['heal']
            self.value_armor = set_player['player_ranger']['armor']
            self.value_speels = set_player['player_ranger']['ranger_speels']
            self.value_skills = set_player['player_ranger']['ranger_skills']
            self.value_set = set_player['player_ranger']['ranger_set']
            self.value_init_map = set_player['player_ranger']['ranger_init_map']
            self.value_inventary = set_player['player_ranger']['inventary']

        create_new = {
            'player_name': self.player_name,
            'player_world': self.player_world,
            'player_type': self.player_type,
            'player_life': self.value_life,
            'player_mana': self.value_mana, 
            'player_heal': self.value_heal,
            'player_armor': self.value_armor,
            'player_speels': self.value_speels,
            'player_skills': self.value_skills,
            'player_set': self.value_set,
            'player_init_map': self.value_init_map,
            'player_inventary': self.value_inventary,
        }
        return create_new