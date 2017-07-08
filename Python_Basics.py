
# coding: utf-8

# In[33]:

# This is a Python Comment
"""adsfsd
This is multi-line comment
"""

# Declaration/Initialization
answer = 44
answer = "The answer is 44."

# Data Types
number = 1.1
print number
string = "Strings can be declared with single or double quotes."
print string
list = ["List can have", 1, 2, 3, 4, "or more types together!"]
print list
tuple = ("Tuples","Can", 4 , 5, "Elements!")
print tuple
dictionary = {'one' : 1, 'two' : 2, 'three' : 3}
print dictionary
varaible_with_zero_data = None


# Conditionals
def condition(cake):
    if cake == "delicious":
        return "Yes please!"
    elif cake == "okay":
        return "I'll have a small piece."
    else:
        return "No, thank you."
condition("delicious")


# Loops
for item in list:
    print item
    
total = 0
while (total < 50):
    total += 10
print total


# Functions
def divide(dividend,divisor):
    quotient = dividend/divisor
    remainder = dividend % divisor
    return quotient, remainder

def calculate_stuff(x, y):
    (q,r) = divide(x, y)
    print q,r
    
calculate_stuff(200,3)

# Classes

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def birthday(self):
        self.age += 1

