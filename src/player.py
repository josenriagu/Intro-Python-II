# Write a class to hold player information, e.g. what room they are in
# currently.
from textwrap import TextWrapper


class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def print_room(self):
        print()  # prints empty line for demarcation
        print("You are currently in")
        print("Room name: {}".format(self.current_room.name))
        # using textwrap to break long room descriptions
        wrapper = TextWrapper(width=55)
        word_list = wrapper.wrap(text=self.current_room.description)
        print("Room description: ", end=" ")
        for line in word_list:
            print(line)

    def move(self, next_room):
        self.current_room = next_room
