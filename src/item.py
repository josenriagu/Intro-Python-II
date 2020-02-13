class Item:
    # constructor
    def __init__(self, name, description, qty=1):
        self.name = name
        self.description = description
        self.qty = qty

    def __str__(self):
        return (f'{self.name}')

    def on_take(self):
        print(f'\nYou have picked up {self.name}!')
        return self

    def on_drop(self):
        print(f'\nYou have dropped {self.name}!')
        return self
