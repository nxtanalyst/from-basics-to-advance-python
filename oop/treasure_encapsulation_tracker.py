'''Scenario: Royal Treasure Chest with Gold Tracking & Encapsulation

This class models a Royal Treasure Chest system where gold deposits and withdrawals are recorded privately and securely.

The total gold (__goldamount) is hidden from direct access.

All changes to gold are logged using a private logging method (__log_action()).

The chest also tracks the last action taken, which is exposed through view_log() for transparency.

It follows encapsulation best practices:

Public methods handle all changes to internal state.

Sensitive data is never accessed directly.

The _chest_type attribute is marked as protected, discouraging external modification but allowing visibility.

This is an ideal model for secure vault simulations, educational tools, or any system that needs controlled state modification with auditability.

'''


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
