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

# @decorator_function
# def display_info(name,age):
#     print(f'display info ran with arguments {name} {age}')
# decorated_display=decorator_function(display)
# decorated_display()
# display_info('Kamal',25)
# display()

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
        result=func(*args)
        cache_value[args]=result
        return result

    return wrapper



@cache
def long_running_func(a,b):
    time.sleep(4)
    return a+b
long_running_func(4,6)
