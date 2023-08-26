class Animal:
    def __init__(self, name, breed, age) -> None:
        self.name = name
        self.breed = breed
        self.age = age
    def sleep(self):
        print('The animal fell asleep')
    def wake_up(self):
        print('The animal woke up')

class Cat(Animal):
    weight = 5
    height = 35
    def sleep(self):
        print('The cat fell asleep')
    def wake_up(self):
        print('The cat woke up')

class Dog(Animal):
    weight = 18
    height = 45
    def sleep(self):
        print('The dog fell asleep')
    def wake_up(self):
        print('The dog woke up')

cat = Cat('Mary', 'Maine', 5)
dog = Dog('Max', 'Chow-chow', 4)

print(cat.name, cat.breed, cat.age, cat.weight, cat.height)
print(dog.name, dog.breed, dog.age, dog.weight, dog.height)
cat.sleep()
cat.wake_up()
dog.wake_up()
dog.sleep()