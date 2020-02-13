# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    # constructor
    def __init__(self, name, description, treasures=[]):
        self.name = name
        self.description = description
        self.treasures = treasures

    def get_item(self, treasure):
        self.treasures.append(treasure)
        return self

    def drop_item(self, treasure):
        self.treasures.remove(treasure)
        return self
