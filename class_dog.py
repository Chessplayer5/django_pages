class Dog:

    # the __init__ method initializes the object.
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []  # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)
