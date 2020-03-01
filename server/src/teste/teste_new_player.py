__author__ = "jacksonsr45@gmail.com"

from src.define_player.new_player import New_Player

knght = {
    'player_name': 'Jackson',
    'player_world': 'Lua',
    'player_type': 'KNIGHT',
}

new_knight = New_Player(knght)
player1 = new_knight.create_new_player()

print(player1)


mage = {
    'player_name': 'Amanda',
    'player_world': 'Sol',
    'player_type': 'MAGE',
}

new_knight = New_Player(mage)
player2 = new_knight.create_new_player()

print(player2)

paladin = {
    'player_name': 'Diego',
    'player_world': 'Sombrio',
    'player_type': 'PALADIN',
}

new_knight = New_Player(paladin)
player3 = new_knight.create_new_player()

print(player3)


ranger = {
    'player_name': 'Renata',
    'player_world': 'Ruinas',
    'player_type': 'RANGER',
}

new_knight = New_Player(ranger)
player4 = new_knight.create_new_player()

print(player4)