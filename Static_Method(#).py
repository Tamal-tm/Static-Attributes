# A static method in Python is a method that belongs to the class itself rather than any instance of the class. 
# They do not take self as a parameter to access or modify instance specific data instead they are used for functionality relevant to the class but not tied to individual instances.

# To define a static method, we use the '@staticmethod' decorator.

class BankAccount:
    MIN_BALANCE = 100 # static attribute

    def __init__(self, owner, balance=0): # init method
        self.owner=owner # instance attribute
        self._balance=balance # protected attribute

    def deposit(self, amount): # instance method
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}'s new balance: {self._balance} ")
        else:
            print("Deposit amount must be positive.")

    @staticmethod 
    def is_valid_interest_rate(rate): # static method # Does not interact with any specific account or instance.
                                      # Instead performs a check on the rate parameter
                                      # Independent of any BankAccount object.
        return 0<= rate <=5 # Called ddirectly on the class, not on instance objects. 
    
account=BankAccount("Alice",500)
account.deposit(200)

print(BankAccount.is_valid_interest_rate(3)) # On class (BankAccount.method_name)
print(BankAccount.is_valid_interest_rate(10))

# Both static and instance methods are stored in class itself, not in each individual object that we create from the class.
# Memory efficiency, since only one copy of each method exists in memory no matter how many instances we create.

# When to use Static Methods?

# They are ideal for class's domain but don't require any specific instance data.
# Ex: Utlity function/Method. Bank, account. Helper.They can also help to process data or to format outputs that don't rely on instance specific data.
#  Using static methods give a clear separation between behaviour that require instance specfic data and behaviour that doesn't...
# This approache reinforces Encapsulation. (By keeping related functionality within the relevant class)