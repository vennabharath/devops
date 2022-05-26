i = 0
while i < 5:
	print(i)
	i+=2

for i in range(1,5):
	print(i)
	
numbers = [1,2,3,4,5]
numbers[0]

append(6)
insert(0,6)
remove(6)
pop
clear
  removes all items
index(8) returns the index of the first occurence
sort() sorts the list
reveerse 
copy

range (5)
range (2,5)
co-ordin

customer = {
	"name" : "ab",
	"age" : 20,
	"profession" : carpenter
}

customer["name"]
customer.get("date_of_birth", 25/09/1990)
customer["name"]

def sampl_func(a,b):
		print(a+b)
		

result = sampl_func(2,3)
print(result)
		

		
try:
			age = int(input('Age: '))
			income = 200
			risk = income / age
			print(age)
except ValueError:
	print('Not a valid number')
except zerodivisionerror:
	print('Age cannot be 0')
	

when a function is a part of class 


class sampl:
	def _init (sampl,a,b):
		sampl.a = a
		sampl.b = b
	
	
	sampl1 = sampl()
	sampl = sampl
	
	classes define templates or blue prints for creating objects . 
		
A package is a directory with _init.py
It can contain one or more modules.

#importing the entire sales modules
from     import     

from  import

python standard library

python comes with a huge library of modules for 
performing common tasks such as 


import random

random.random
random.randint(1,6)

members = ['a', 'b', 'c']
leader = random.choice

pypi
dictionary = {key1 : value1, key2 : va}
dictionary[key]=value1
class_instance = class(args)


built 

/
//  
%

data types

list
dict
int
str
def fun_name(arg1, arg2, keyword1=val1, keyword2=val2):

	aaaaa
	aaaaaaa
	return valuename
	
def sampl(x,y,z=0)
	sum = x+y+z
	return sum
	
Accessing variable values

val = dictionary[key]
val = dictionary.get(key, default_value)
val = list[index]
val = string[start,end]
val = classname.class_var
val = class_instance.instance_variable
val = class_instance.function(args)

comparisions

val is not val2  
val in list
isinstance(class_instance, classname)

"""
"""
----------------------------------------------------------
if conditional
	;;;;;;
elif conditional
	;;;;;;;
else:
	;;;;;;;
	
for val in list
	;;;;;;;
	continue
	break
	
for val in range()
	;;;;;
	
for num in [2,3,4]
	if num == 2:
	continue
	
	if num == 4:
	break

while conditional:
		;;;;;;
		continue
		break
	
----------------------------------------------------------
class classname(superclass):
	class_var = static
	
	def _init_(self, value2,.....)
		self.instance_var1 = val
		self.instance_function()
		
	def instance_function(self, arg1, arg2, ......)
		;;;;;;
		return value
		
		
class class2(object)
	offset = 1
	def _init_(self, value)
		self.value = value
		
		import module
		from module import class,fucntion,variable
		
		

		
self:
			the self parameter is a reference to the current instance of the class, and is used 
			to access variables belonging to class. 
			

class 	Student:
	
	def _init_(reference, name, age):
		reference.name = name
		reference.age = age
	
	def sampl(abc):
		print("Hello the name of student:" + abc.name)
		
p1 = Student("aaaa", 25)
p1.sampl()

p1.age = 40

del p1.age

del p1

class Student
	pass
	
	
-----------------------------------------------------	
	

-----------------------------------------------------	
self variable:

self is implicit variable

self is pointing to current object

for every constructor and instance method self is always first argument

within the class self can be used to declare instance variables.

constructor :
constructor is a special method 
__init__()
automatically executed when object is created.

to declare and initialize instance variables

constructor can take atleast one argument which is self 

if you are not writing any constuctor python will provide default constructor



all classes have a function called
which is always executed when a class is initiated

use the init function to assign values to object properties
or other operations that are necessary  when the object is created.


-------------------------------------------------------
sets are used to store multiple items in a single variable

sets is one of 4 data types list tuples dictionary

set is a set of elements which are unordered unindexed

sets are written in curly brackets

fruits = { "apple", "banana", "mangos"}

print(fruits)

for x in fruits


print 


fruits.add("orange")

add sets

trees = {"papaya", "cherry"}

fruits.update(trees)


lists , tuples, dictionary can be updated into sets

set = {"a", "b", "c"}
set2 = {1, 2, 3}

set6 = set.union(set2)
----------------------------------------------------------

