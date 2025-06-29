# LAMBDA FUNCTIONS
'''Functions without anmes are called lambda functions, and also know as Anonymos functions,
 that can be defined in single line of code'''

# Syntax
f=lambda a:a*a
# Differnce B/w Normal Function & Lambda Function
# Lambda Has no return value
# Lambda function returns functins not return value
# One line
# Not Used for code Useablility
# No name Lambda 

def returnList(func,l):
    result=0
    for i in l:
        if func(i):
            result+=i
    return result

l=[2,3,4,6,78,9,1,3]
even=lambda x:x%2==0
odd=lambda x:x%2!=0
diV3=lambda x:x%3==0
print('Even: ',returnList(even,l))
print('Odd :',returnList(odd,l))
print('Div3 :',returnList(diV3,l))

# MAP functions in lambda 
'We used it when we have to transform each values'
m=[2,3,4,6,78,9,1,3]
squared=list(map(lambda x:x**2,m))
print(squared)
l=[2,4,5,6,7,8]
x=list(map(lambda x:x*2,l))
print(x)
# Checking Even List using Map function
l=[2,4,5,6,7,8]
x=list(map(lambda x:x%2==0,m))
print(x)
# Checking for List Attributes in Dictiorary:
people = [
    {"name": "Ali", "father_name": "Ahmed", "address": "1234 Street, City, Country"},
    {"name": "Sara", "father_name": "Hassan", "address": "5678 Avenue, City, Country"},
    {"name": "Zain", "father_name": "Bilal", "address": "91011 Road, City, Country"}
]
x=list(map(lambda people:people['name'],people))
y=list(map(lambda people:people['address'],people))
z=list(map(lambda people:people['father_name'],people))
print('Names are:=',x)
print('Address are:=',y)
print('father_names are:=',z)


'Keeps only those items that pass a condition (i.e., function returns True).'
m=list(map(lambda person:'Ahmed' in person.values() ,people))
print(m)
# Filter Lambada functions
num=[232,3,5,68,53,6,8,5,9]
chec=list(filter(lambda x:x<9,num))
print(chec)
# Reduce Lambda Function
'Have to import it from functools '
import functools as fuc
lis=[1,2,3,5,6,6]
res=fuc.reduce(lambda x,y:x+y,lis)
print(res)
number=[232,3,5,68,53,6,8,500,9]
ress=fuc.reduce(lambda x,y:x if x>y else y,number)
print(ress)
nums = [1, 2, 3, 4]
product = fuc.reduce(lambda x, y: x * y, nums)
print(product)  # 24

##################################################################Exercise-->################################################# 
l=[1, 2, 3, 4, 5]
check=list(map(lambda x:x**2,l))
print(check)

odd=[1, 2, 3, 4, 5, 6]
check=list(filter(lambda x:x % 2 == 0,odd))
print(check)

tax=[100, 200, 300]
tax_check=list(map(lambda x:x+10,tax))
print(tax_check)

import functools as fuc
mul=[1, 2, 3, 4]
ress=fuc.reduce(lambda x,y:x*y,mul)
print(ress)

name_check=["Majesty", "Royal", "Magic", "King", "Moon"]

check=list(filter(lambda names:names[0]=='M',name_check))
print(check)