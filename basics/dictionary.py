tea_shop={
    "chai":{"masla":"spicy","Ginger":"Zesty"},
     "Tea":{"Green":"Mild","Black":"Strong"}
          }
print(tea_shop)
print(tea_shop["chai"]["masla"])

#-----------------------------------> Dictionary Exericse<-----------------------------------
squre_num={x:x**2 for x in range(6)}
print(squre_num)
#-----------------------------------> Dictionary Exericse<-----------------------------------
keys = ["masla", "Ginger", "lemon"]
default_value = 'sweet'
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)

keys = ['masla', 'Ginger', 'lemon']
values = ['spicy', 'strong', 'sour']

new_dict = dict(zip(keys, values))
print(new_dict)

keys = ['rose', 'tulip', 'sunflower']
values = ['red', 'yellow', 'golden']
default_value='Beautifull'
new_dict=dict(zip(keys,values))
print(new_dict)
new_dict=dict.fromkeys(keys,default_value)
print(new_dict)

# ### 🧠 Scenario:

# You're a **librarian** setting up a system:

# 1. You have these book titles:

# ```python
# books = ['Python Basics', 'AI for Beginners', 'Data Science 101']
# ```

# 2. You want to do **two tasks**:

# ---

# ### ✅ Task 1:

# Each book has a **different number of copies**:

# ```python
# copies = [4, 2, 5]
# ```

# **👉 Create a dictionary that shows how many copies are available per book.**

# ---

# ### ✅ Task 2:

# Later, you decide to **mark all books as "Available"** in your library system.

# **👉 Create a second dictionary where each book has the same value: `"Available"`**

books = ['Python Basics', 'AI for Beginners', 'Data Science 101']
copies = [4, 2, 5]

default_value="Available"
stock_details=dict(zip(books,copies))

print(stock_details)

stock_details=dict.fromkeys(books,default_value)
print(stock_details)
