class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
    
    def make_sound(self):
        print(f"{self.name} the {self.species} says '{self.sound}.'")
    
    def eat(self, food):
        print(f"{self.name} is eating {food}.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Cow", "Moo")
    
    def produce_milk(self):
        print(f"{self.name} is producing milk.")

class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, "Chicken", "Cluck")
    
    def lay_egg(self):
        print(f"{self.name} laid an egg.")
    def scratch_ground(self):
        print(f"{self.name} is scratching the ground looking for food.")

class Horse(Animal):
    def __init__(self, name):
        super().__init__(name, "Horse", "Neigh")
    
    def run(self):
        print(f"{self.name} is running across the field.")

sigir = Cow("Sigir")
sigir.make_sound()
sigir.eat("grass")
sigir.produce_milk()

tovuq = Chicken("Tovuq")
tovuq.make_sound()
tovuq.lay_egg()
tovuq.scratch_ground()

ot = Horse("Ot")
ot.make_sound()
ot.run()
ot.sleep()
