class Animal():
    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Animal Eat")


class Dog(Animal):
    def __init__(self):
        #Animal.__init__(self)
        print("Dog Created")


result = Dog()
result.whoAmI()
result.eat()


""" 
Dog Created
Animal
Animal Eat """
