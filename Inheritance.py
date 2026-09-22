# INHERITANCE:
# -> It allows one class(child) to use the properties and methods of another class(parent).
# -> Child class can also override parent methods or add new ones.
# -> In python, syntax for inheritance is child(parent)
# -> In java, syntax will be like child class extends parent class
# Example:
class Animal:                                # Animal is a parent class
    def sound(self):
        print("Some generic animal sound")
class Dog(Animal):                           # Dog is a child class
    def sound(self):                         # Method overriding by child
        print("Bark! Bark!")
class Cat(Animal):
    def sound(self):
        print("Meow! Meow!")
a = Animal()
d = Dog()
c = Cat()
a.sound()                                   # Some generic animal sound
d.sound()                                   # Bark! Bark!
c.sound()                                   # Meow! Meow!


# Inheritance classified into 4 types:
#   1. Single Inheritance
#   2. Multiple Inheritance
#   3. Multilevel Inheritance
#   4. Hierarchial Inheritance
#   5. Hybrid Inheritance


# 1. SINGLE INHERITANCE:
# -> One child inherits from one parent.
# -> Child -> parent
# Example:
class Animal:
    def sound(self):
        print("Animal Sound")
class Dog(Animal):
    def sound(self):
        print("Bark! Bark!")
d = Dog()
d.sound()                         # output: Bark! Bark!


# 2. MULTIPLE INHERITANCE:
# -> One child inherits from two or more parents.
# -> child -> parent1 -> parent2
# Example:
class Animal:
    def sound(self):
        print("Animal Sound")
class Pet:
    def owner(self):
        print("Has an owner")
class Dog(Animal, Pet):
    def sound(self):
        print("Bark! Bark!")
d = Dog()
d.sound()                      # Output: Bark! Bark!
d.owner()                      # Output: Has an owner


# 3. MULTILEVEL INHERITANCE:
# -> Inheritance chain.
# -> Grandparent -> parent -> child
# Example:
class Animal:
    def sound(self):                # Grandparent
        print("Animal sound")
class Dog(Animal):                  # Parent
    def sound(self):
        print("Bark! Bark!")
class Puppy(Dog):                   # Child
    def sound(self):
        print("Little Bark!")
p = Puppy()
p.sound()                      # Output: Little Bark!


# 4. HIERARCHIAL INHERITANCE:
# -> Multiple children inherits from the same parent.
# -> Parent -> child1 -> child2
# Example:
class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def sound(self):
        print("Bark! Bark!")
class Cat(Animal):
    def sound(self):
        print("Meow! Meow!")
d = Dog()
d.sound()                           # Output: Bark! Bark!
c = Cat()
c.sound()                           # Output: Meow! Meow!


# 5. HYBRID INHERITANCE:
# -> Combination of two or more types of inheritance(rare in practice)
# Example:
class Animal:
    def sound(self):
        print("Animal Sound")
class Pet:
    def owner(self):
        print("Has an owner")
class Dog(Animal, Pet):               # Multiple Inheritance
    def sound(self):
        print("Bark! Bark!")
class Puppy(Dog):                     # MultiLevel Inheritance
    def sound(self):
        print("Little Bark!")
p = Puppy()
p.sound()                         # Output: Little Bark!
p.owner()                         # Output: Has an owner


# super():
# -> lets the child class call the parent's method.
# -> This is useful when you want to extend the parent's behaviour instead of completely replacing it.
# Example:
class Animal:
    def sound(self):
        print("Generic animal sound")
class Dog(Animal):
    def sound(self):
        super().sound()                  # calling parent method
        print("Bark! Bark!")
d=Dog()                      
d.sound()                  
# Output:
# Generic animal sound
# Bark! Bark!