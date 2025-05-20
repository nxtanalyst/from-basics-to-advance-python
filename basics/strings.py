# A string in Python is a sequence of characters enclosed in single, double, or triple quotes.

chai='Masla Chai'
first_char=chai[0]
print(first_char)
#now have to extrac masla from Masla chai
slice_chai=chai[0:6]
print(slice_chai)
print(chai[::-1])
#-----------------------------------> String Methods<-----------------------------------

str2="hey there"
print('these is for strip method: ',str2.strip())
print('these is for Replace method: ',str2.replace('hey','Hi'))
print('these is for Spilt method: ',str2.split(" "))
print('these is for Captilize method: ',str2.capitalize())
print('these is for Center method: ',str2.center(50))
print('these is for Count method: ',str2.count('e'))
print('these is for Endswith method: ',str2.endswith('there'))
print('these is for Find method: ',str2.find('ne'))
print('these is for Index method: ',str2.index('there'))
print('these is for Isalnum method: ',str2.isalnum())
print('these is for isaplpha method: ',str2.isalpha())
print('these is for Isprintable method: ',str2.isprintable())
print('these is for Isupper method: ',str2.isupper())
print('these is for Islower method: ',str2.islower())
print('these is for Stratwith method: ',str2.startswith('hey'))
print('these is for Swapcase method: ',str2.swapcase())
print('these is for title method: ',str2.title())
print('these is for Join method: ',",".join(str2))

#-----------------------------------> Exercise<-----------------------------------
text = "I am learning Python"
print(text[0],text[-1])
print(text[5:13])
print(text[::-1])
print('Python' in text)
# if "Python" in text:
#     print("True")
# else:
#     print('False')
text2= " Strings are fun"
print(text+text2)
# -----------------------------------> Exercise-2<-----------------------------------
sentence = "   Python is Awesome and python is Fun   "
print(sentence.lower())
print(sentence.strip())
print(sentence.replace('Python','coding'))
print(sentence.count('is'))
# print(sentence.split(' '))
print(sentence.strip().split())








