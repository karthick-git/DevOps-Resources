Python basics

#Installation
install latest version of pyton
install vs code
install python and code runner extension from vs code marketplace
Go to File > Preference > Settings then
type: run code and scroll down until you see code-runner: Run in terminal, There will be multiple options called "code-runner". In that you can find the option mentioned below.
just check "Whether to run code in integrated terminal" and restart vscode.
To run Python code: use shortcut Ctrl+Alt+N.
To stop the running code: use shortcut Ctrl+Alt+M.
The file can also be run in the terminal by typing 'python <filename>.py'

#sysout
print ("Hello world")
either single or double quotes can be used. use prints effectively for debugging. Use double quotes around a string when the string itself contains single quotes inside of it.We can also use \ before single quote in the middle of the string to escape the character.
print('it\'s an example for using double quotes')
print("it's an example for using double quotes")

#scanner
name = input ('Enter your name : ')
print(name)
Note: input function will always return a string by default. So don't forget to do type conversion before doing math operations with user's input

#enter new line
print('blank line \nin the middle of the string')
\n is the new line character ,it moves the cursor to starting of next line. \t is the horizontal tab character,it moves the cursor a tab width.

#storing string in a variable
first_name='karthick'
print(first_name)

#string concatenation
first_name='karthick'
last_name='srinivasan'
print(first_name+' '+last_name)

#string manipulation
print(first_name.upper())
print(first_name.lower())
print(first_name.capitalize())
print(first_name.count('k'))

#line break
Break a big line with \ at the end of the line. It's optional though.
print(first_name.lower()+' '+first_name.upper()+' '+\
    first_name.capitalize())

#string formatting
first_name='Karthick'
last_name='srinivasan'
output='hello {1},{0} '.format(first_name,last_name)
print(output)
The .format function gives the option to change the order in which the output variables are displayed without changing the input order.
Another way of writing the format fucntion
output=f'hello {first_name},{last_name}'
print(output)

#working with numbers
Just like strings, numbers are also stored in variables
first_num=2
second_num=5
print(first_num+second_num)
print(first_num-second_num)
print(first_num*second_num)
print(first_num/second_num)
print(first_num**second_num)
Remember the ** is used for exponent, not ^. Using ^ will add the numbers

#Type conversion
Python will concatenate 2 strings if we use + and will add 2 numbers if we use +, but it won't concatenate a string and a number if we use +, like in java. So we have to explicitly convert the type from one to another, usually numbers to string.

first_name='karthick\'s age is '
age=25
print(first_name+age) will result in TypeError: can only concatenate str (not "int") to str
So use the code: print(first_name+str(age))

When asking input from user
num1=input('Enter the 1st number: ')
num2=input('Enter the 2nd number: ')
print(num1+num)
Output: Enter the 1st number: 2
Enter the 2nd number: 3
23

How to correct this:
num1=int(input('Enter the 1st number: '))
num2=int(input('Enter the 2nd number: '))
print(num1+num2)
Output:Enter the 1st number: 2
Enter the 2nd number: 3
5

float() can also be used in place of int(), but the numbers will be appended with .0 at the end.

#Dates
use datetime library's datetime function by importing
from datetime import datetime
currentDate=datetime.now()
print('currentDate is '+str(currentDate))

timedelta is used to define a period of time
from datetime import datetime,timedelta
currentDate=datetime.now()
print('currentDate is '+str(currentDate))
oneday=timedelta(days=1)
print(currentDate-oneday)

To get indiviaual numbers
from datetime import datetime
currentDate=datetime.now()
print(currentDate.day)
print(currentDate.month)
print(currentDate.year)
print(currentDate.hour)
print(currentDate.minute)
print(currentDate.second)

To convert the received date into a datetime object
birthday=input('Enter your birthday (dd/mm/yyyy)')
birthday_date=datetime.strptime(birthday, '%d/%m/%Y')
print(birthday +': '+str(birthday_date))

