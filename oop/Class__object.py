# Recap of Object Oreineted Programming
'''A class is a blueprint for object like we objects to mapping realworld scenarios'''
'''And an object is instance of a class created using blueprint'''
'''__init__ a special method which is used to intialzie the attributes of an objectg'''
'''Methods: Its defines the actions behaviour of a Object and these Methods belongs to Object and class'''

# Creating a class with Student Names

class Student:
    name='Mishi'
    def __init__(self,fullname):
        self.fullname=fullname
        
        print(f'Hi Students {self.fullname}')


s1=Student('Kamal Hussain')
print(s1.fullname)
print(Student.name)


# STATIC METHOD
'Static methods Does not use Self keyword they do not work at Object level they work at class level'










    

