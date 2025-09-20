
class BankAccount:
    MIN_BALANCE = 100 # static attribute

    def __init__(self, owner, balance=0): # init method
        self.owner=owner # instance attribute
        self._balance=balance # protected attribute

    def deposit(self, amount): # instance method
        if self._is_valid_amount(amount):
            self._balance += amount
            self.__log_transaction("deposit", amount)
            print(f"{self.owner}'s new balance: {self._balance} ")
        else:
            print("Deposit amount must be positive.")

    def _is_valid_amount(self, amount): # Protected method # Only used within the class or sub classes
        return amount > 0
    
    def __log_transaction(self, transaction_type, amount): # Private method 
        print(f"Logging {transaction_type} of ${amount}. New balance: ${self._balance}")


    @staticmethod 
    def is_valid_interest_rate(rate):  # static method
        return 0<= rate <=5
    
account=BankAccount("Alice",500)
account.deposit(200)


print(BankAccount.is_valid_interest_rate(10))

