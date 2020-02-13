from item import Item
from room import Room
from player import Player

# Declare Items

items = {
    # if qty is not specified, default to 1
    'torch': Item(
        'Torch',
        'Light your path if you stay till night'
    ),
    'phone': Item(
        'Phone',
        'Play some music and rest a while'
    ),
    'charger': Item(
        'Charger',
        'Get some juice into your phone'
    ),
    'sabre': Item(
        'Sabre',
        'If the enemies attack, save your life with this',
        2
    ),
    'gems': Item(
        'Gems',
        'Trade gems for more coins',
        10
    ),
    'coins': Item(
        'Coins',
        'A reward for your journey!',
        5
    ),
}


# Declare all the rooms
rooms = {
    'outside':  Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons",
    ),
    'foyer':    Room(
        "Foyer",
        """Dim light filters in from the south. Dusty passages run north and east."""
    ),
    'overlook': Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""
    ),
    'narrow':   Room(
        "Narrow Passage",
        """The narrow passage bends here from west to north. The smell of gold permeates the air."""
    ),
    'treasure': Room(
        "Treasure Chamber",
        """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""
    ),
}


# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

# add initial treasures to rooms
rooms['outside'].treasures = [items['torch']]
rooms['foyer'].treasures = [items['phone'], items['sabre']]
rooms['overlook'].treasures = [items['charger']]
rooms['narrow'].treasures = [items['gems'], items['coins']]
rooms['treasure'].treasures = []


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
start_room = 'outside'
# Write a loop that:
#
# * Prints the current room name - ✔️
# * Prints the current description (the textwrap module might be useful here) - ✔️
# * Waits for user input and decides what to do - ✔️
#
# If the user enters a cardinal direction, attempt to move to the room there - ✔️
# Print an error message if the movement isn't allowed - ✔️
#
# If the user enters "q", quit the game - ✔️

player = Player(rooms[start_room])
all_directions = ['N', 'E', 'W', 'S']
room_directions = []
quit_game = False


def print_coordinates():
    global room_directions
    if len(room_directions) <= 1:
        print(f'Available Exit: {room_directions}')
    else:
        print(f'Available Exits: {room_directions}')


def intro():
    print(
        f'\nThere\'s one or more exits in each room.\nUse any of {all_directions} to navigate depending on the available exit(s) in that room')
    print("Let's go on some adventure!")


def main():
    global room_directions
    # show introduction
    intro()
    while not quit_game:
        # show room information
        player.print_room()
        # get permitted directions for the current room
        room_directions = [key.split("_")[0].upper() for key, val in vars(
            player.current_room).items() if key not in ['name', 'description', 'treasures']]
        choose_action()


def choose_action():
    user_input = input(
        "\nWhat do you want to do?\nT to travel,\nIT to interact\nI or INVENTORY to view inventory\nQ to quit \n").upper()
    if (user_input == 'T'):
        print("\nAlright buddy, take my hands, let's make a journey")
        travel()
    elif (user_input == 'IT'):
        print("\nWoohoo! Let's find some treasures in this room")
        interact()
    elif (user_input == 'I' or user_input == 'INVENTORY'):
        player.get_inventory()
    elif (user_input == 'Q'):
        quit(player.current_room.name)
    else:
        print("\nInvalid command!")
        choose_action()


def travel():
    # inform player of available directions
    print()
    print_coordinates()
    # allow player input
    user_input = input(
        "Enter an available exit to travel or 'q' to quit game\n").upper()
    # check if directions are pernitted
    if user_input == 'N' and user_input in room_directions:
        player.move(player.current_room.n_to)
    elif user_input == 'E' and user_input in room_directions:
        player.move(player.current_room.e_to)
    elif user_input == 'W' and user_input in room_directions:
        player.move(player.current_room.w_to)
    elif user_input == 'S' and user_input in room_directions:
        player.move(player.current_room.s_to)
    elif user_input == 'Q':
        quit(player.current_room.name)
    elif user_input in all_directions and user_input not in room_directions:
        print("\nAuch! you can travel to this direction from this room. Grab some coffee and let's start afresh")
        travel()
    elif user_input not in all_directions:
        print("\nDon't get lost yet buddy. Remember to choose a real direction!")
        travel()


def interact():
    # add two words to REPL
    user_input = input("\nWhat do you want to do? eg: get Torch \n").split(" ")
    if (len(user_input) == 2 and (user_input[0].lower() == 'get' or user_input[0].lower() == 'drop')):
        do_interact(user_input[0], user_input[1].lower())
    else:
        print("\nInvalid command")
        interact()


def do_interact(action_type, treasure_name):
    if action_type == 'get':
        if len(player.current_room.treasures) > 0:
            for treasure in player.current_room.treasures:
                if treasure_name == treasure.name.lower():
                    player.get_item(treasure)
                    treasure.on_take()
                else:
                    print(f"\nI can't find '{treasure_name}' in this room")
        else:
            print("\nSeems like this room has been ripped of all treasures\nMaybe try dropping some from your inventory?")
            choose_action()
    elif action_type == 'drop':
        if len(player.inventory) > 0:
            for inventory_item in player.inventory:
                if treasure_name == inventory_item.name.lower():
                    player.drop_item(inventory_item)
                    inventory_item.on_drop()
                else:
                    print(
                        f"\nI can't find '{treasure_name}' in your inventory")
        else:
            print(
                "\nOops! Your inventory is empty\nMaybe try searching for some treasures around?")
            choose_action()


def quit(room_name):
    global quit_game
    print(f'\nYou are quitting the game from {room_name}', 'Bye!', sep="\n")
    quit_game = True


# start game
main()
