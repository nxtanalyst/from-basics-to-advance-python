'''In a fantasy wildlife simulator or storytelling game, animals are given royal titles, unique traits, and speaking abilities based on their species. The RoyalAnimal class models this behavior.

introduce() presents the royal identity of the animal.

make_sound() outputs species-specific royal sounds.

rename() allows animals to change titles as part of evolving stories.

describe() gives a formal identity to each creature.

crown() assigns a royal title based on species.

newtrait() introduces magical or legendary abilities (like "Run fast", "Breathe fire", etc.) dynamically.

This system supports a fantasy kingdom setting, making it ideal for educational storytelling apps, interactive games, or even animated children's series concepts.

'''

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