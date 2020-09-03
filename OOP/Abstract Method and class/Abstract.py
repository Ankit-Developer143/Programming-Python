from abc import ABC ,abstractmethod



class Animal(ABC):
    pass

@abstractmethod
def eat(self):
    pass

class Dog(Animal):
    def eat(self):
        print("Dog eat")

#a = Animal()
b = Dog()
b.eat()

    

   




