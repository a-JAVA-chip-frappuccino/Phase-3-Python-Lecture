class Animal():

    # class attributes
    zoo = []
    zoo_count = 0

    # constructor magic method (called upon creation of an instance of the class)
    def __init__(self, species, color):
        self.species = species
        self.color = color

        Animal.zoo_count += 1
        Animal.zoo.append(self) # appends object to class attribute

    def get_species(self):
        return self._species
    
    def set_species(self, new_species):
        if len(new_species) > 1:
            self._species = new_species

    species = property(get_species, set_species) # property with getter and setter

    @property # property with getter
    def color(self):
        return self._color
    
    @color.setter # property with setter
    def color(self, new_color):
        self._color = new_color

    def take_a_nap(self):
        print("zzzzzzz")
        print(f"sssssshhhhh! {self._species} is taking a nap!")

    # called on Animal class
    @classmethod
    def add_to_zoo_count(cls):
        cls.zoo_count += 1 # cls.zoo_count = cls.zoo_count + 1

    # overriding method to print given string for object
    def __str__(self):
        return "I am a " + self.species + "!!!"

zebra = Animal("zebra", "black and white")
giraffe = Animal("giraffe", "yellow and brown")
giraffe = Animal("giraffe", "yellow and brown")

# print(Animal.zoo_count)
# print(Animal.zoo)

# for a in Animal.zoo:
#     print(a)