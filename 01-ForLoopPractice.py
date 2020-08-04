#EXAMPLE 1 for with string
print('String Iteration')
for letter in 'This is a great day':
    print(letter)


#Example 2 for with List
#range syntax is range(start,stop,step)
print('List iteration Example')
list1=range(1,11)  #Using range generator to create list of 1 to 10.
list2=['Nazia','Adnan','Lubna','Hira']
print(sorted(list2))  #This will return sorted list object but original list won't be touched.
print(list2)
list2.sort() #This will do in place sorting
print(list2)
for item in list1:
    print(item)

print()

#Example 3 showing we can use range directly wit the for as it returns list
print('List Generation using random generator and iteration')
for item in range(0,11,2): ##This is going to print number in increment of 2 as step is 2. Starting from 0.
    print(item)

#Example 4 Take input from starting and ending value from user.
#There are two input functions in Python 2.x, input and raw_input. Mostly input is used but it has the capability to expand the
#expression. While raw_input shows input as is
#Starting from Python 3.x input is same as 2.x raw_input and input that evaluated input has been removed.
print('Another range generator example with input taken from user')
start= int(input('Enter the value for start: '))
stop = int(input('Enter the value for stop : '))
step = int(input('Enter the value for step : '))

for item in range(start,stop,step):
    print(item)

#Example 5 Tuple Unpacking
print('Tuple Unpacking Example:')
mylist = [(1,2),(3,4),(5,6),(7,8)]
for t1,t2 in mylist:
    print(t1)
    print(t2)

##Dictionary and for loop

#Print keys only default behavior
print('Default printing of Dictionary Object which prints only keys')
for item in {'key1':'value1','key2':'value2','key3':'value3'}:
    print(item) #This will print key

#Print keys and values as tuples
print('Print using item() method of dictionary which produces Tuples')
for item in {'key1':'value1','key2':'value2','key3':'value3'}.items():
    print(item) #This will print key

#Below feature is called DICTIONARY UNPACKING where dictionary allows to separate key and value using 2 variables.
#Print keys and values
print('This uses similar concept as TUPLE Unpacking but it is called Dictionary Unpacking')
for x,y in {'key1':'value1','key2':'value2','key3':'value3'}.items():
    print(x) #This will print key
    print(y)

#Print keys only exclusively
print('print keys')
for item in {'key1':'value1','key2':'value2','key3':'value3'}.keys():
    print(item) #This will print key

#Print values only exclusively
print('Print values')
for item in {'key1':'value1','key2':'value2','key3':'value3'}.values():
    print(item) #This will print values

#Running Tally
# Start sum at zero
list_sum = 0
for num in range(1,11):
    list_sum += num
print(list_sum)

#Print Even numbers and Odd Number
for num in range(0,11):
    if num % 2 == 0 and num != 0:
        print (f"Even Number:{num}")
    else:
        print(f"Odd Number:{num}")
