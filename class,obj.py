# CLASS:
# -> Blueprint or template
# -> defines attribute and methods
class Person:
    hair="black"
    eyes="brown"
#  Person is the class


# OBJECT:
# -> Instance of a class(real world entity from blueprint)
class Person:
    eyes="brown"
    hair="black"
p1 = Person()
print(p1.hair)  # Output: black
print(p1.eyes)  # Output: brown
# p1 is the object of the class Person 

# ex1
class Person:
    hair="black"
    eyes="brown"
p1 = Person()
print(p1.hair) # Output: black
print(p1.eyes) # Output: brown

#ex2:
class Check:
    name="Nikki"
    age=25
c1=Check()
print(c1.name + " is " + str(c1.age) + " years old.") # Output: Nikki is 25 years old.


# METHOD:
# -> Function inside a class
# -> alwayd takes self as first parameter
# SELF:
# -> Reprsents the instance of the class
class Person:
    def display(self):
        print("Hello, I am a person.")
p1 = Person()
p1.display()  # Output: Hello, I am a person.
# display is the method

# ex1:
class Person:
    hair="black"
    eyes="brown"
    def qualities(self):
        print(self.eyes + " eyes and " + self.hair + " hair.")
p1 = Person()
p1.qualities() # Output: brown eyes and black hair.


# CONSTRUCTOR:
# -> Special method that is runs automatically when an object is created
# -> used to initialize attributes of the class
# Eg: __init__ method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age)
p1 = Person("Alice", 30)
p1.display()  # Output: Alice 30


# CLASS VARIABLES AND INSTANCE VARIABLES:
# -> Class variables are shared among all instances of a class.
# -> Instance variables are unique to each instance.
class Car:
    wheels=4                     # Class Variable
    def __init__(self,name):
        self.name = name         # Instance Variable
c1 = Car("Fortuner")
