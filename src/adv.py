from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {  # can modify
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
    welcome_message = "Welcome, let's start an adventure!"
    print(welcome_message)

def show_info_message(name):
    while True:
        if len(name) > 0:
            info_message = f'\nHello {name}! Your adventure begins here! Navigate to different rooms to progress. Have fun✨!\n'
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
    print(player.current_room.name)
    # Write a loop that:
    while True:
        #
        # * Prints the current room name
        # print(player.current_room)
        print(f'You are currently at "{player.current_room.name}".')
        # * Prints the current description (the textwrap module might be useful here).
        print(textwrap.dedent(player.current_room.description))

        # * Waits for user input and decides what to do.
        #
        print("\nWhere do you go next?")
        command = input("[n] north   [s] south   [e] east    [w] west    [q] quit\nyour choice >>  ")

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
                print(f'\n****There is no rooms to the north of "{player.current_room.name}". Try a different path!***\n')
                continue

        elif command[0] == 's':
            if player.current_room.s_to:
                player.current_room = player.current_room.s_to
            else:
                print(f'\n****There is no rooms to the south of "{player.current_room.name}". Try a different path!***\n')
                continue

        elif command[0] == 'e':
            if player.current_room.e_to:
                player.current_room = player.current_room.e_to
            # except (NameError, AttributeError):
            else:
                print(f'\n****There is no rooms to the east of "{player.current_room.name}". Try a different path!***\n')
                continue

        elif command[0] == 'w':
            if player.current_room.w_to:
                player.current_room = player.current_room.w_to
            # except (NameError, AttributeError):
            else:
                print(f'\n****There is no rooms to the west of "{player.current_room.name}". Try a different path!***\n')
                continue

        else:
            print(f'\n****Wrong command: "{command}"...Try again?****\n')



if __name__ == '__main__':
  adventure_game()