lambda function can take any number of arguments 


lambda arguments : expression


sampl = lambda a : a + 10
print(sampl(5))

sampl = lambda a, b, c : a + b + c
print(sampl(2, 3, 4))

def sampl(n)
	return lambda a: a * n

p2 = sampl(2)

print(p2(20))

---------------------------------------------------------

self variable is used to declare at the first method argument to access the instance variables and methods

this variable is used only with the instance methods





you can access the current object in a method
without the need for explicitly having it as a method
parameter. For example we can use this keyword to access the current object in 

but in python we have to explicitly declare the object instance as self variable.


class Dog:

	def _init_(self, breed):
		self.breed = breed

	def bark(self)
		print(f'{self.breed} is barking.')

d = Dog('village dog')
d.bark()

the self is automatically assigned to newly created 
instance of Dog object

we can skip self variable 

class Dog:

	def bark():
		print('Barking')

d = Dog()
d.bark()


Python self variable Example
Let’s say we have a Dog class defined as below.

class Dog:
 
    def __init__(self, breed, age):
        self.breed = breed
 
    def bark(self):
        print(f'{self.breed} is barking. age is {self.age}')
 
 
d = Dog('Labrador')
d.bark()
Output: Labrador is barking.


The __init__() function is defined with two variables but when we are creating
 the Dog instance, we have to provide only one argument. The “self” is automatically
  assigned to the newly created instance of Dog class.
The bark() method has only one argument – “self” – which gets bind to the Dog
 instance that calls this method. That’s why we are not passing any argument when
  calling the bark() method.
If we have to access any instance variable in the function, we can use the dot operator.
Can we skip “self” variable?
What if the instance method doesn’t need to access instance variables.
 Can we skip the self variable in this case?

Let’s find out with a simple example.

class Dog:
 
    def bark():
        print('Barking')
 
d = Dog()
print("Done")
If you will run the above code, there won’t be any error. But, we are not 
calling the bark() method. Let’s see what happens when we try to call
 the bark() method.

d = Dog()
d.bark()
Python Class Method Without Self Error
Python instance method without self Error
We are getting error as the bark() method accepts 0 argument but we provided 
1. It’s because when we are calling d.bark(), the “d” instance is automatically 
passed as the first argument to the bark() instance method.


But, if we access the bark() instance method through class reference then it 
will work fine. So, calling Dog.bark() will not cause any errors.

Similar variables for Class Method and Static Method?
The same behavior is present with the Class methods too. The only difference
 is that the convention is to use “cls” as the variable name for the Class reference.

class Dog:
 
    @classmethod
    def walk(cls):
        print('Dog is Walking')
 
 
Dog.walk()
However, it’s not required with a static method. Because, the static
 methods are self sufficient functions and they can’t access any of 
 the class variables or functions directly.

Let’s look at a complete example with self and cls variables and a
 static method without any arguments.

class Dog:
 
    def __init__(self, breed):
        self.breed = breed
 
    @classmethod
    def walk(cls):
        print('Dog is Walking')
 
    # instance method
    def bark(self):
        print(f'{self.breed} is barking.')
 
    @staticmethod
    def add(x, y):
        return x + y
 
 
Dog.walk()
d = Dog('Labrador')
d.bark()
print(Dog.add(10, 20))
Output:


Dog is Walking
Labrador is barking.
30
Quick Example to Break the Convention
This example is just to show you that it’s not mandatory to use the
 variable name as “self” and “cls”. In real programming, always stick to this convention.

class Dog:
 
    @classmethod
    def walk(myclass):
        print('Dog is Walking')
 
    # instance method
    def bark(myobject):
        print('Dog is Barking.')
 
Dog.walk()
d = Dog()
d.bark()
The “self” variable is bound to the current instance
The self variable gives us access to the current instance properties.
 We can confirm this with a simple example by creating two different instances of the Dog class.

class Dog:
 
    def __init__(self, b):
        self.breed = b
 
    def bark(self):
        print(f'{self.breed} is Barking.')
 
 
d1 = Dog('Labrador')
d2 = Dog('Husky')
 
d1.bark()
d2.bark()
Output:

Labrador is Barking.
Husky is Barking.




def methodA(self, arg1, arg2):
	;;;;;;;;;;;;;;;;

objectA = is a n instance of this class 

objectA.methodA(arg1, arg2)

the self variable refers to the object itself


