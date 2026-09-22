# POLYMORPHISM:
# -> Same method name, different behaviour.
# -> It literally means "many forms".
# -> It allows different classes to define methods with same name but different implementations.
# Example:
class Animal:
    def sound(self):
        print("Generic animal sound")
class Dog(Animal):
    def sound(self):
        print("Bark! Bark!")
class Cat(Animal):
    def sound(self):
        print("Meow! Meow!")
animals = [Dog(), Cat()]                              # Polymorphism in action
for a in animals:
    a.sound()                                         # same method call, different output                  
# Output:
# Bark! Bark!
# Meow! Meow!



# 2 main forms of polymorphism:
# Method overloading
# Method overriding

# METHOD OVERLOADING:
# -> Same method name, different parameter list.
# -> Decided at Compile time (called as compile time polymorphism).
# -> Common in Java, but not directly supported in Pyhton(Python allows default arguments instead).
# Example:
class Sum:
    def add(self,a,b=10):
        print(a+b)
s=Sum()
s.add(5)                                                #15
s.add(20,20)                                            #40
# Here b is a default argument, so if argument not passed at object, it takes default argument.

# Java program:
# class Sum{
#     int add(int a){
#         return a+10;                                  #declaring in body but not at parameters.
#     }
#     int add(int a, int b){
#         return a+b;
#     }
# }
# public class Main{
#     public static void main(String[] args){
#         Sum s = new Sum();
#         System.out.println(s.add(5));                # 15
#         System.out.println(s.add(20,20));            # 40
#     }
# }


# METHOD OVERRIDING:
# -> Same method, same parameters, but different behaviour and defined in child class.
# -> Decided at runtime (called as runtime polymorphism).
# -> Supported in both Python and Java
class Animal:
    def sound(self):
        print("Generic sound")
class Dog(Animal):
    def sound(self):                                # overriding
        print("Bark! Bark!")
d=Dog()
d.sound()                                           # Output: Bark! Bark!
              