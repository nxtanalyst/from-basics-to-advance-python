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

