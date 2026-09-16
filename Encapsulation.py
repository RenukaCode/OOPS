# ENCAPSULATION
# Encapsulation means wrapping data(variables) and methods(functions) together inside a class.
# It allows data hiding -> restricting direct access to variables, so they can only be accessed through methods of the class.
# This protects the internal state of an object from unintended changes

# Example
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance
    # getter method 
    def get_balance(self):
        return self.__balance
    # setter method 
    def deposit(self,amt):
        if amt > 0:
            self.__balance += amt
            print(f"Deposited {amt}. New Balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")
acc = BankAccount("Nikki",1000)
acc.deposit(500)   # Output: Deposited 500. New Balance: 1500
# __balance -> double underscore makes it private 
# Getter method -> safely retrieves/access the value
# Setter method -> safely modifies the value