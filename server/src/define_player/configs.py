__author__= "jacksonsr45@gmail.com"

from .config_set_player import new_set
from .config_speel_player import new_speel
from .config_inventary import new_inventary
from .config_skill_player import new_skill
from .config_init_map import new_init_map
from .config_init_exp import new_init_exp

""""
Configs from set values by init to player!
"""

values_init_player = {
    'player_knight': {
        'life': 750,
        'mana': 0,
        'heal': 2,
        'armor': 70,
        'knight_skills': new_skill['knight'],
        'inventary': new_inventary['knight'],
        'knight_set': new_set['knight'],
        'knight_init_map': new_init_map['knight'],
        'knight_exp': new_init_exp['knight'],
        'knight_speels': {
                'speel_q': new_speel['knight']['Q'],
                'speel_w': new_speel['knight']['W'],
                'speel_e': new_speel['knight']['E'],
                'speel_r': new_speel['knight']['R'],
            },
    },
    'player_mage': {
        'life': 150,
        'mana': 250,
        'heal': 8,
        'armor': 10,
        'mage_skills': new_skill['mage'],
        'inventary': new_inventary['mage'],
        'mage_set': new_set['mage'],
        'mage_init_map': new_init_map['mage'],
        'mage_exp': new_init_exp['knight'],
        'mage_speels': {
                'speel_q': new_speel['mage']['Q'],
                'speel_w': new_speel['mage']['W'],
                'speel_e': new_speel['mage']['E'],
                'speel_r': new_speel['mage']['R'],
            },
    },
    'player_paladin': {
        'life': 250,
        'mana': 100,
        'heal': 5,
        'armor': 20,
        'paladin_skills': new_skill['paladin'],
        'inventary': new_inventary['paladin'],
        'paladin_set': new_set['paladin'],
        'paladin_init_map': new_init_map['paladin'],
        'paladin_exp': new_init_exp['knight'],
        'paladin_speels': {
                'speel_q': new_speel['paladin']['Q'],
                'speel_w': new_speel['paladin']['W'],
                'speel_e': new_speel['paladin']['E'],
                'speel_r': new_speel['paladin']['R'],
            },
    },
    'player_ranger': {
        'life': 250,
        'mana': 50,
        'heal': 2,
        'armor': 20,
        'ranger_skills': new_skill['ranger'],
        'inventary': new_inventary['ranger'],
        'ranger_set': new_set['ranger'],
        'ranger_init_map': new_init_map['ranger'],
        'ranger_exp': new_init_exp['knight'],
        'ranger_speels': {
                'speel_q': new_speel['ranger']['Q'],
                'speel_w': new_speel['ranger']['W'],
                'speel_e': new_speel['ranger']['E'],
                'speel_r': new_speel['ranger']['R'],
            },
    },
}