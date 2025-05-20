# A list is an ordered, change-able (mutable) collection of items 
# written inside square brackets, separated by commas.
#-----------------------------------> List Methods<-----------------------------------
my_list = [1, "hello", 3.14, True]
print(my_list[3])
# List Comprehension
x = ['even' if i % 2 == 0 else 'odd' for i in range(6)]
print(x)
x = [i*i for i in range(5)]
print(x)
y=[i for i in range(10) if i % 2 == 0]
# Output: [0, 2, 4, 6, 8]
print(y)
z=[i**2 for i in range(10) if i % 2 == 1]
# Output: [1, 9, 25, 49, 81]
#-----------------------------------> List Exericse<-----------------------------------
print(z)
nums = [7, 2, 5, 9, 2]
nums.append(4)
nums.insert(0, 0)
nums.remove(2)
print("Index of 9:", nums.index(9))
nums.sort()
print("Sorted:", nums)
print("Reversed copy:", nums[::-1])

# Exercise ------->2
a = ['data', 'science']
b = ['is', 'fun']
c = a + b
print(c)               
print(c.count('data')) 

# Exercise ------->3
nested = [1, [2, 3], 4]
print(nested[1][1])  # First go to index 1 (list), then index 1 inside that
