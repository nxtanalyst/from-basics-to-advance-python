'''Scenario: Royal Vault Data Protection Using Encapsulation

In the royal treasury system (RoyalVault), there are different layers of data protection:

gold: Publicly accessible — general information.

_map: Protected — meant for internal or subclass use, but accessible with caution.

__code: Private — critical data hidden using name mangling, not directly accessible.

The code demonstrates:

Why accessing __code directly fails (vault.__code)

Why using vault._RoyalVault__code works but is discouraged

How to correctly expose private data using a public method (reveal_code())

This mirrors real-world security practices, where sensitive information is guarded and only exposed through controlled interfaces.

Ideal for teaching data hiding and class security concepts in Python's OOP paradigm.

'''

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
