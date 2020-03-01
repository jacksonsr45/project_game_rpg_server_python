# This is folder defoult fron init the new player. 
## Here builder tools stack from player by your class.

### *But has a file from defoult value!* 

- - 1º config_init_map.py for init value map.
- - 2º config_inventary.py for init value by inventary in player from your class.
- - 3º config_set_player.py define sutup initial by class for your player.
- - 4º config_skill_player.py define skills initial from your player for defoult the class.
- - 5º config_speel_player.py define speels from your player by defalt from class.
- - 6º config.py build informations in one file for export by class
- - 7º new_player.py this file has responsability from create new player by name user and build class inporting defoult values. 

---

#### Requereds from a new player

player_name < = > name from player 
player_world < = > world from player
player_type < = > type is a class from player
player_life < = > Total of te life inital from player
player_mana < = > Total mana of the initial from player
player_heal < = > Total of the heal initial from player
player_armor < = > Value of the armor from player
player_speels < = > Inital speels from player
player_skills < = > Initial skills from player
player_set < = > Initial sutup from player
player_init_map < = > Local initial from player in map
player_init_exp < = > Value by exp from player
player_inventary < = > Value inventary from player

---

```py
# config_init_map.py
new_init_map = {
    'class': { # <-- this is declared the class from player in initial map
        'pos_x': { # <-- this is declared the pos_x in map and other values by map from pos_x 

        },
        'pos_y': { # <-- this is declared the pos_y in map and other values by map from pos_y

        },
    },
}
```

```py
# config_inventary.py
new_inventary = {
    'class': { # <-- this is declared the class from player for init value inventary
        'value': 000, # <-- this is declared the value from initial inventary
        'object': { # <-- this is declared objects from inventary

        },
    },
}
```

```py
# config_set_player.py
new_set = {
    'class': { # <-- this is declared the class from player for setup initail from player
        'sword': {

        },
        'shielde': {

        },
        'helmet': {

        },
        'armor': {

        },
        'legs': {

        },
        'boots': {

        },
    },
}
```


```py
# config_skill_player.py
new_skill = {
    'class': { # <-- this is declared the class from player for skill initail from player
        'attack speed': {

        },
        'move speed': {

        },
        'attack distance': {

        },
        'defense': {

        },
        'magic attack': {

        },
        'dodge': {

        },
    },
}
```

```py
# config_spell_player.py
new_speel = {
    'class': { # <-- this is declared the class from player for speel initail from player
        'Q': {

        },
        'W': {

        },
        'E': {

        },
        'R': {

        },
    },
}
```


```py 
# config.py
values_init_player = {
    'player_class': { # <-- this is declared the class from player  type 
        'life': 000,# <-- this is declared the life from class  type 
        'mana': 000,# <-- this is declared the mana from class  type 
        'heal': 000,# <-- this is declared the heal from class  type 
        'armor': 000,# <-- this is declared the armor from class  type 
        'class_skills': new_skill['value'],# <-- this is declared the skill from class  type 
        'inventary': new_inventary['value'],# <-- this is declared the inventory from class  type 
        'class_set': new_set['value'],# <-- this is declared the setup from class  type 
        'class_init_map': new_init_map['value'],# <-- this is declared the initial map from class  type 
        'class_speels': {# <-- this is declared the speels from class  type 
                'speel_q': new_speel['value']['Q'],
                'speel_w': new_speel['value']['W'],
                'speel_e': new_speel['value']['E'],
                'speel_r': new_speel['value']['R'],
            },
    },
}
```