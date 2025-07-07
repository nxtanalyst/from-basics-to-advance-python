'''Scenario: Class-Level Royal Zoo Management System

In this system, every time a new animal is created, it is automatically registered into the Royal Zoo's central registry using a class variable. The zoo can then:

Show a list of all current animals.

Count the total number of animals in the zoo.

Remove an animal when it's transferred to another kingdom, using a confirmation prompt.

This structure uses class methods for centralized tracking and control, making it ideal for simulations, educational software, or lightweight zoo/inventory management systems where global state needs to be maintained across multiple instances.

The design makes it easy to maintain a shared resource across all instances and perform collective operations.'''


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
