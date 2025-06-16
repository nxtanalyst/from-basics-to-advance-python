# num=5
# fact=1

# while num>0:
#     fact=fact*num
#     num-=1

# print(f'Factorial Given number is: {fact}')

# asking = int(input('Enter number b/w 1 to 10 --> '))
# while 0 < asking < 10:
#     print(asking)
#     # asking = int(input('Enter number b/w 1 to 10 --> '))

# count=1
# while count<=12:
#     if count%2==0:
#         print(count)
#     count+=1
# while True:
#     ask=input('Enter the Word-->')
#     if isinstance(ask, str):
#         print(ask[::-1])
#         break
    
#     else:
#         print('Invalid String')
fact=1
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