class Vector:
	def _init_(self, x, y):
		self.x = x
		self.y = y

	def length(self):
		return math.sqrt(self.x ** 2 + self.y ** 2)



#----not required to use self name
-------------------------------------------
class Dog:

	@classmethod
	def walk(myclass):
		print('Dog is walking')

	# instance method
	def bark(myobject):
		print('Dog is barking')

Dog.walk()
d = Dog()
d.bark()

the self variable is to the current instance
---------------------------------------------
class Dog:

	def _init_(self, b)
		self.b = b

	def bark(self)
		print(f'{self.b} is barking')

	d1 = Dog('village dog')
	d2 = Dog('town dog')

	d1.bark()
	d2.bark()

---------------------------------------------------



---------------------------------------------------

Python Inheritance

class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def printname(self):
		print(self.firstname, self.lastname)

nameperson = Person("humpty", "dumpty")

nameperson.printname() 

creates a class that inherits the functionality from another class 
send the the parent class as a parameter when creating.

class Student(Person):
	pass


namestudent = Student("aa", "bb")

namestudent.printname()

we want to add the ___init__() function to the child class 

the __init__() function is called everytime automatically when the class is being 
used to create a object. 


as in other languages __init__ is'nt called the constructor method

__init__ method is called the initializer method.

THe initializer method initialies the new class instance . so the initializer method is
called the class instance is already constructed

The __init__ method alllows you to accept arguents to your class

the init method allows to assign initial values to carious attributes on class instances.


-----------------------------------------------------------------------------------		

creating , reading and writing files

open a text file:
-----------------

to open a file use the open function.
-------------------------------------

the file open function returns a file object that 
contains methods and attribures to perform 
various operations for opening
files in python.

file_object = open("file.txt", rw)

create a text file 

file_create = open("sampl.txt", "w+")

w  create file
+ indicates both read and write

for i in range(10):
	file_create.write("This is line \r\n" % (i+1))

writes data to file


close the file

file_create.close()
this will close the instance file_create


append text to file
---------------------

file_create = open("sampl.txt", "a+")
		
+ indicates file is created if it does not exist.


for i in range(2):
	file_create.write("Append line \r\n" % (i+1))


close the file

file_create.close()		
		

read file 
--------------

file_create=open("sampl.txt", "r")

find if the file is in open module

if file_create.mode == 'r':

use file_create.read() to the read  the file data and store 
it in a variable .

contents = file_create.read()
print(contents)


read a file line by line
-----------------------
def main()

	file_create=open("sampl.txt", "r")

	file_readline = file_create.readlines()
# or 

	for line in file_readline
		print(line)


if __name__=="__main__":
	main()
	
	
r - this is the default mode and opens the file for reading
w - writes to the file and if the file does not exist it creates the file
x - creates a new file 
a - opens file in append mode
    if the file does not exist it creates a file
t - this is the default mode and opens the file in text mode
b - 
+ - this will open the file for reading eand writing (updating)


import os.path
from os import path

use path.exists() 

path.exists("sampl.txt")

def main():
	print(+str(path.exists('sampl.txt')))
	print(+str(path.exists('dirname')))

file exists: True
directory exists: False

path.isfile()  whether a particular is a file or not

	


pathlib.Path.exists() returns  true if path or directory exists

-------------------------------------------------------------

return multiple values by functions

def Student
	name = "humpty"
	age = 20
	return name, age

name, age = Student()

print(name)
print(age)

---------------------------------------------------------------

scope of variables

global variables: can be used anywhere in the programming
local variables: can be used only in a certain location(loop, function)

----------------------------------------------------------------

dictionary

fish_dict = {
	'name' : seafish
	'age' : 2
	'river' : freshwater
}

fish_dict['age']
len(fish_dict)
list(fish_dict.keys())
list(fish_dict.values())
list(fish_dict.items())
fish_dict['food'] = 'sea weed'

fish_dict.get('age')  # returns none if age does not exist

del fish_dict['age'] deletes age key 
fish_dict.pop('age', None)
-----------------------------------------

functions 
args and kwargs

* expands a collection into positional arguments
** expands a dictionary into keyword arguments

args = (1,2)
kwargs = {'x': 3, 'y': 4}

def add(*val):
	for v in val
	 	sum+=v

add(1,2,3)

result 6


def add_f(*val)					# add_f(1,2,3,4)
def add_f(x,y, *args) 			# add_f(1,2,3,4)
def add_f(*args, z)				# add_f(1,2, z =3)
def add(**kwargs)
def(*args, *kwargs)