In python we use : instead of {}
We use except instead of catch. 
An indent is 4 spaces, not a tab. VS code will autocorrect that for us.
String comparisons are case sensitive. 
else if is elif in python.
In python functions must be declared before the line in which we use it
In python we can assign values when we are passing parameters also.
E.g: def get_initial(name,force_uppercase=True)
In this case, we don't need to pass True as the second parameter while calling the function, since we have already declared it as the default value. We just need to pass if we are going to pass False.
E.g: get_initial(first_name) or get_initial(first_name,False)
In python, booleans start with uppercase
In python, the order in which pass the parameter should be same as the order in which we have declared it in the function.This is incase we pass unnamed notations. If we are passing named notations, we can pass the arguments in whatever order we need.
E.g: If def get_initial(name,force_uppercase) is the function, then we have to call it like get_initial(first_name,True). 
We can also do it in the below way
get_initial(force_uppercase=True,name=first_name). 

#Exception handling:
x=5
y=2
try:
    print(x/y)
except ZeroDivisionError as e:
    print('not allowed to divide by 0')
else:
    print('something else went wrong')
finally:
    print('cleanup code')

    When the values are not zeros, try, else and finally will be executed.
    When any of the values are 0. try, except and finally will be executed.

#Conditions
or statements: if x=a or x=b:
in statements: if x in (a,b,c):
in is like or for a list of possible values. mostly used if the number of values are more than 2.
and statements: if x>2 and x<5
If you need to remember the results of a condition check later in your code, use boolean flags.

Visit https://github.com/microsoft/c9-python-getting-started/tree/master/python-for-beginners for more code examples.

#Lists
For Lists you don't need to import any library but a list can store any datatype.
names=['ash','tsubame','karthick']
marks=[]
marks.append(90)
marks.append(100)
print(len(marks))
marks.insert(0,95)
names.sort()
marks.sort()
presenters = names[0:2]
print(names,marks)
Note: don't use dort inside a print statement, it will give you 'none' as the result. sort will work with both strings and ints. 
Indexes start from brackets and are on the commas and end on brackets--> easy way to remember. Range is always upto and not including.

#Arrays
For using arrays you should import array library
Arrays are numerical data types, it must be all same data type in an array.
from array import array
scores=array('d')
scores.append(90)
scores.append(100)
print(scores)
print(scores[1])

#Dictionaries
For Dictionaries you don't need to import any library and storage orde is not guaranteed.
for storing key value pairs
person = {'first':'karthick'}
person['last']='ash'
print(person)
print(person['first'])

#List of Dictionaries
karthick = {'first':'karthick'}
karthick['last']='ash'

tsubame = {'first':'tsubame'}
tsubame['last']='hatori'

people=[]
people.append(karthick)
people.append(tsubame)
people.append({'first':'shinzo','last':'hatori'})
print(people)

Always good to declare empty collections and append. Always give names to ditionaries and lists so that it will be easier to manipulate later.

#Loops:
Looping through a collection - condition can be specified only with a while
for name in ['Ash','Karthick']:
    print(name)

Looping through 'n' number of times
for index in range(0,5):
    print(index)

Looping with a condition
name=['karthick','ash']
index=0
while index<len(name):
    print(name[index])
    index+=1

remember to use while here and index++ can't be used, instead use index=index+1 or index+=1.
While is mostly used to traverse through all lines of a file etc. it's always good to use for. if while is always true, it will end in a stackovdrflow error.

#Modules and Packages:
Module is a python file with fucntions, classes and other components. It helps us breakdown our code into reusable functions.
We can create a class with a function E.g - helpers.py
This can be imported into another class in 3 ways.
importing module as namespace:
E.g- import helpers - in this case i need to call that function like 
helpers.display("")
import all into current namespace
E.g - from helpers import * - in this case we can call it like display("")
import specific items into current namespace
E.g - from helpers import display - in this case we cam call it like display("") again
We can use any import and there will be no performance impact
To stop cluttering intellisense, 3rd option is preferred.

Packages are published collections of modules. We can find them in python package index.
To install them we just need to use pip - package installer for python
E.g - pip install <package_name>
or we can also install from a text file as a bulk
E.g - pip install -r requirements.txt
inside requirements.txt we can just have the package name E.g- colorama

By default packages are installed globally and maintenance becomes challenging.Virtual envs can be used to manage package collections.Just a folder behind the scenes with all our packages.

To create vitual env
pip install virtualenv
python -m venv <folder_name>
To activate virtual env
Open cmd--> <folder_name>\Scripts\Activate.ps1
make sure (venv) is present in the start of the line in terminal and ('venv':venv) is present in the bottom of vscode where python version is displayed. If not click on python version and select venv manually

Request library provided by python is very useful for sending API requests.
    