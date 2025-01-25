class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("I am {}and i am {} years old".format(self.name,self.age)) 
    def make_sound(self):
        print("I bark at strangers")  
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("I am {}and i am {} years old".format(self.name,self.age)) 
    def make_sound(self):  
        print("I make sound meow when i need milk")     

d1=Dog("Coco",3)  
C1=Cat("kitty",8) 

for animal in(d1,C1):
    animal.info()
    animal.make_sound()
