# Implement a class to hold room information. This should have name and
# description attributes.

# room class -> items? monsters? dark/cant see?
class Room:
    def __init__(self, name, description, items= []):
        self.name = name
        self.description = description
        
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        
        self.items = items

    def __str__(self):
        # return f'Name: {self.name}, Description: {self.description}, Items: {[item for item in self.items]}'
        return f'Name: {self.name}, Description: {self.description}, Items: {self.items}'
    
    def print_items(self):
        # print("Items on the floor: ",[f'{item.name}: {item.description}' for item in self.items], '\n' )
        for id, i in enumerate(self.items):
            print(f'{i}')
        print() # -> formating ; extra empty line
        
    def print_item_name(self):
        for  item in self.items:
            print(item.name)
        # return self.items.name
    
    def remove_item(self, item):
        self.items.remove(item)
    
    def add_item(self, item):
        self.items.append(item)