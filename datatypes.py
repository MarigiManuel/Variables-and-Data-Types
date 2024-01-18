#Python Operators
"""
def subst_numbers(a,b):
    result = a / b
    return str(result)
result = subst_numbers(95, 3)
print(result)
"""

#Getting the Type
"""
x = 5
y = "John"
print(type(x))
print(type(y))
"""

#Output Variables
"""
x = 'Love'
print(x)

x = 'Python '
y = 'is '
z = 'interesting'
print(x + y + z)
"""

#Create a variable outside of a function, and use it inside the function

"""
x = "funny"
def my_gfd():
    print("My girlfriend is " + x)
my_gfd()  """

#Create a variable inside a function, with the same name as the global variable
"""
x = 'success.'
def myfunc():
  x = "rewarding."
  print("My coding will be " + x)
myfunc()  

print('My coding will be a ' +x)
"""


#Using  the type() function to determine the type of a variable.
"""
student_count = 1000
is_done = True
rating = 3.98
student_name = "Manuel"

print(type(student_count))
print(type(is_done))
print(type(rating))
print(type(student_name))
"""
#Working with strings and string methods

name = 'Manuel'
age = 26

print(name)                    #Outputs the name.
print(len(name))               #Outputs the length of the name.
print(f'My name is {name}.')
print(f'I am {age} years old') #Same as print('I am '+ str(age) +' years old.)
print(name.upper())            #Returns upper case
print(name[3])                 #Prints the character specified.
print(name.find('l'))          #will output the index of the first 'l' in the string assigned to the variable name. If there is no 'l' in the string, it will print -1.