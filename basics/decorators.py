# Before getting to decorators must know about CLosure
def outerFunc():
    msg='Hi from Outer'

    def inner_function():
        print(msg)
    
    return inner_function()

outerFunc()
# DECORATORS
'''A decorators are specical functions that return a new function as an arguement and return a new fucntions that modifies the
behaviour of orignal functions'''

def decorator_function(oringalFuc):# here decorator_function() is an HOF functions which takes 
    def wrapper_function(*args,**kwargs):
        print(f'wrapper executed these before {oringalFuc.__name__}')
        return oringalFuc(*args,**kwargs)
    return wrapper_function
# @decorator_function
def display():
    print('Display function ran')

@decorator_function
def display_info(name,age):
    print(f'display info ran with arguments {name} {age}')
decorated_display=decorator_function(display)
decorated_display()
display_info('Kamal',25)
display()

class decroator_class(object):
    def __init__(self,orignal_fuc):
        self.orignal_fuc=orignal_fuc
    
    def __call__(self, *args, **kwargs):
        print(f'call method executed these before {self.orignal_fuc.__name__}')
        return self.orignal_fuc(*args, **kwargs)

@decroator_class
def display():
    print('Display function ran')

@decroator_class
def display_info(name,age):
    print(f'display info ran with arguments {name} {age}')

display_info('Kamal',25)
display()

def mylogger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    def wrapper (*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper
def my_timer(orig_func):
    import time

    def my_timer(orig_func):

        import time
        def wrapper(*args, **kwargs):
            t1=time.time()
            result=orig_func(*args, **kwargs)
            t2=time.time()-t1
            print('{} ran in: {} sec'.format(orig_func.__name__, t2))
            return result
        
        return wrapper

@mylogger
def display_info(name,age):
    print(f'display info ran with arguments {name} {age}')

display_info('Mishi',7)

import time
def cache(func):
    cache_value={}
    print(cache_value)
    def wrapper(*args):
        
        if args in cache_value:
            return cache_value[args]
        result=func(*args) #orignal function is been called
        cache_value[args]=result
        print('Here is result before executing the result',result)
        print(cache_value)
        return result

    return wrapper



@cache
def long_running_func(a,b):
    time.sleep(4)
    return a+b
print(long_running_func(4,6))
print(long_running_func(2,7))
print(long_running_func(4,6))

def deco(func):
    def wrapper():
        return func()
    
    return wrapper


@deco
def my_func_1():
    print('Function is being called')
@deco
def my_func_2():
    print('Hello, Majesty!')

my_func_1()
# my_func_2()
def decorator_Upper(func):
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        return result.upper()
    
    return wrapper

@decorator_Upper
def capitlize_func(word):
    return word

print(capitlize_func('kamal'))
###############################################3############################################## 
def decora_twice(func):
    def wrapper():
        func()
        func()
        return
    
    return wrapper

@decora_twice
def func_twice():
    print('Hello')

func_twice()

import time
def time_chec(func):
    def wrapper(*args,**kwargs):
        t1=time.time()
        result=func(*args,**kwargs)
        duration = time.time() - t1
        print(f"⏱ Function '{func.__name__}' executed in {duration:.5f} seconds.")
        return result
    
    return wrapper

@time_chec
def funct(a,b):
    time.sleep(0.5)
    if a%b==0:
        return f'Even'
    return 'No means No'

print(funct(4,2))
print(funct(8,2))
print(funct(3,2))
def check_access(role_required):
    def decorator(func):
         def wrapper(user_role):
            if user_role.lower() != role_required.lower():
                print(f"Access Denied! '{user_role}' cannot enter the royal court.")
            else:
                print(f"Access Granted! Welcome, {user_role.title()}.")

                return func(user_role)
            
         return wrapper 
    
    return decorator
        
@check_access("Admin")  # Only 'king' can access this function
def enter_court(role):
    print("Welcome, Majesty!")

# Testing with different roles
ask=input('what is your Acess point: ')
enter_court(ask)

import time
def measure_time(func):
     def wrapper(*args,**kwargs):
          start=time.time()
          result = func(*args, **kwargs)
          end=start-time.time()
          print(f"Execution Time: {end - start:.5f} seconds")
          return result
     return wrapper

def check_access(role_required):
        def decorator(func):
            def wrapper(user_role):
                if user_role.lower() != role_required.lower():
                 print(f"Access Denied! '{user_role}' cannot enter the royal court.")
                else:
                    print(f"Access Granted! Welcome, {user_role.title()}.")
                    return func(user_role)
            return wrapper
        return decorator    
    

@measure_time
@check_access("king")  # Only the king can run royal commands
def royal_command(role):
    # Simulate heavy royal work
    for i in range(1, 6):
        print(f"Command {i} executed.")
        time.sleep(2)

ask=input('what is your Acess point: ')
royal_command(ask)


def limit_attempts(max_attempts):
    def decorator(func):
        failed_attempts = [0]
        access_blocked = [False]

        def wrapper(*args, **kwargs):
            if access_blocked[0]:
                print("❌ Access blocked after 3 failed attempts.")
                return

            while failed_attempts[0] < max_attempts:
                username = input("Enter username: ")
                if username == "Majesty":
                    print("✅ Welcome, Majesty!")
                    failed_attempts[0] = 0  # Reset after success
                    return func(username)
                else:
                    failed_attempts[0] += 1
                    print("❌ Invalid login.")
            
            access_blocked[0] = True
            print(f"🚫 Access blocked after {failed_attempts} failed attempts.")

        return wrapper
    return decorator

@limit_attempts(3)
def login(username):
    print(f"Logged in as: {username}")
    
login()

def sanitize_input():
    def decorator(func):
        def wrapper(name,*args, **kwargs):
            cleaned_name = name.strip().title()
            return func(cleaned_name, *args, **kwargs)
        
        return wrapper
    return decorator
            

@sanitize_input()
def greet_user(name):
    return f"Welcome, {name}!"

print(greet_user('  saTasdas'))
