# class RoyalScroll:
#     def __init__(self,title,author,secret_msg):
#         self.title=title
#         self._author=author
#         self.__secret_msg=secret_msg
    
#     def read_scroll(self):
#         print(f'Title: {self.title} Author: {self._author}, SecretMsg: {self.__secret_msg}')

# obj=RoyalScroll('Alchemsit','ElShafaq','Hi Like your book')
# obj.read_scroll()
# print(obj.title)
# print(obj._author)
# # print(obj.__secret_msg)

# class KingdomAccount:
#     def __init__(self,balance):
#         self.__balance=balance
    
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#             print('Amount Has been Deposited')
#         else:
#             print('Insufficent balance: ')
#     def  withdraw(self,amount):
#         if amount <= self.__balance:
#             self.__balance-=amount
#             print('Amount Has been withdrawl')
#         else:
#             print('Insufficent balance: ')
    
#     def get_balance(self):
#         return self.__balance

# abc=KingdomAccount(2000)
# abc.deposit(10000)
# print(abc.get_balance())
# abc.withdraw(1000)
# print(abc.get_balance())

# class RoyalStatue:
#     def __init__(self,material):
#         self.__material=material
    
#     @property
#     def material(self):
#         return self.__material
#     @material.setter
#     def material(self, new_material):
#             allowed_materials = ["gold", "silver", "marble", "bronze"]
#             if new_material.lower() in allowed_materials:
#                 print(f"✅ Changing material from {self.__material} to {new_material}")
#                 self.__material = new_material
#             else:
#                 print("❌ Invalid operation: material not allowed.")
        
# abc = RoyalStatue("gold")
# print(abc.material)         # Output: gold

# abc.material = "silver"     # Output: ✅ Changing material from gold to silver
# print(abc.material)         # Output: silver

# abc.material = "wood"       # Output: ❌ Invalid operation: material not allowed.

# class  SecretCouncil:

#     def __reveal_plan(self):
#         return "Hi, it's the strategy string"
    
#     def access(self):
#         return self.__reveal_plan()


# abc=SecretCouncil()
# abc.access()

# class KingdomGate:
#     def __init__(self,passcode):
#         self.__passcode=passcode
#         self.__attempts = []  # private log
    
#     def enter(self,pass_input):
#         if pass_input==self.__passcode:
#             print('Gate Opened, Welcome Majesty!')
#         else:
#             print("Intruder Alert!")
    
#     def __log_attempt(self, attempt):
#             self.__attempts.append(attempt)

#     def view_logs(self):
#         print("📜 Access Log:", self.__attempts)


# gate = KingdomGate("majestic123")

# gate.enter("wrongpass")
# gate.enter("majestic123")
# gate.enter("spycode")
# gate.view_logs()
