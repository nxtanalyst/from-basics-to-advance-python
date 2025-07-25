class Fraction:
    def __init__(self,nenomenitor,deniomintor):
        self.nenomenitor=nenomenitor
        self.deniomintor=deniomintor
    def __str__(self):
        return f'Hi from Str: {self.nenomenitor}/{self.deniomintor}'
    def __add__(self,other):
        temp_den=self.nenomenitor*other.deniomintor+other.nenomenitor*self.deniomintor
        temp_nen=self.deniomintor*other.deniomintor
        return f'{temp_den}/{temp_nen}'
    def __sub__(self,other):
        temp_den=self.nenomenitor*other.deniomintor-other.nenomenitor*self.deniomintor
        temp_nen=self.deniomintor*other.deniomintor
        return f'{temp_den}/{temp_nen}'
    def __mul__(self,other):
        temp_den=self.nenomenitor*other.nenomenitor
        temp_nen=self.deniomintor*other.deniomintor
        return f'{temp_den}/{temp_nen}'
    
    def __truediv__(self,other):
        temp_den=self.nenomenitor*other.deniomintor
        temp_nen=self.deniomintor*other.nenomenitor
        return f'{temp_den}/{temp_nen}'


x=Fraction(4,5)
y=Fraction(5,6)
print('Addition',x+y)
print('Substraction',x-y)
print('Multiplication',x*y)
print('Division',x/y)