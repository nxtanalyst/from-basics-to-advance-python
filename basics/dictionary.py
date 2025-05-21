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
# books = ['Python Basics', 'AI for Beginners', 'Data Science 101']

# 2. You want to do **two tasks**:

# ### ✅ Task 1:

# Each book has a **different number of copies**:

# **👉 Create a dictionary that shows how many copies are available per book.**

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
#----------------------------------->Dictionary Methods<-----------------------------------
 #-----------------------------------> Update Method
#  The update() method is used to add new key-value pairs or
#  change the value of existing keys in a dictionary.
person = {'name': 'Ali', 'age': 25}


new_info = {'age': 30, 'profession': 'Engineer'}
person.update(new_info)
print(person)


#----------------------------------->update method Clear()
person = {'name': 'Ali', 'age': 25}


new_info = {'age': 30, 'profession': 'Engineer'}
person.update(new_info)
print(person)
#----------------------------------->Remove method Clear()
# Remove complete Items from dictionary and returns empty dictionary
person_2 = {'name': 'Ali', 'age': 25}
person_2.clear()
print(person_2)
#----------------------------------->Remove method Pop()
# removes the key-value whose key is passed
person_3 = {'name': 'Ali', 'age': 25}
person_3.pop('age')
print(person_3)
#----------------------------------->Remove method popitems()
# removes the last item from the dictionary
person_4 = {'name': 'Ali', 'age': 25}
person_4.popitem()
print(person_4)
#----------------------------------->Remove method del()
# del is used to delete:A specific key-value pair from a dictionary
# Or even the entire dictionary if needed
student = {'name': 'Sara', 'age': 22, 'grade': 'A'}
del student['age']  # Deletes the 'age' key
print(student)
# del student['age']
del student
#-----------------------------------> Dictionary Exericse<-----------------------------------


"""🔧 Most Common Operations (Concept-Only for Now)

| Task         | Syntax                              | Description                       |
| ------------ | ----------------------------------- | --------------------------------- |
| Access value | `person["name"]`                    | Get value by key                  |
| Safe access  | `person.get("age")`                 | Avoids error if key missing       |
| Add/update   | `person["email"] = "a@example.com"` | Adds or updates a key             |
| Remove       | `person.pop("age")`                 | Removes and returns value         |
| Delete key   | `del person["city"]`                | Deletes key-value pair            |
| Keys only    | `person.keys()`                     | Returns all keys                  |
| Values only  | `person.values()`                   | Returns all values                |
| All items    | `person.items()`                    | Returns key-value pairs as tuples |
| Check key    | `"name" in person`                  | Returns True/False                |
| Copy dict    | `person.copy()`                     | Returns a shallow copy            |
| Clear dict   | `person.clear()`                    | Removes all items                 |


Now do the following (your task):

1. Add a new key `"gender"` with value `"Male"`.
2. Change the `"age"` to `21`.
3. Print the average of `"grades"` using the list inside the dictionary.
4. Check if the key `"email"` exists.
5. Safely try to get the `"email"` value using `.get()`.
6. Remove the `"age"` key using `pop()` and print the removed value.
7. Print all keys and all values from the dictionary.
8. Create a shallow copy of the dictionary and print it.
"""

student = {
    "name": "Ali",
    "age": 20,
    "grades": [90, 85, 88]
}
new_dict={"gender":"Male"}
student.update(new_dict)
print(student)
student['age']=21
print(student)
x=sum(student['grades'])/len(student['grades'])
print(x)
print('email' in student)
student.get('email')
student.pop('age')
print(student)

for key,value in student.items():
    print(key,value)
    
shallow_copy=student.copy()
print(shallow_copy)