# ABSTRACTION:
# -> It means hiding implementation details and showing only the essential features.
# -> Abstraction is usually achieved through abstract classes and interfaces in programming.

# Example1:
class Animal:
    def sound(self):              # abstract method
        pass                      # no details here, just a placeholder
class Dog(Animal):
    def sound(self):
        print("Bark! Bark!")
class Cat(Animal):
    def sound(self):
        print("Meow! Meow!")
a1 = Dog()
a1.sound()                       # Output: Bark! Bark!
a2 = Cat()
a2.sound()                       # Output: Meow! Meow!


# Example2: 
class PaymentProcessor:
    def processPayment(self, amt):                                  # abstract method
        pass
class CreditCardPayment(PaymentProcessor):
    def processPayment(self, amt):
        print(f"Processing credit card payment of {amt}")         
class UPIProcessor(PaymentProcessor):
    def processPayment(self, amt):
        print(f"Processing UPI payment of {amt}")
payment1 = CreditCardPayment()
payment1.processPayment(5000)                                       # Processing credit card payment of 5000
payment2 = UPIProcessor()
payment2.processPayment(2000)                                       # Processing UPI payment of 2000                                   
