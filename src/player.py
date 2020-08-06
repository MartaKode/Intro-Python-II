# Write a class to hold player information, e.g. what room they are in
# currently.

# --> here will be the player class; attributes:  health, mana?, backpack?
class Player: 
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

        self.item_backpack = []
    
    def get_item(self, item):
        self.item_backpack.append(item)
        print(f'\nYou have successfully picked up {item.name}')
        print('Your backpack contains: ', [f'{item.name} , {item.description}' for item in self.item_backpack])
    
    def drop_item(self, item):
        self.item_backpack.remove(item)
        print(f'\nYou have successfully dropped {item.name}')
        print('Your backpack contains: ', [f'{item.name} , {item.description}' for item in self.item_backpack])
        
    def open_backpack(self):
        print([f'{item.name}: {item.description}' for item in self.item_backpack])
