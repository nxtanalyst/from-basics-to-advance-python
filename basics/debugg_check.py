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
