'''cenario: Secure Royal Bank Account Management with Encapsulation

In this banking simulation, each account uses encapsulation principles to manage sensitive financial data securely.

__balance is private, ensuring no direct external modification.

deposit() and withdraw() provide controlled ways to update the balance.

_acountype is protected, indicating internal usage but still accessible if needed.

__log_access() is a private method that logs account activity, accessed safely via get_log().

The code also demonstrates:

Best practice vs. unsafe (hacky) access to private data/methods

The importance of method-based access for data integrity

This design is ideal for financial systems, banking applications, or security-focused software where access control is critical.'''

class RoyalBankAccount:

    def __init__(self,balance,acountype,owner):
        self.__balance=balance
        self._acountype=acountype
        self.owner=owner

    
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount

        return self.__balance
    def withdraw(self, amount):
        if amount<=self.__balance:
            self.__balance-=amount
            return f"Withdrawn {amount}, remaining balance: {self.__balance}"
        else:
            return "❌ Insufficient funds."
    
    def get_balance(self):
        return self.__balance
    def _display_type(self):
        return self._acountype
    def __log_access(self): 
        return f"Accessed by: {self.owner}, balance: {self.__balance}"
    def get_log(self):  # Recommended way to access private method
        return self.__log_access()

obj=RoyalBankAccount(10000,'Current','Hussain')
print(obj.deposit(2000))
print(obj.withdraw(1000))
print(obj.get_balance())
print(obj._display_type())
print(obj.get_log())

print(obj._RoyalBankAccount__log_access())  # ❌ Hacky access
