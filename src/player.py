# Write a class to hold player information, e.g. what room they are in
# currently.
from textwrap import TextWrapper


class Player:
    def __init__(self, current_room, inventory=[]):
        self.current_room = current_room
        self.inventory = inventory

    def print_room(self):
        print()  # prints empty line for demarcation
        print("=" * 70)
        print("You are currently in")
        # show room name and description
        print("Room name: {}".format(self.current_room.name))
        # using textwrap to break long room descriptions
        wrapper = TextWrapper(width=55)
        word_list = wrapper.wrap(text=self.current_room.description)
        print("Room description: ", end=" ")
        for line in word_list:
            print(line)
        # show room treasures
        treasures = []
        for treasure in self.current_room.treasures:
            treasures.append(treasure.__str__())
        print(f'Treasures in this room: {treasures}')

    def move(self, next_room):
        self.current_room = next_room

    def get_item(self, treasure):
        # remove treasure from room
        self.current_room.drop_item(treasure)
        # add treasure to player inventory
        self.inventory.append(treasure)

    def drop_item(self, treasure):
        # remove treasure from player's inventory
        self.inventory.remove(treasure)
        # add treasure back to room
        self.current_room.get_item(treasure)

    def get_inventory(self):
        # show player's inventory
        collectibles = []
        for inventory in self.inventory:
            collectibles.append(inventory.__str__())
        print(f'\nYour inventory: {collectibles}')
