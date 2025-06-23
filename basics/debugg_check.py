# # num=5
# # fact=1

# # while num>0:
# #     fact=fact*num
# #     num-=1

# # print(f'Factorial Given number is: {fact}')

# # asking = int(input('Enter number b/w 1 to 10 --> '))
# # while 0 < asking < 10:
# #     print(asking)
# #     # asking = int(input('Enter number b/w 1 to 10 --> '))

# # count=1
# # while count<=12:
# #     if count%2==0:
# #         print(count)
# #     count+=1
# # while True:
# #     ask=input('Enter the Word-->')
# #     if isinstance(ask, str):
# #         print(ask[::-1])
# #         break
    
# #     else:
# #         print('Invalid String')

# # while True:
# #     ask=input('Bot: ')
# #     if ask=='bye':
# #         break
# #     else:
# #         print('You:',ask)
# #         continue

# # while True:
# #     ask=int(input('Enter the num-->'))
# #     if ask==1:
# #         print(f'Factorial of Num is {ask}')
# #         break
# #     elif ask==0:
# #         print(f'Factorial of Num is 1')
# #         break
# #     else:
# #         fact = 1
# #         for i in range(1, ask + 1):
# #             fact *= i
# #         print(f'Factorial of Num is {fact}')
# #         break

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

# def primes_up_to_n(n):
#     sieve = [True] * (n + 1)
#     sieve[0:2] = [False, False]

#     for i in range(2, int(n**0.5) + 1):
#         if sieve[i]:
#             for j in range(i * i, n + 1, i):
#                 sieve[j] = False

#     return [i for i, is_prime in enumerate(sieve) if is_prime]

# x=primes_up_to_n(100)
# print(x)

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

# import time 
 
# start = time.time() 
 
# def fib(numb):
#     if numb==0:
#         return 0
#     elif numb==1:
#         return 1
#     else:
#         return fib(numb-1)+fib(numb-2)

# ask=int(input('Enter your number: '))
# result=fib(ask)
# after = time.time()
# print("Result:", result)
# print("Start Time:", start)
# print("End Time:", after)
# print("Execution Time (seconds):", after - start)    

player_score={}

with open("scores.csv", "r") as f:
    for line in f:
        tokens=line.split(',')
        player=tokens[0]
        score=int(tokens[1])
        print(tokens)
        print(player)
        
        if player in player_score:
            player_score[player].append(score)
        else:
            player_score[player]=[score]


for player, score_list in player_score.items():
    max_score=min(score_list)
    min_score=min(score_list)
    avg_score=sum(score_list)/len(score_list)
    print(f"{player}==>Min:{min_score}, Max:{max_score}, Avg{avg_score}")