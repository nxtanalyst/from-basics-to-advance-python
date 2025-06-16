# Problem: Given a list of numbers, count how many are positive.
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
postive=0
negative=0
for i in numbers:
    if i<0:
        print(f'Number is Negative={i}',)
        postive+=1
    else:
        print(f'Number is Postive={i}')
        negative+=1
print(f'Total Positive Numbers = {postive}')
print(f'Total Negative Numbers = {negative}')

# #2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.
num=int(input('Enter your number =>'))
sum=0

for i in range(num):
    if i%2==0:
        sum+=i
print(sum)
# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
numb_up=10
ask=int(input('Enter your number =>'))
j=1
for i in range(1,numb_up+1):
    if i==5:
        continue
    j=ask*i
    print(f'{ask}*{i}={j}')

# 4. Reverse a String
# Problem: Reverse a string using a loop.
asked=input('Enter your word -->')
empty_str=''
for char in asked:
    
    empty_str=char +empty_str
    
print(empty_str)

Find the First Non-Repeated Character
Problem: Given a string, find the first non-repeated character.
input_str='teeter'
char_count={}

for char in input_str:
    #print(char)
    if char in char_count:
        char_count[char]+=1      
        # char_count[char] = char_count[char] + 1
    else:
        char_count[char]=1
#  Second Loop to vlaidate the count in char_count

for char in input_str:    #char_count{t:2,e:3,r:1}
    if char_count[char]==1:
        print(f'First non Repeated Character is {char}')
        break
else:
        print("No non-repeated character found.")
'''okay what I am understanding up to now is first char=s so will go to else of first loop 
than char_count = {s:1} after  char=w than char_count = {s:1,w:1}
after char=i than char_count = {s:1,w:1,i:1,s:1,s:1}  so now first loop completes 
now second loops runs it will check  if char_count[char] == 1: than will give the first non repeated char and break
'''

# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

input_strr=6 # 6 *5*4*3*2*1

num=5
fact=1

while num>0:
    fact=fact*num
    num-=1

print(f'Factorial Given number is: {fact}')

asking = int(input('Enter number b/w 1 to 10 --> '))
while 0 < asking < 10:
    print(asking)
    # asking = int(input('Enter number b/w 1 to 10 --> '))

count=1
while count<=12:
    if count%2==0:
        print(count)
    count+=1
'''1. 🔄 Reverse a String
Goal: Ask the user for a word and print it in reverse using a while loop.'''
while True:
    ask=input('Enter the Word-->')
    if isinstance(ask, str):
        print(ask[::-1])
        break
    
    # else:
    #     print('Invalid String')
'''2. 💬 Mini Chatbot Loop
Goal: Keep chatting until the user types "bye".'''
while True:
    ask=input('Bot: ')
    if ask=='bye':
        break
    else:
        print('You:',ask)
        continue
'''3. 🔢 Factorial Calculator
Goal: Ask the user for a number and calculate its factorial using a while loo'''
while True:
    ask=int(input('Enter the num-->'))
    if ask==1:
        print(f'Factorial of Num is {ask}')
        break
    elif ask==0:
        print(f'Factorial of Num is 1')
        break
    else:
        fact = 1
        for i in range(1, ask + 1):
            fact *= i
        print(f'Factorial of Num is {fact}')
        break

    # ask = int(input("Enter a number → "))
    # fact = 1
    # for i in range(1, ask + 1):
    #     fact *= i
    # print(f"Factorial of {ask} is {fact}")





