class RoyalScroll:
    def __init__(self,title,author,secret_msg):
        self.title=title
        self._author=author
        self.__secret_msg=secret_msg
    
    def read_scroll(self):
        print(f'Title: {self.title} Author: {self._author}, SecretMsg: {self.__secret_msg}')

obj=RoyalScroll('Alchemsit','ElShafaq','Hi Like your book')
obj.read_scroll()
print(obj.title)
print(obj._author)
# print(obj.__secret_msg)

class KingdomAccount:
    def __init__(self,balance):
        self.__balance=balance
    
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print('Amount Has been Deposited')
        else:
            print('Insufficent balance: ')
    def  withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance-=amount
            print('Amount Has been withdrawl')
        else:
            print('Insufficent balance: ')
    
    def get_balance(self):
        return self.__balance

abc=KingdomAccount(2000)
abc.deposit(10000)
print(abc.get_balance())
abc.withdraw(1000)
print(abc.get_balance())

class RoyalStatue:
    def __init__(self,material):
        self.__material=material
    
    @property
    def material(self):
        return self.__material
    @material.setter
    def material(self, new_material):
            allowed_materials = ["gold", "silver", "marble", "bronze"]
            if new_material.lower() in allowed_materials:
                print(f"✅ Changing material from {self.__material} to {new_material}")
                self.__material = new_material
            else:
                print("❌ Invalid operation: material not allowed.")
        
abc = RoyalStatue("gold")
print(abc.material)         # Output: gold

abc.material = "silver"     # Output: ✅ Changing material from gold to silver
print(abc.material)         # Output: silver

abc.material = "wood"       # Output: ❌ Invalid operation: material not allowed.

class  SecretCouncil:

    def __reveal_plan(self):
        return "Hi, it's the strategy string"
    
    def access(self):
        return self.__reveal_plan()


abc=SecretCouncil()
abc.access()

class KingdomGate:
    def __init__(self,passcode):
        self.__passcode=passcode
        self.__attempts = []  # private log
    
    def enter(self,pass_input):
        if pass_input==self.__passcode:
            print('Gate Opened, Welcome Majesty!')
        else:
            print("Intruder Alert!")
    
    def __log_attempt(self, attempt):
            self.__attempts.append(attempt)

    def view_logs(self):
        print("📜 Access Log:", self.__attempts)


gate = KingdomGate("majestic123")

gate.enter("wrongpass")
gate.enter("majestic123")
gate.enter("spycode")
gate.view_logs()


class RoyalSecuritySystem:
    def __init__(self):
        self.__treasure=10
        self.__authorized_users=["Majesty"]
        self.__logs=[]
        self.__mode='locked'
    
    def access_vault(self,user):
        if user in self.__authorized_users and self.__mode=='open':
            self.__log_attempt(user, "Success")
            return f"✅ Access granted to {user}"
        
        else:
            self.__log_attempt(user, "Failed")
            return f'sorry acess is denied {user}'
    
    @property
    def treasure(self):
        return self.__treasure
    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self,newmode):
        if newmode.lower() in ["open", "locked"]:    
            self.__mode=newmode.lower()
            print(f"🔐 Mode changed to: {self.__mode}")
        else:
            print("❌ Invalid mode. Use 'open' or 'locked'.")
    def add_user(self,user):
        if self.__mode=='locked':
            self.__authorized_users.append(user)
            print(f"✅ {user} added to authorized users.")
        else:
            print("❌ Cannot add user while vault is open.")
        
    def __log_attempt(self, user, status):
        self.__logs.append({"user": user, "status": status})
    
    def summary(self):
        print("\n📜 Access Summary:")
        print(f"Total attempts: {len(self.__logs)}")
        success = sum(1 for log in self.__logs if log["status"] == "Success")
        failed = len(self.__logs) - success
        print(f"✅ Successes: {success}")
        print(f"❌ Failures: {failed}")



vault = RoyalSecuritySystem()
vault.access_vault("Spy")
vault.mode = "open"
print(vault.access_vault("Majesty"))
vault.access_vault("Guard")
vault.mode = "locked"
vault.add_user("Guard")
vault.mode = "open"
vault.access_vault("Guard")

print("💰 Treasure inside:", vault.treasure)
vault.summary()
