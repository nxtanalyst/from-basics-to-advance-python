# # Problem: Given a list of numbers, count how many are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# postive=0
# negative=0
# for i in numbers:
#     if i<0:
#         print(f'Number is Negative={i}',)
#         postive+=1
#     else:
#         print(f'Number is Postive={i}')
#         negative+=1
# print(f'Total Positive Numbers = {postive}')
# print(f'Total Negative Numbers = {negative}')

# # #2. Sum of Even Numbers
# # Problem: Calculate the sum of even numbers up to a given number n.
# num=int(input('Enter your number =>'))
# sum=0

# for i in range(num):
#     if i%2==0:
#         sum+=i
# print(sum)
# # 3. Multiplication Table Printer
# # Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
# numb_up=10
# ask=int(input('Enter your number =>'))
# j=1
# for i in range(1,numb_up+1):
#     if i==5:
#         continue
#     j=ask*i
#     print(f'{ask}*{i}={j}')

# # 4. Reverse a String
# # Problem: Reverse a string using a loop.
# asked=input('Enter your word -->')
# empty_str=''
# for char in asked:
    
#     empty_str=char +empty_str
    
# print(empty_str)

# Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.
input_str='teeter'
for char in input_str:
    print(char)
    if input_str.count(char)==1:
        print("Char is",char)
        break

