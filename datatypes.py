#Python uses single quotes ('), double quotes ("), triple single quotes (''') and triple-double quotes (""") to denote a string literal.
"""
s = 'This is a string'
print(s)
s = "Another string using double quotes"
print(s)
s = ''' string can span
        multiple line '''
print(s)
"""

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
"""
name = 'Manuel Marigi'
age = 26

print(name)                    #Outputs the name.
print(len(name))               #Outputs the length of the name.
print(f'My name is {name}.')
print(f'I am {age} years old') #Same as print('I am '+ str(age) +' years old.)
print(name.upper())            #Returns upper case
print(name[3])                 #Prints the character specified.
print(name.find('l'))          #will output the index of the first 'l' in the string assigned to the variable name. If there is no 'l' in the string, it will print -1.
"""

#Using Backslash in Python.
"""
comment = 'Performed \nExcellently!'

print(comment) #Outputs Excellently on a new line.


task_completed = 'Went\tto\tthe\tgym.'  # \t is a space tab.
task_completed_spaces = task_completed.replace('\t', ' ')

print(task_completed_spaces) #Task_completed_spaces has been used to help replace the number of spaces if task_completed is run as is.


MyName = '"My name\'s Marigi," he said.'

print(MyName) #The backslash escapes the single quote that is inside another single quote.


s = r'\n'

print(s)  # s is a raw string defined by the prefix r. \n is treated as a literal character.



colors = ['red','green','blue']

print(f'The RGB colors are:\n {'\n'.join(colors)}')  
          #Output: SyntaxError: f-string expression part cannot include a backslash
          #An f-string cannot contain a backslash character as a part of the expression inside the curly braces {}.

colors = ['red','green','blue']
rgb = '\n'.join(colors)

print(f"The RGB colors are:\n{rgb}") #Fixed to give correct output.



long_statement = "This is a very long statement that needs to be " \
                 "broken into multiple lines for better readability. " \
                 "Using the backslash allows you to continue the " \
                 "statement on the next line without causing any errors."

print(long_statement)  #Using the backslash \ to split a long statement across multiple lines


import keyword

print(keyword.kwlist)  #Provides the current keyword list
"""

#String Concatenation
"""
s1 = 'String'
s2 = 'Concatenation'

print(f'{s1} {s2}')              #Using f-string to concatenate.
print(' '.join([s1, s2]))        #Using join()

mycar, myhouse, mysalary = "Mercedes", "storey", 1000000
formatted_salary = '{:,}'.format(mysalary)

print(f'I drive a {mycar}, live in a {myhouse} house, and earn ${formatted_salary} a year')
print(', '.join([mycar, myhouse, str(formatted_salary)]))
"""

str = "Python String"
new_str = 'J' + str[1:]

print(new_str) #Replacing a string character.