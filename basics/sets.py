# sets are undordered of data items they store multiple items in a single vairable 
# sets items are spearted by commas and enclosed within curly bracket 
# sets are unchangeable sets don't conatins duplicate 

#----------------------------------->Sets Methods<-----------------------------------
#----------------------------------->Union method Union()
# Union Methods prints all the memebers of both sets and returns new sets
# where update methods prints all memebers of both sets but it update the first sets 

cities_1={'Tokoyo','Madrid','Berlin','Delhi'}
cities_2={'Tokoyo','Seoul','Kabul','Madrid'}
print(cities_1.union(cities_2))
cities_1.update(cities_2)
print(cities_1)
#----------------------------------->Intersection()    Methods
# These Methods is used to find the common elemnts b/w sets
cities_3={'Tokoyo','Madrid','Berlin','Delhi'}
cities_4={'Tokoyo','Seoul','Kabul','Madrid'}
print(f'Intersection={cities_3.intersection(cities_4)}')
cities_5={'Tokoyo','Madrid','Berlin','Delhi'}
cities_6={'Tokoyo','Seoul','Kabul','Madrid'}

cities_5.intersection_update(cities_6)
print('Update_intersection=',cities_5)
#----------------------------------->Symmetric- DIffernece     Methods()
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f'Syemtric-Diccerce=={set1.symmetric_difference(set2)}')
set1.symmetric_difference_update(set2)
print('symmetric_difference_update',set1)
set1.difference(set2)
print(set1)
#----------------------------------->iddisjoint     Methods()
# isDisjoint always returns True if not elements is common b/w sets

set1 = {1, 2, 3, 4}
set2 = {6, 7, 5, 6}
print(f'Is Disjoint or not=={set1.isdisjoint(set2)}')


#----------------------------------->isSuperSet     Methods()
# The issuper() method checks if all the items of a particular sets are present in the orignal
# and it returns True if presented and otherwise returns flase
cities_3={'Tokoyo','Madrid','Berlin','Delhi'}
cities_4={'Tokoyo','Seoul','Kabul','Madrid'}
print('SuperSet=',cities_3.issuperset(cities_4))
# Subset
# A set A is a subset of set B if all elements of A are also present in B. In other words, A is 
# "contained within" B. This relationship is denoted as A ⊆ B. 
print(cities_3.issubset(cities_4))
#----------------------------------->add  Methods()
# when a single item is added add() method is used
cities_3={'Tokoyo','Madrid','Berlin','Delhi'}

cities_3.add('Sherqillah')
print(cities_3)
# #----------------------------------->Removing   Methods()


# remove(element): Removes the element; raises KeyError if not found.
# discard(element): Removes the element if present; no error if not found.
# pop(): Removes and returns a random element; raises KeyError if set is empty.
# clear(): Removes all elements.
my_set = {1, 2, 3, 4}
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}

my_set.discard(5)  # No error, even though 5 isn't in the set
print(my_set)  # Output: {1, 3, 4}

popped = my_set.pop()  # Removes a random element
print(popped, my_set)  # Output: 1 {3, 4} (popped value may vary)

my_set.clear()
print(my_set)  # Output: set()