----------------------------------------------------

lists

append() - adds the element at the end of the list
clear()  	removes all the elements from the list
copy() 		returns a copy of the list
count() 	returns the number of elements
extend()	adds the elements to the end of the list

index()		returns the index of the specified element
insert()	inserts the element at a specified index
pop() 		removes the element at a  specified index
remove() 	removes the element with spefied value
reverse()	reverse the order of list
sort() 		sorts list
-----------------------------------------------

dictionary

os.path.join (Windows) and pathlib.Path.joinpath (L)

current working directory

use os on Windows
import os
os.getcwd()
os.chdir('C:\\Windows\\System32')




use pathlib on L

from pathlib import Path
from os import chdir

def add()
	global a, b
	value = 'local'
try:
	 This block is run
except Exception as e:
	raise    this block is run when exception occurs
else:
	pass
finally:
	pass this block is always run


---------------------------------------------


list comprehensions

It is a syntax to create new list using values in existing list:

a = [0,1,2]

b=[i+1 for i in a]
print(b)
Output
[1,2,3]


sampllist7 = [num*num for num in a]
print sampllist7

set comprehensions
creates a new set from existing set

a={0,1,2}
b={i**2 for i in a}

print(b)

{0,1,4}

Dict comprehensions

a = {'Hello' : 'greetings', 'first' : 1}

b = {val: k for k, val in a.items()}


dictionary comprehensions

sampldict7 = {num : num ** 2  for num in a}

set comprehensions

regex search match

Call re.search(regex, subject) to apply 
a regex pattern to a subject string. 
The function returns None if the matching
 attempt fails, and a Match object otherwise.
  Since None evaluates to False, you can 
  easily use re.search() in an if statement. 

----------------------------------------
multiple arguments 

* args - arguments passed as list
** args - arguments passed as dict 

def add(*val):
    sum = 0
    print(val)
    for v in val:
        sum+=v
    return sum

print("sum ", add(1,2,3,4,5))


def printval(**fish)
	
	for l, m in fish:
		print(l, m)

printval("name" : "seafish", "age" : "2") 
------------------------------------------------
  command line arguments
  --------------------

  accepts input from command prompt

  sys module
  forms a list
  sys.argv
  the arguments that are passed are considered as string

  sys.argv(LIST)

  elements of argv can be accessed using index (0,1,2,......)

  sys.argv[0]  - the first element of the list is the filename
  sys.argv[1] - from this all are arguments

import sys
print(sys.argv)
len(sys.argv) includ filename

for val in sys.argv:
	print("val is:", val)

for i in range(0, len(sys.argv))
	print("val is: ", sys.argv[i])

# SUM OF VALUES

sum = 0
for i in range(1, len(sys.argv))
	sum+=int(sys.argv[i])
print(sum)


  change the path to where the program is saved
  py filename.py arg1 arg2 arg3 ............


meta charachters and special sequences and sets
[] - specify the patternin square brackets
^ - returns a match if a line starts with a pattern
$ - returns a match if a line ends with a pattern
. - Any charachter except a newline
* - returns a match if there is a zero or more occurences
+ - one or more occurences
{} - specified number of occurences
/ - special sequences


[abc] - if a b and c exists in a text

a - yes (1 match)
ac -yes (2 match)
rapid - no

acc -yes

re.match()
searches only those starting with a 
re.search()
[abc] searches the whole string 

special sequences

\d - returns a match if a given text contains digits
\D - returns a match if a given string does not have digits
\w - returns a match if a line contains a alphabet charachters
\W - returns a match if a line does not contain alphabet charachters
\s - returns if a line contains spaces
\S - if a line does not contain spaces
\Z - if a line ends with specified charachters



import re
sampl_pattern = ^a...s$
sampl_text = 'alabs'

result = re.match(sampl_pattern, sampl_text)

# result = re.search(r"[abc]", sampl_text)

if result:
	print("Search successful")
else:
	print("search no succss")


sets

[abc] - returns a match if a string contains any of the specified charachters 


def get_sequence(p):
	for l in range(p):
		yield l

seq = get_sequence(7)
next(seq)
next(seq)
next(seq)
next(seq)
next(seq)
next(seq)


def sampl_generator():
	print('First item')
	yield 10

	print('Second item')
	yield 20

gen = sampl_generator()
next(gen)
next(gen)

def fibonacci(p)
	a, b = 0, 1

	while a < p
		yield a
		a = b
		b = a+b


