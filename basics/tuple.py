# my_tuple = (10, 20, 30, 20, 40, 50)
# Now do these:

# Print the length of the tuple.

# Access the third element.

# Slice the tuple to get (20, 30).

# Count how many times 20 appears.

# Find the index of 40.

# Loop through the tuple and print each item.

# Create a new nested tuple like this:
# nested = ("Data", (1, 2, 3), "Science"), then print 2 from the nested part.

#tuple is like a list, but immutable — meaning once created, you cannot change its elements.

my_tuple = (10, 20, 30, 20, 40, 50)
print(len(my_tuple))
print(my_tuple[3])
print(my_tuple[1:3])
print(my_tuple.count(20))
print(my_tuple.index(40))
for i in my_tuple:
    print(i)

nested = ("Data", (1, 2, 3), "Science")
print(nested[1][1])