from room import Room
from player import Player

# Declare all the rooms

rooms = {
    'outside':  Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons"
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


def main():
    global room_directions
    while not quit_game:
        # print room information
        player.print_room()
        # get permitted directions for the current room
        room_directions = [key.split("_")[0].upper() for key, val in vars(
            player.current_room).items() if key not in ['name', 'description', 'key']]
        # inform player of available directions
        print()
        print(f'All Coordinates: {all_directions}',
              f'This room permits: {room_directions}', sep="\n")
        # allow player input
        print()
        user_input = input(
            "Enter a direction to travel or 'q' to quit game\n").upper()
        # make a journey
        travel(user_input)


def travel(user_input):
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
        print("Auch! you can travel to this direction from this room")
    elif user_input not in all_directions:
        print("Errhm! Are you just turnioniown? Choose from all coordinates!")


def quit(room_name):
    global quit_game
    print(f'You are quitting the game from {room_name}', 'Bye!', sep="\n")
    quit_game = True


# start game
main()
