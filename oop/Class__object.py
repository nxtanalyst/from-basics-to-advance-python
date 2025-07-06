# Recap of Object Oreineted Programming
'''A class is a blueprint for object like we objects to mapping realworld scenarios'''
'''And an object is instance of a class created using blueprint'''
'''__init__ a special method which is used to intialzie the attributes of an objectg'''
'''Methods: Its defines the actions behaviour of a Object and these Methods belongs to Object and class'''

# Creating a class with Student Names

class Student:
    name='Mishi'
    def __init__(self,fullname):
        self.fullname=fullname
        
        print(f'Hi Students {self.fullname}')


s1=Student('Kamal Hussain')
print(s1.fullname)
print(Student.name)

class Stu:
    @staticmethod
    def hello():
        print('Checking My Static Method')

    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
    def average(self):
        return f'Average of: {sum(self.subject)/len(self.subject)}'

S3=Stu('Haroon',[10,12,14])
print(S3.average())
S3.hello()
# STATIC METHOD
'Static methods Does not use Self keyword they do not work at Object level they work at class level'

class RoyalAnimal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def introduce(self):
        print(f"I am {self.name}, the majestic {self.species} of the royal jungle!")

    def make_sound(self):
        if self.species.lower() == "lion":
            print("Roar! 🦁")
        elif self.species.lower() == "eagle":
            print("Screech! 🦅")
        else:
            print("A noble sound echoes...")

    def rename(self, new_name):
        self.name = new_name
        print(f"My new royal name is {self.name}!")

    def describe(self):
        print(f"{self.name} is a noble {self.species} of the kingdom.")
    
    def crown(self):
        if self.species.lower()=='lion':
            print(f'The title for {self.species} is KingLeo')
        elif self.species.lower() == "eagle":
            print(f'The title for {self.species.title()} is KingEgo')
        else:
            print(f'The title for {self.species} is KingKong')
        print(f"{self.name} is a noble {self.species} of the kingdom.")
    
    def newtrait(self,new_trait):
        self.new_trait=new_trait
        print(f"{self.name} is a noble {self.species} and can Do {self.new_trait} of the kingdom.")




r1=RoyalAnimal('Simba','lion')
r2=RoyalAnimal('Zara','Eagle')
r1.introduce()
r2.introduce()
r1.make_sound()
r2.make_sound()
r1.rename('Zibra')
r1.describe()
r1.crown()
r2.newtrait('Run fast')

class Royalzoo:
    animals=[]
    
    def __init__(self, name, specie, unique_skill):
        self.name = name
        self.specie = specie
        self.unique_skill = unique_skill
        Royalzoo.animals.append(self)  # Add animal to the list on creation
    
    def describe(self):
        print(f'Animal is {self.name} Specie: {self.specie} uniqueSkills: {self.unique_skill}')
    
    def update_skills(self, new_skill):
        self.unique_skill = new_skill
        print(f"✅ {self.name}'s skill updated to: {self.unique_skill}")

    @classmethod
    def allanimals(cls):
        print(f'The List: {cls.animals}')
    @classmethod
    def countAnimal(cls):
        print(f'The animals are, {len(cls.animals)}')
    @classmethod
    def removeAnimal(cls, nameanimal):
        ask = input(f"⚖️ Has '{nameanimal}' been sent to another kingdom? (yes/no): ")
        if ask.lower() == 'yes':
            for animal in cls.animals:
                if animal.name == nameanimal:
                    cls.animals.remove(animal)
                    print(f"🚚 {nameanimal} has been removed from the Royal Zoo.")
                    return
            print(f"❌ {nameanimal} not found in the Royal Zoo.")
        else:
            print("🔁 No changes made.")
    

# 🧪 Example Usage
a1 = Royalzoo("Simba", "Lion", "Roaring")
a2 = Royalzoo("Zara", "Eagle", "Flying High")
a3 = Royalzoo("Rocky", "Bear", "Fishing Expert")

a1.describe()
a1.update_skills("Running Fast")

