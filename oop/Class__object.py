# # Recap of Object Oreineted Programming
# '''A class is a blueprint for object like we objects to mapping realworld scenarios'''
# '''And an object is instance of a class created using blueprint'''
# '''__init__ a special method which is used to intialzie the attributes of an objectg'''
# '''Methods: Its defines the actions behaviour of a Object and these Methods belongs to Object and class'''

# # Creating a class with Student Names

# class Student:
#     name='Mishi'
#     def __init__(self,fullname):
#         self.fullname=fullname
        
#         print(f'Hi Students {self.fullname}')


# s1=Student('Kamal Hussain')
# print(s1.fullname)
# print(Student.name)

# class Stu:
#     @staticmethod
#     def hello():
#         print('Checking My Static Method')

#     def __init__(self,name,subject):
#         self.name=name
#         self.subject=subject
#     def average(self):
#         return f'Average of: {sum(self.subject)/len(self.subject)}'

# S3=Stu('Haroon',[10,12,14])
# print(S3.average())
# S3.hello()
# # STATIC METHOD
# 'Static methods Does not use Self keyword they do not work at Object level they work at class level'

# class RoyalAnimal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def introduce(self):
#         print(f"I am {self.name}, the majestic {self.species} of the royal jungle!")

#     def make_sound(self):
#         if self.species.lower() == "lion":
#             print("Roar! 🦁")
#         elif self.species.lower() == "eagle":
#             print("Screech! 🦅")
#         else:
#             print("A noble sound echoes...")

#     def rename(self, new_name):
#         self.name = new_name
#         print(f"My new royal name is {self.name}!")

#     def describe(self):
#         print(f"{self.name} is a noble {self.species} of the kingdom.")
    
#     def crown(self):
#         if self.species.lower()=='lion':
#             print(f'The title for {self.species} is KingLeo')
#         elif self.species.lower() == "eagle":
#             print(f'The title for {self.species.title()} is KingEgo')
#         else:
#             print(f'The title for {self.species} is KingKong')
#         print(f"{self.name} is a noble {self.species} of the kingdom.")
    
#     def newtrait(self,new_trait):
#         self.new_trait=new_trait
#         print(f"{self.name} is a noble {self.species} and can Do {self.new_trait} of the kingdom.")




# r1=RoyalAnimal('Simba','lion')
# r2=RoyalAnimal('Zara','Eagle')
# r1.introduce()
# r2.introduce()
# r1.make_sound()
# r2.make_sound()
# r1.rename('Zibra')
# r1.describe()
# r1.crown()
# r2.newtrait('Run fast')

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

