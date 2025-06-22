# '''Funtions is block of code it rums when its called 
#     it enhance reusadblity  ,make program more readable'''
# def say_hello():
#     print("Welcome to Python Functions!")

# say_hello()

# def greet(name):
#     print(f'Hello, {name}')
# # Output: Hello, Kamal!

# greet('Kamal')


# def add(a,b):
#     return a+b

# result=add(3,7)
# print(result)

# def  multiply_and_return(c,d):
#     return c*d

# res=multiply_and_return(7,3)
# print(res)

# def mul(p1,p2):
#     return p1*p2

# print(mul(2,3))
# print(mul(2,'b'))
# print(mul('a',3))

# import math
# def circle_stats(radius):
#     area= round(math.pi*radius**2,2)
#     circumference=round(math.pi*radius,2)
#     return f'Area={area},\nCircumference={circumference}'

# circle_stats_var=circle_stats(4)
# print(circle_stats_var)


# def mult_total(exp):
#     mult_total=1
#     for item in exp:
#         mult_total*=int(item)
#     return mult_total

# n1 = input("Enter the expense list for addition: ").split(',')
# n2 = input("Enter the expense list for addition: ").split(',')

# addition_total = mult_total(n1)
# print("Total expense for list 1:", addition_total)

# addition_total = mult_total(n2)
# print("Total expense for list 2:", addition_total)
# # print(help(mult_total))
# '''⚔️ Challenge 1: Even or Odd Counter
# Problem:
# Write a function count_even_odd(numbers) that takes a list of numbers and prints how many are even and how many are odd'''
# def count_even_odd(*num):
#     Even_num=0
#     odd_num=0
#     for i in num:
#         if i%2==0:
#             Even_num+=1
#         else:
#             odd_num+=1
#     return f'Even: {Even_num}, Odd: {odd_num}'

# x = count_even_odd(1, 2, 3, 4, 5, 6)
# print(x)
# # '''⚔️ Challenge 2: Palindrome Checker
# # Problem:
# # Write a function is_palindrome(word) that checks if the word is a palindrome (same forward and backward).'''

# def is_palindrome(word):
#     if word[::-1]==word:
#         return f'Yes plaindrome: {word[::-1]}'
#     else:
#         return f'No plaindrome: {word}'

# xyz=is_palindrome('kamak')
# print(xyz)

# '''⚔️ Challenge 3: Count Vowels in a Sentence
# Problem:
# Create a function count_vowels(sentence) that counts how many vowels are in the sentence.

# '''
# # count_vowels("Majesty rules the code!")  # Output: 8
# def count_vowels(sentence):
#     count=0
#     for i in sentence:
#         if i=='a'or i=='e' or i=='i' or i=='o'or i=='u':
#              count += 1
#     return  count
    

 

# vowels=count_vowels("Majesty rules the code!")  # Output: 8

# print(vowels)

# '''💡 1. Sum of Digits of a Number
# Problem:Ask the user to input a number. Write a function that calculates the sum of its digits.'''
# # # Example Input: 1234
# # Output: 1 + 2 + 3 + 4 = 10
# def sum_digit(num):
#     count=0
#     x=str(num)
#     for i in x:
#         count+=int(i)
    
#     return count

# result=sum_digit(1234567)
# print(result)

# '''💡 2. Check Prime Number
# Problem:Write a function is_prime(n) that returns whether a number is prime or not. Ask the user for input.'''

# def prime_checker(numb):
#     if numb<=1:
#         return  f'Number is Not prime: {numb}'
#     for i in range(2, int(numb**0.5) + 1):
#         if numb%i==0:
#             return f'Number is Not prime: {numb}'
    
#     return f'Yes Number is prime: {numb}'

# result_1=prime_checker(5)
# result_2=prime_checker(9)
# result_3=prime_checker(10)
# result_4=prime_checker(7)
# result_5=prime_checker(13)
# print(result_1)
# print(result_2)
# print(result_3)
# print(result_4)
# print(result_5)

# ''' 3. Word Frequency Counter
# Problem:Ask the user to input a sentence. Write a function that returns a dictionary of each word and its frequency.'''
# # Input: "hello world hello"
# # Output: {'hello': 2, 'world': 1}

# def frequecny_counter(n1):
#     new_dict={}
#     word=n1.split()
#     for subwords in word: # ['Python', 'is', 'a', 'versatile', 'language.']
#         if subwords in new_dict:
#             new_dict[subwords]+=1
            
#         else:
#             new_dict[subwords]=1
#     return new_dict

# result=frequecny_counter("hello world hello")
# print(result)




# def fib(numb):
#     if numb==0:
#         return 0
#     elif numb==1:
#         return 1
#     else:
#         return fib(numb-1)+fib(numb-2)

# ask=int(input('Enter your number: '))
# result=fib(ask)
# print(result)


# #  fo =f0 and f1=0+1=1, f2=1+2=3 , f3=3+3=6, f4=4+3=7, f5=5+7=12

# def password_checker(passw):
#     has_special = any(not char.isalnum() for char in passw)
#     if len(passw)>=8 and passw.isalnum() and has_special:
#         return f'Yes password has 8 charas and have number as well'
    
#     return 'Password does not supports password criteria'

# ask=input('Enter your password: ')
# result=password_checker(ask)
# print(result)

# def print_kwargs(**kwargs):
#     for key,value in kwargs.items():
#         return f'{key}: {value}'

# xyz=print_kwargs(Fname='Kamal',lastName='Hussain')
# x=print_kwargs(Fname='Zoya',lastName='Haider')
# z=print_kwargs(Fname='Fariyal',lastName='Wali')
# print(xyz)
# print(x)
# print(z)
'''🧭 What Is yield?
In simple words:
return → gives one final value and ends the function.
yield → gives one value at a time, pauses the function, and resumes later from where it left off.
It's like a pause button for functions.'''

# def even_generator(limit):
#     for i in range(2,limit+1,2):
#         yield i
# x=even_generator(10)
# for num in x:
#     print(num)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) # 6*fac(5)--->fac(5)-->fac(4)-->fac(3)-->fac(2)-->fac(1)

xl=factorial(6)
print(xl)