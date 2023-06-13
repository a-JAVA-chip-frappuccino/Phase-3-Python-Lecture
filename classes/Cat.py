from Animal import Animal

# class Cat inherits class Animal
class Cat(Animal):

    def __init__(self, color):
        super().__init__("cat", color) # calls constructor of Animal and sends over information

    def take_a_cat_nap(self):
        super().take_a_nap() # calls take_a_nap method of Animal

    def make_biscuits(self):
        print("rolling out the dough")
        print("biscuits in the oven delish")
        return "hooray free biscuits"

kurt = Cat("orange")

print(kurt.make_biscuits())