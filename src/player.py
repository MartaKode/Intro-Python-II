# Write a class to hold player information, e.g. what room they are in
# currently.

# --> here will be the player class; attributes:  health, mana?, backpack?
class Player: 
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room