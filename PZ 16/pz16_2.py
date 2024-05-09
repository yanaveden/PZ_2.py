"""Создайте класс "Животное", который содержит
информацию о виде и возрасте животного. Создайте классы "Собака" и
"Кошка", которые наследуются от класса "Животное" и содержат информацию
о породе"""


class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age

    def get_info(self):
        return f"Это {self.species} возрастом {self.age} лет."


class Pet(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed

    def get_info(self):
        return f"Это {self.species} породы {self.breed} возрастом {self.age} лет."


dog = Pet("Собака", 5, "Лабрадор")
print(dog.get_info())

cat = Pet("Кошка", 6, "Сиамская")
print(cat.get_info())