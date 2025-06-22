# Closure and Scope in python are
'''who can access what, and when. '''
# and scope means Where can I use this variable?
x=5
def fuc():
    x=10
    print('Inside',x)

fuc()
print("Outside:", x)

def outer():
    msg = "Majesty rules!"

    def inner():
        print('Msg from Inner()',msg)  # This uses the 'msg' from outer()

    return inner  # Notice we're returning the function, not calling it

greet = outer()  # This gives us the inner() function
greet()          # Now we call inner()

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(f'Running "{func.__name__}" with arguments {args}')
        print(f'{func.__name__}={func(*args)}')
    return log_func

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)

def html_tag(tag):
  
  def wrap_text(msg):
        print(f"<{tag}>{msg}</{tag}>")  # using f-string
  return wrap_text


print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')
print(print_h1.__name__)

