'''Encapsulation means wrapping senstive data into single unit  and allowing senstive data through controll access'''
# wrapping data and methods in single units/ prevent theri acess to unknown place
# Nothing in Python is truly private: 

class Atm:
    def __init__(self,pin,balance):
        self.__pin=pin
        self.__balance=balance
        self.menu()
    

    def menu(self):
        
        while True:
            ask=input('''
                    Hello How would you like to proceed
                    1). Enter 1 for create Pin
                    2). Enter 2 to Deposit
                    3). Enter 3 for witdhrawl
                    4). Enter 4 to check balance
                    5). Enter 5 to exit
                    ''')
            if ask=='1':
                print('You can create the Pin')
                self.createpine()
            elif ask=='2':
                print('Deposit!!!')
                self.deposit()
            elif ask=='3':
                print('*******Withdrawal**********')
                self.withdrawl()
            elif ask=='4':
                print('check for balance')
                self.checkblance()
            elif ask=='5':
                print('*********************Exiting***************************')
                break
    #Using Setter Getter:/
    # getter
    def get_pin(self):
        return self.__pin
    # Setter
    def set_pin(self,new_pin):
        self.__pin=new_pin
        print('Pin Changed Successfully!')
    def createpine(self):
        self.__pin=input('Enter your pin: ')
        print("Pin Created Successfully:)")
    
    def deposit(self):
            if not self.verfiypin(): 
                return 
            amount=int(input('Enter Amount: '))
            if amount>0:
                self.__balance+=amount
                print(f"Amount Deposit Successfully: {amount})")
            else:
                 print("❌ Invalid amount.")
        
    def withdrawl(self):
        if not self.verfiypin():
            return
        amount = int(input('🏧 Enter amount to withdraw: '))
        if amount>self.__balance:
            print('Sorry Insufficent Balance: ')
        else:
            self.__balance-=amount
            print(f"✅ {amount} withdrawn successfully!")
    
    def checkblance(self):
        if not self.verfiypin():
            return
        print('Here is Your Current Blance',self.__balance)
    def verfiypin(self):
        entered = input("🔑 Enter your PIN to proceed: ")
        if entered==self.__pin:
            return True
        else:
            print("❌ Incorrect PIN.")
            return False

abc=Atm('1234',10000)
abc.__balance='asdasdas'
abc._Atm__balance='asdasdas'
abc.deposit()