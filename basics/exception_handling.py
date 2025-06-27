# ################################################################################################################################ 
# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num
# except ZeroDivisionError:
#     print("Can't divide by zero.")
# ################################################################################################################################
# try:
#     with open('magic.txt','r') as f:
#         f.read()
# except:
#     print('File not found!')
# ################################################################################################################################
# try:
#     ask=int(input('ENter your age: '))
#     if ask<0:
#         raise ValueError("Age can't be negative!")
# except ValueError as e:
#     print("Caught error:", e)
# ################################################################################################################################

# try:
#     with open('data.txt','r') as f:
#         count=0
#         for word in f.read():
#             count+=1

# except:
#     print('No file found, Majesty.')
# try:
#         f=open('diary.txt','r')
#         # var=badvar 
#         if f.name=='diary.txt':
#               raise Exception

# # except Exception as e:
# #     print('Error as',e)

# except Exception as e:
#     print(e)
# except Exception as e:
#       print(e)
# else:
#       print(f.read())
#       f.close()
    
# finally:
#       print('I am executing the FINALLY')
        
         
               
      
# try:
#       while True:
#             ask=int(input('Enter The number:'))
#             if ask is not int:
#                   continue
# except Exception as e:
#       print(e)

# else:
#       print(ask)
# finally:
#       print('I am Executing')
# #######################################################1. Royal Calculator#########################################################


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
try:    

    a=int(input('Enter your First number : '))
    b=int(input('Enter your Second number : '))
    op = input("Choose operation (+, -, *, /): ")

    if op=='+':
        print("Result =", add(a, b))
    elif op=='-':
        print("Result =", sub(a, b))
    elif op=='/':
        print("Result =", div(a, b))
    elif op=='*':
        print("Result =", mul(a, b))
    else:
        print("Invalid operation!")


except ValueError:
    print('Values are not correct')
except ZeroDivisionError:
    print('Values can not divided by 0')
except Exception as e:
    print(e) 
# #######################################################Kingdom Entry Validator#########################################################

def check_passport(name, age):
    if not name:
        raise ValueError("Name is required!")
    if age<18:
        raise PermissionError("Minors not allowed in royal court!")
    print(f"Welcome to the royal court, {name}!") 
var=check_passport(12)
print(var)
try:
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    check_passport(user_name, user_age)
except ValueError as ve:
    print("Error",ve)

except PermissionError as pe:
    print("Access denied:", pe)
# #######################################################  🧪 3. Secret Scroll Reader'#########################################################
try:
    ask = input('Enter file name: ')
    with open(ask, 'r') as f:
        content = f.read()
        if content.strip() == '':
            raise ValueError("This scroll contains no knowledge!")
        print("📜 Scroll content:\n", content)
except FileNotFoundError:
    print("❌ Scroll not found!")
except ValueError as ve:
    print("⚠️", ve)
except Exception as e:
    print("Unexpected error:", e)


# #######################################################  4. Palace Messenger Chat (Loop Until 'exit'#########################################################
 
while True:
    try:
        ask=input('Enter your Msg: ')
        if ask.lower()=='exit':
            break
        elif ask.isdigit():
            raise TypeError("No numbers allowed in royal speech!")
        print('You',ask)
            
    except Exception as e:
        print('Error',e)
