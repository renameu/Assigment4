class Stuff:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def display_info(self):
        pass


class House(Stuff):
    def __init__(self, name, description, price, address):
        super().__init__(name, description, price)
        self.address = address

    def display_info(self):
        print(f"{self.name} - {self.description} - {self.address} - ${self.price}")


class Flat(Stuff):
    def __init__(self, name, description, price, floor):
        super().__init__(name, description, price)
        self.floor = floor

    def display_info(self):
        print(f"{self.name} - {self.description} - {self.floor} - ${self.price}")


