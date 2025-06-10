# . Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).
age=int(input("Provide me the age=>"))

if age<13:
    print('The age Lise in Group "Child"')
elif 13<=age<=20:
    print('The age Lise in Group "Teenager"')
elif 20<=age<=60:
    print('The age Lise in Group "Adult"')
elif age>60:
    print('The age Lise in Group "Senior"')


# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.