re.findall(r'..', 'fght')

--------------------------------------------------------

os module
---------

In Python, 

			file names, 
			command line arguments, 
			and environment variables 

are represented
 using the string type.

  On some systems, decoding these 
 strings to and from bytes is necessary before passing 
 them to the operating system.


Python uses the filesystem encoding 
and error handler to perform this conversion 
(see sys.getfilesystemencoding())

The Python UTF-8 Mode ignores the
 locale encoding and forces the usage of
  the UTF-8 encoding:

Use UTF-8 as the filesystem encoding.

sys.getfilesystemencoding() returns 'UTF-8'.

locale.getpreferredencoding() returns 'UTF-8' (the do_setlocale argument has no effect).		

Process 
-------

os.chdir(path)

os.fchdir(fd)

os.getcwd()

os.fspath(path)

class os.Pathlike

An abstract base class for objects representing file system path
pathlib.PurePath

abstractmethod_fspath()
return the filesystem representation of the object


os.getenv(key, default=None)
return the value of environment variable key

os.get_exec_path()
return the list of directories that will be searched for a namestudent
executable when launching a process

os.getegid()
return the effective group id of process

os.getgid()
return the real group id of the current process

os.getgrouplist()
return the list of groups that the user belongs to.

os.getlogin()
return the name of the user logged in on the controlling terminal of the
process. For most purposes it is more useful to use getpass.getuser()

os.getpgid()
return the process group id of the process with process pid 

os.getpgrp()
return the id the current process group

os.strerror(code)

return the error message corresponding to the error code in code 

os.umask(mask)
set the current numeric umask and return the previous umask

os.uname()
return the information 
the return value is an object with five attributes

	sysname	-	 os name 
	nodename	-	name of machine on network
	release	-	os release
	version - 	os version
	machine	-	hw identifier

	the object is a tuple containing the attributes in that order

	Some systems truncate nodename to 8 characters or to 
	the leading component; a better way to get the hostname
	 is socket.gethostname()
		
os.unsetenv(key)
Unset (delete) the environment variable named key. Such 
changes to the environment affect subprocesses started
 with os.system(), popen() or fork() and execv().	


os.mkdir()

os.listdir()
list files and sub-directories 
--------------------------------------------------------------------

flatten list
------------
cascaded list or list of lists resembles  two dimensional array

nestedlist = [1,2,3,4], [5,6],[7,8,9]
flatlist = []

for sublist in nestedlist:
	for p in sublist:
		flatlist.append(p)

print(flatlist)


using list comprehensions
--------------------------
nestedlist = [1,2,3,4], [5,6],[7,8,9]
flatlist = [p for sublist in nestedlist for p in sublist]
print(flatlist)


merge dictionaries 
-----------------
key-value pair with key being non-repeateable and it
doesnt have a append operation. If a key repeatedly
appears in dictionary representation only the last 
appearence is taken

dict1 = {
	"a1" : 10,
	"a2" : 20,
	"a3" : 30,
	"a2" : 50,
	"a4" : 60
}
is considered as  

dict1 = {
	"a1" : 10,
	"a3" : 30,
	"a2" : 50,
	"a4" : 60
}

this charachterstic is used to merge the contents
of one dictionary in another.

If a key exists in another it will be updated or else
it will be added as a new pair

dict1 = {
	"a1" : 10,
	"a3" : 30,
	"a2" : 50,
	"a4" : 60
}

dict2 = {
	"p1" : 100,
	"p2" : 200,
	"a1" : 100
}

for l, m in dict2.items():
	dict1[l] = m 


print(dict1)

merge dictionaries using dict.update()
--------------------------------------



list =list[slice]
list.append(item) 		# list += item
list.extend(collection)	# list += collection

list.sort() - sorts in asc order
list.reverse()	-	reverses the list in place
list 	= sorted(collection)	- returns a sorted list 
list 	= reverse(list) 

sum =	sum(collection)
itemwise_sum	=	[sum(pair) in zip(list_a, list_b)]
sorted_by_second	=	sorted(collection, key=lambda el:el[1])
product_of_digits	= functools.reduce(lambda out, el:out * el, collection)
list_of_chars	=	 list(string)

list.insert(index, item) inserts the item at the appropriate index
digit = list.pop(integer)  # removes and returns item at index 
integer = list.count(digit)  # returns the number of occurences 
-------------------------------------------------------------------
