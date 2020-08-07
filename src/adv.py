from room import Room
from player import Player
from item import Item

import textwrap

# Declare all the rooms

room = {  # can modify
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('Spoon', 'A metal spoon, might it have a use aside of enjoying a bowl of soup? Who knows.'), Item('Umbrella', 'An umbrella that can protect you from rain'), Item('Butter_Knife', 'Not sharp, perfect for for spreading, not so much for stabbing')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('Sword', 'Sharp, heavy, and powerful!'), Item('Puppy', 'It looks so cute...look at those eyes! How can you leave it behind?!')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('Key', 'A golden key; It must be able to open something!'), Item('Shovel', 'a solid shovel, can be used to dig through the ground')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('Gold', 'A solid chunk of gold. That must be worth some money!'), Item('Pickaxe', 'Useful to destroy stones and look through cave walls')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('Chest', 'Empty treasure chest'), Item('Coin', 'A silver coin'), Item('Note', 'There is no way out...There is no way out! Unless you know a way to dig under walls...')]),
}



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

''''Helpers'''
def show_welcome_message():
    welcome_message = "Welcome, let's start an adventure!🐲\n"
    print(welcome_message)

def show_info_message(name):
    while True:
        if len(name) > 0:
            info_message = f'\n🎇✨Hello {name}!🧙 Your adventure begins here! Navigate to different rooms to progress. Have fun!✨🎇\n'
            print(info_message)
            break
        else:
            print('⚠️  Please provide an adventurer name⚠️')
            name = input('Type out youe name: \n>>  ')
            # break
#
# Main
#
''''Starting the Game:'''
def adventure_game():
    show_welcome_message()
    player_name = input('Choose your adventurer name: \n >>  ')
    # print(room['outside'].name)
    show_info_message(player_name)

    # Make a new player object that is currently in the 'outside' room.
    player = Player(player_name, room['outside'])
    # print(player.current_room.name)

    # Write a loop that:
    while True:
        #
        # * Prints the current room name
        # print(player.current_room)
        print(f'\nYou are currently at "{player.current_room.name}".')
        # * Prints the current description (the textwrap module might be useful here).
        print(textwrap.dedent(player.current_room.description), '\n')
        
        player.current_room.print_items()
        # player.current_room.print_item_name()
        # '''' Let the player pick up items or move on to the next room'''''
        print(f'Do you wish to pick up any of the items? \n')
        take_items = [f'[take {item.name}]' for item in player.current_room.items]
        
        def take_command(take_items):
            for i in take_items:
                print(i)
            return 'Type out one of those take commands below or type [pass] to move on'
        
        drop_items = [f'[drop {item.name}]' for item in player.item_backpack]
        def drop_command(drop_items):
            for i in drop_items:
                print(i)
            return ' '
        
        item_command = input(f"{take_command(take_items)} {drop_command(drop_items)} \n >>  ").lower().split(' ')
        # print(item_command)
        
        if item_command[0] == 'pass':
            pass
        elif item_command[0] == 'take' or item_command[0] == 'get':
            for item in player.current_room.items:
                if item_command[1] == item.name.lower():
                    player.get_item(item)
                    player.current_room.remove_item(item)
                    break
                elif item_command[1] not in player.current_room.items:
                    print('That item is not in this room! You can come back here later and try again')
                    # item_command = input().lower().split(' ')
                    break
        elif item_command[0] == 'drop' or item_command[0] == 'leave':
            for item in player.item_backpack:
                if item_command[1] == item.name.lower():
                    player.drop_item(item)
                    player.current_room.add_item(item)
                    break
                elif item_command[1] not in player.item_backpack:
                    print('wrong command, or the items is already gone? Try again!')
                    break
        else:
            print("\nWrong command, let's try that again...")
            continue

        ''''''''''''''''''''''''''''''''''''''''''''''''
        # * Waits for user input and decides what to do.
        #
        print("\nWhere do you go next?")
        command = input("[n] north   [s] south   [e] east    [w] west   [i] open inventory    [q] quit\nyour choice >>  ")

        # If the user enters a cardinal direction, attempt to move to the room there.
        # Print an error message if the movement isn't allowed.
        #
        # If the user enters "q", quit the game.
        # command = input(">Make a ").split(',')

        if command == 'q':
            break

        elif command[0] == 'n':
            # check if the player can move to the north 
            # if there is, set that north room as the player's location 
            if player.current_room.n_to:
                player.current_room = player.current_room.n_to
            # except (NameError, AttributeError):
            else:
                print(f'\n****🚫 There is no rooms to the north of "{player.current_room.name}". Try a different path!⛔️ ***\n')
                continue

        elif command[0] == 's':
            if player.current_room.s_to:
                player.current_room = player.current_room.s_to
            else:
                print(f'\n****🚫 There is no rooms to the south of "{player.current_room.name}". Try a different path!⛔️ ***\n')
                continue

        elif command[0] == 'e':
            if player.current_room.e_to:
                player.current_room = player.current_room.e_to
            # except (NameError, AttributeError):
            else:
                print(f'\n****🚫 There is no rooms to the east of "{player.current_room.name}". Try a different path!⛔️ ***\n')
                continue

        elif command[0] == 'w':
            if player.current_room.w_to:
                player.current_room = player.current_room.w_to
            # except (NameError, AttributeError):
            else:
                print(f'\n****🚫 There is no rooms to the west of "{player.current_room.name}". Try a different path!⛔️ ***\n')
                continue

        elif command[0] == 'i' or command[0] == 'inventory':
            player.open_backpack()

            backpack_choice = input('Drop [drop] items or continue [pass] \n>>  ')
            if backpack_choice == 'pass':
                pass
            elif backpack_choice == 'drop':
                drop_items = [f'[drop {item.name}]' for item in player.item_backpack]
                def drop_command(drop_items):
                    for i in drop_items:
                        print(i)
                        
                drop_command(drop_items)
                choice = input('>>  ').lower().split(' ')
                if choice[0] == 'drop':
                    for item in player.item_backpack:
                        if choice[1] == item.name.lower():
                            player.drop_item(item)
                            player.current_room.add_item(item)
                            break
                        elif choice[1] not in player.item_backpack:
                            print('No such item in your backpack. Moving on..')
                            break
                else:
                    pass
            else: 
                pass

        else:
            print(f'\n****⚠️  Wrong command: "{command}"...Try again?⚠️  ****\n')



if __name__ == '__main__':
  adventure_game()



'''''''''''''''''''🍝 Spaghetti code '''''''''''''''''''

             

 
        # for item in player.current_room.items:
        #     if item_command == f'take {item.name.lower()}' or item_command == f'get {item.name.lower()}':
        #         player.get_item(item)
        #         player.current_room.remove_item(item)
        #         break
        #     elif item_command == 'pass':
        #         break
        #     elif item_command not in player.current_room.items:
        #         print('wrong command, or the items is already gone? Try again!')
        #         # item = input()
        #         # continue
        # for item in player.item_backpack:
        #     if item_command == f'drop {item.name.lower()}' or item_command == f'leave {item.name.lower()}':
        #         player.drop_item(item)
        #         player.current_room.add_item(item)
        #         break
        #     elif item_command == 'pass':
        #         break
            # else:
            #     print('wrong command, or the items is already gone? Try again!')
            #     item = input()
            #     continue

        # possible_items = player.current_room.items
        
        # selected_item = possible_items[item_command]
        
        # player.get_item(selected_item)