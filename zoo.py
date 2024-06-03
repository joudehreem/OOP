class Animal:
    def __init__(self,name,age,health_level,happiness_level):
        self.name=name
        self.age=age
        self.health=health_level
        self.happiness=happiness_level
    
    def display_info (self):
        print(f"The animal : {self.name} ,Age: {self.age} ,Level of Health: {self.health} , Level of Happiness: {self.happiness}")
        return self
    def feed(self):
        self.happiness+=10
        self.health+=10
        return self

class Lion(Animal):
    def __init__(self, name,age=6):
        super().__init__(name,age, health_level=10, happiness_level=10)
    def feed(self):
        self.health += 9
        self.happiness += 5
class Tiger(Animal):
    def __init__(self, name,age=7):
        super().__init__(name,age ,health_level=10, happiness_level=10)
    def feed(self):
        self.health += 5
        self.happiness += 8

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name):
        self.animals.append(Lion(name))
    def add_tiger(self, name):
        self.animals.append(Tiger(name))
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()
