class Dog():
    
    
    species = "mammal"
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
        
mydog = Dog(breed="Lab",name = "Ankit")
print(mydog.breed)
print(mydog.name)
print(mydog.species)

""" 
op:-Lab
Ankit
mammal 

"""
