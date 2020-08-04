import os
import datetime
import sys

##Case 1 Exclusive Create i.e if file exists throw error
##Shows how to create a file and have it in read and write mode
try:
	try:
		print("O o file already exists so I am going to try to remove it")
		os.remove('d:\\backup\\python\\pythonpractice\\ExclusiveFCreation.txt')
	except:
		print("Good we don't have file so lets create one using x+ mode")
		print("Unexpected error:", sys.exc_info()[0])
	with open('d:\\backup\\python\\pythonpractice\\ExclusiveFCreation.txt',mode='x+') as myxfile:
		#x+ and xt+ is same thing t is for text file. Other option is b which is for binary file.
		print('**Inside x+ section')
		print(myxfile.writable())
		print(myxfile.readable())
		myxfile.write("This is my first line.\n")
		myxfile.seek(0)
		print("**This will read full contents in one go using READ method")
		print(myxfile.read())
		print("**This will read only one line and will return string using READLINE method")
		myxfile.seek(0)
		print(myxfile.readline())
		print("**This will return list as READLINES method returns all rows in LIST object")
		myxfile.seek(0)
		print(myxfile.readlines())
except FileExistsError:
	print("Whoops you already created that file.")
except:
	print("Unexpected error:", sys.exc_info()[0])
	raise

##Case 2 WRITE i.e w+ mode
##Write to file using w mode. This mode truncates the file. We are using + with w which will also allow READ instead of just write. w overrites file or create a new one if doesn't exist
##NOTE: This will not throw file exist Error as last example did.

with open('d:\\backup\\python\\pythonpractice\\ExclusiveFCreation.txt', mode='w+') as myxfile:
	# x+ and xt+ is same thing t is for text file. Other option is b which is for binary file.
	print('**Inside w+ section')
	print(myxfile.writable())
	print(myxfile.readable())
	t=datetime.datetime.now()
	myxfile.write(f"This is my first line. Time is {t}.\n")
	myxfile.seek(0)
	print("**This will read full contents in one go using READ method")
	print(myxfile.read())
	print("**This will read only one line and will return string using READLINE method")
	myxfile.seek(0)
	print(myxfile.readline())
	print("**This will return list as READLINES method returns all rows in LIST object")
	myxfile.seek(0)
	print(myxfile.readlines())

##Case 3 READ i.e r+ mode which allows READ and WRITE but doesn't truncate file when it opens.
with open('d:\\backup\\python\\pythonpractice\\ExclusiveFCreation.txt', mode='r+') as myxfile:
	# x+ and xt+ is same thing t is for text file. Other option is b which is for binary file.
	print('**INSIDE r+ section')
	print(myxfile.writable())
	print(myxfile.readable())
	t=datetime.datetime.now()
	myxfile.read() ##THIS IS MOST IMPORTANT READ. IF NOT DONE SUBSEQUENT WRITE WILL START WRITING FROM OFFSET 0 MEANS
	#ESSENTIALLY OVERRITING THE CURRENT CONTENTS. READ TAKES SEEK TO END OF FILE.
	myxfile.write(f"This is my Second line. Time is {t}.\n")
	myxfile.seek(0)
	print("**This will read full contents in one go using READ method")
	print(myxfile.read())
	print("**This will read only one line and will return string using READLINE method")
	myxfile.seek(0)
	print(myxfile.readline())
	print("**This will return list as READLINES method returns all rows in LIST object")
	myxfile.seek(0)
	print(myxfile.readlines())
	print(myxfile.mode)

##Case 4 Append
with open('d:\\backup\\python\\pythonpractice\\ExclusiveFCreation.txt', mode='a+') as myxfile:
	# x+ and xt+ is same thing t is for text file. Other option is b which is for binary file.
	print('**INSIDE r+ section')
	print(myxfile.writable())
	print(myxfile.readable())
	t=datetime.datetime.now()
	myxfile.read() ##THIS IS MOST IMPORTANT READ. IF NOT DONE SUBSEQUENT WRITE WILL START WRITING FROM OFFSET 0 MEANS
	#ESSENTIALLY OVERRITING THE CURRENT CONTENTS. READ TAKES SEEK TO END OF FILE.
	myxfile.write(f"This is my Second line. Time is {t}.\n")
	myxfile.seek(0)
	print("**This will read full contents in one go using READ method")
	print(myxfile.read())
	print("**This will read only one line and will return string using READLINE method")
	myxfile.seek(0)
	print(myxfile.readline())
	print("**This will return list as READLINES method returns all rows in LIST object")
	myxfile.seek(0)
	print(myxfile.readlines())
	print(myxfile.mode)
with open('d:\\backup\\python\\pythonpractice\\AppendFCreation.txt', mode='a+') as myafile:
	myafile.write("Hello World by Append. This file did not exist before, append created me.")
	myafile.seek(0)
	print(myafile.read())
	myafile.seek(0)
	myafile.write("\nWell writing once again and now APPEND should overrite this file right ? But it won't, APPEND always append at the end.")
	myafile.seek(0)
	print(myafile.read())


	

