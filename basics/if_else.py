# import datetime

# current_date = datetime.datetime.now()
# full_weekday = current_date.strftime("%A")
# abbreviated_weekday = current_date.strftime("%a")
# # . Age Group Categorization
# # Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).
# age=int(input("Provide me the age=>"))

# if age<13:
#     print('The age Lise in Group "Child"')
# elif 13<=age<=20:
#     print('The age Lise in Group "Teenager"')   
# elif 20<=age<=60:
#     print('The age Lise in Group "Adult"')
# elif age>60:
#     print('The age Lise in Group "Senior"') 


# # 2. Movie Ticket Pricing
# # Problem: Movie tickets are priced based on age: $12 for adults (18 and over),
# # $8 for children. Everyone gets a $2 discount on Wednesday.

# age=int(input("Provide me the age=>"))
# price_for_adults=12
# price_for_child=8



# if full_weekday=="Wednesday" and  age>=18:
#         discount_price=price_for_adults-2
#         print(f'Group is adults {discount_price}')

# elif full_weekday=="Wednesday" and  age<18:
#     discount_price=price_for_child-2
#     print(f'Group is child {discount_price}')

# elif age >= 18:
#     print(f'Group is adult, ticket price is ${price_for_adults}')
# else:
#     print(f'Group is child, ticket price is ${price_for_child}')
     
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).
ask=int(input("Enter your marks==>"))

if 90<=ask<=100:
     print("Congartulation you got the Grade 'A'")
elif 80<=ask<=89:
     print("Congartulation you got the Grade 'B'")
elif 70<=ask<=79:
     print("Congartulation you got the Grade 'C'")
elif 60<=ask<=69:
     print("Congartulation you got the Grade 'D'")
elif ask<60:
     print("Congartulation you got the Grade 'F'")
else:
      print("Invalid input! Please enter marks between 0 and 100.")

     
     
     