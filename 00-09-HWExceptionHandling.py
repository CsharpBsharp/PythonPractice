"""
#To see complete pylint report use pylint your filename -r y
Errors and Exceptions Homework
Problem 1
Handle the exception thrown by the code below by using try and except blocks.

for i in ['a','b','c']:
    print(i**2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-c35f41ad7311> in <module>()
      1 for i in ['a','b','c']:
----> 2     print(i**2)

TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
Problem 2
Handle the exception thrown by the code below by using try and except blocks. Then use a finally
block to print 'All Done.'

x = 5
y = 0
​
z = x/y
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-2-6f985c4c80dd> in <module>()
      2 y = 0
      3
----> 4 z = x/y

ZeroDivisionError: division by zero
Problem 3
Write a function that asks for an integer and prints the square of it. Use a while loop with a
try, except, else block to account for incorrect inputs.

def ask():
    pass
ask()
Input an integer: null
An error occurred! Please try again!
Input an integer: 2
Thank you, your number squared is:  4
"""

# Problem 1
for i in ['a', 'b', 'c']:
    try:
        print(i ** 2)
    except TypeError:
        print("Well sorry to bust your bubble we got String here dude! instead of integer")

# Problem 2
    try:
        x = 5
        y = 0
        z = x/y
    except ZeroDivisionError:
        print("Son you just F'ed it up and divided a number by zero how dare you!")
    finally:
        print("All Done!")


# Problem 3
def ask():
    while True:
        try:
            userinput = int(input('Enter and integer :'))
            print(f'Thank you, your number squared is : {userinput ** 2}')
            break
        except ValueError:
            print('An error occurred! Please try again!')


ask()