Royalzoo.allanimals()
Royalzoo.countAnimal()
Royalzoo.removeAnimal("Zara")
Royalzoo.allanimals()

class Book:
    def __init__(self, title, author, genre, available=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available

    def describe(self):
        status = "Available" if self.available else "Borrowed"
        print(f"📖 Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Status: {status}")

    def mark_borrowed(self):
        self.available = False

    def mark_returned(self):
        self.available = True


class Library:
    books = []

    @classmethod
    def add_books(cls, book):
        cls.books.append(book)

    @classmethod
    def show_available_books(cls):
        for book in cls.books:
            if book.available:
                book.describe()

    @classmethod
    def borrow_book(cls, title):
        for book in cls.books:
            if book.title == title and book.available:
                book.mark_borrowed()
                print(f"✅ '{title}' has been borrowed.")
                return
        print(f"❌ '{title}' is not available for borrowing.")

    @classmethod
    def return_book(cls, title):
        for book in cls.books:
            if book.title == title:
                book.mark_returned()
                print(f"🔁 '{title}' has been returned.")
                return
        print(f"❌ '{title}' not found in library.")

    @staticmethod
    def welcome_note():
        print("📚 Welcome to the Royal Library System! 📖")


# Create Book instances
b1 = Book("The Alchemist", "Paulo Coelho", "Fiction")
b2 = Book("A Brief History of Time", "Stephen Hawking", "Science")
b3 = Book("To Kill a Mockingbird", "Harper Lee", "Classic")

# Add books to the Library
Library.add_books(b1)
Library.add_books(b2)
Library.add_books(b3)

# Show welcome note
Library.welcome_note()

# Show all available books
print("\n--- 📘 Available Books ---")
Library.show_available_books()

# Borrow a book
print("\n--- 🛒 Borrowing Book ---")
Library.borrow_book("The Alchemist")

# Show available books after borrowing
print("\n--- 📉 Available Books After Borrowing ---")
Library.show_available_books()

# Return a book
print("\n--- 🔁 Returning Book ---")
Library.return_book("The Alchemist")

# Show available books after return
print("\n--- 📈 Available Books After Returning ---")
Library.show_available_books()


class RoyalVault:
    def __init__(self):
        self.gold = 1000          # public
        self._map = "Hidden Map"  # protected (conventionally)
        self.__code = 12345       # private (name mangling)

    def reveal_code(self):
        return self.__code

vault = RoyalVault()
print(vault.gold)       # ✅ Allowed
print(vault._map)       # ⚠️ Allowed but discouraged
print(vault.__code)     # ❌ Will throw error
print(vault._RoyalVault__code)  # ✅ Hacky but possible (not recommended)

print(vault.reveal_code())  # ✅ Best practice to access private data


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


class RoyalTreasureChest:
    def __init__(self,goldamount,chest_type,owner):
        self.__goldamount=goldamount
        self._chest_type=chest_type
        self.owner=owner
        self.__last_action = None  # Private variable to track last action
    def add_gold(self,amount):
        if amount>0:
            self.__goldamount+=amount
            self.__log_action(f"Added {amount} gold.")
            return self.__goldamount
        else:
            return f'Sorry amount is Insufficent'
    
    def remove_gold(self,amount):
        if amount <= self.__goldamount:
            self.__goldamount-=amount
            self.__log_action(f"Removed {amount} gold.")
            return self.__goldamount
        else:
            return "❌ Not enough gold!"
    def get_gold(self):
        return self.__goldamount
    def _reveal_chest_type(self):
        return self._chest_type
    def __log_action(self,action):
        self.__last_action = f"Action by {self.owner}: {action}"
    def view_log(self):
        return self.__last_action or "No actions recorded yet."


chest = RoyalTreasureChest(1000, "Ancient", "Majesty")
chest.add_gold(500)       # Adds 500 gold
chest.remove_gold(300)    # Removes 300 gold
print(chest.get_gold())   # Shows 1200
print(chest._reveal_chest_type())  # Shows “Ancient”
print(chest.view_log())   # Shows last action taken


    

