#variable=A container for a value (String,int,float,boolean).A variable behaves as if it was the value it contains
""""
first_name="Bhanu "
print(f"Hello{first_name}")
"""

#Typecasting=typecasting is the conversiom of one data type to another data type.
"""
name="Bhanu"
age=20
gpa=6.4
is_student=True
print(type(age))"""


#Input()=A function that prompts the user enter data returns the entered data as a string.
"""name=input("What is your name ?: ")"""


# => Shopping cart program
"""item=input("What item would you like to buy ?:")
price=float(input("What is the price of the item? :"))
Quantity=int(input("How many items would you like to buy ?:"))
Total=price*Quantity
print(f"The total is ${Total:.2f}")"""


#Madlibs games
"""adjective1=input("Enter an adjective: ")
adjective2=input("Enter another adjective: ")
verb1=input("Enter a verb: ")
verb2=input("Enter another verb: ")
noun1=input("Enter a noun: ")
noun2=input("Enter another noun: ")

print(f"Today I went to a {adjective1} zoo.")
print(f"I saw a {adjective2} {noun1} {verb1} on the grass.")
print(f"The {noun2} {verb2} in front of me.")
"""


#Math related functions
#Absolute value=Distance between a value and another value
"""X=3.14
Y=4
Z=5
result=abs(X)
result=round(X)
result=pow(5,2)
result=max(X,Y,Z)
result=min(X,Y,Z)
print(result)"""


# Some useful math functions
"""import math
X=9.1
print(math.sqrt(X))
print(math.ceil(X))
print(math.floor(X))
print(math.pi)
print(math.e)"""


#=> find the circumfernce of a circle
"""import math
radius=float(input("Enter the radius of the circle:"))
circumference=2*math.pi*radius
print(f"The circumference of the circle is {circumference:.2f}")"""


#=> find the hypotenuse of a triangle
"""import math
a=float(input("Enter the length of side a :"))
b=float(input("Enter the length of side b :"))
c=math.hypot(a,b)
print(f"The hypotenuse of the triangle is {c:.2f}")"""
#                  or
"""import math
a=float(input("Enter the length of side a :"))
b=float(input("Enter the length of side b :"))
c=math.sqrt(pow(a,2)+pow(b,2))
print(f"The hypotenuse of triangle is {c:.2f}")"""


#=> create a simple calculator
"""operator=input("Ener a operaror(+,-,/,*):")
num1=float(input("ENter the first number:"))
num2=float(input("Enter the second number:"))
if operator=="+":
    result=num1+num2
elif operator=="-":
    result=num1-num2
elif operator=="*":
    result=num1*num2
elif operator=="/":
    result=num1/num2
else:
    result=("invalid operator")"""


#=> python weight convertor
"""weight=float(input("Enter your weight:"))
unit=input("Enter the unit of your weight(K or L):").upper()
if unit=="K":
    weight=weight*2.20462
    print(f"Your weight is {weight} pounds")
elif unit=="L":
    weight=weight/2.20462
    print(f"Your weight is {weight} kilograms")
else:
    print(f"{unit} is not a valid unit")"""


#=> Conversion of tempurature from celsius to farenheit and vice versa
"""temp=float(input("Enter the temperature: "))
unit=input("Enter the unit of the temperature(C or F): ").upper()
if unit=="C":
    temp=temp*9/5+32
    print(f"The temperature in Fahrenheit is {temp}°F")
elif unit=="F":
    temp=(temp-32)*5/9
    print(f"The temperature in Celsius is {temp}°C")
else:
    print(f"{unit} is not a valid unit")"""


#Logical operators = evalute multiple conditions (or,not,and)
 
 #for or condition
"""temp=float(input("Enter the temperature:"))
is_raining=input("Is it raining?(yes/no):").lower()
if temp>30 or is_raining== "yes":
  print("it is hot or raining")
else:
  print("it is not hot and not raining")"""


#for and condition
"""temp=float(input("Enter the temperature:"))
is_sunny=input("IS it sunny?(yes/no):").lower()
if temp>20 and is_sunny=="yes":
    print("it is Warm and sunny")
    print("it is a good day  to go outside")
elif temp<0 and is_sunny=="no"and temp<0:
    print("it is cold and not sunny")
    print("it is not a good day to go outside")
elif temp>20 and is_sunny=="no"and temp>20:
    print("it is warm but not sunny")
    print("it is not a good day to go outside")
else:
    print("it is cold but sunny")
    print("it is not a good day to go outside")"""


# COnditional expressions = A one line shortcut for an if else satatement
      # "x if condition else y"
"""Num=int(input("Enter a number:"))
result="EVEN" if Num%2 == 0 else "ODD"
print(f"The number {Num} is {result}")"""


 # use some important functions
"""name=input("Enter your name:")
phone_number = input("Enter your phone number:")
result=name.find("0")
result=len(name)  to find the length of the string
result=name.capitalize() to capitalize the first letter of the string
result=name.upper() to capatilize all the letters of the string
result=name.lower() to convert all the letters of the string to lower case
result=name.isdigit() to check if the string contains only digits
result=phone_number.count("5") to count the number of times a character appears in a string
result=name.replace("bhanu","chaudhary") to replace a character in a string
print(result)"""


#=>valid user input exercise
# 1. username is no more than 12 character
# 2. username must not contain spaces
# 3. usernmae must not contain digits

"""user_name=input("Enter your username") 
if len(user_name)>12:
    print("your user_name can't be more than 12 characters")
elif not user_name .find(" ")==-1:
  print("your user_name can't contain spaces")
elif  not user_name .isalpha():
   print("your user_name can't contain numbers")
else:
   print(f"welcome{user_name}")"""


#Indexing= accessing elements of a sequence using[].(indexing operator)[start:end:step]
"""Credit_number="1234-5678-9012-3456"
print(Credit_number[:4])   to print first 4 digit
print(Credit_number[5:9])  to print 5 to 9 digit
print(Credit_number[4:])   for do not print first 4 digit
print(Credit_number[-1])   to print last digit
print(Credit_number[: :-1])to reverse the whole number
print(Credit_number[-4:])  to print last 4 digit"""


#Format Specifier = {value:flags} format a value based on what flags are inserted
#.(numbers)f = round to that may decimals place(fixed point)
#:(number) allocated that may spaces.
# 03 = allocate and Zero pad that may spaces.






# While loop = execute some code WHILE some condition remains true.
"""name=input("Enter your name :")
while name==" ":
    print("you did not enter your name:")
    name=input("Enter your name :")
    print(f"hello{name}")"""


# Python compound intrest calculator
#formula=>  A=P(pow(1+r/n,t))

"""Principle=34
time=-34
rate=12
while Principle <0:
    Principle=float(input("Enter the Principle amount:"))
if Principle<0:
    print("Principle can't less than zero:")
while time<0:
     time=int(input("Enter your time:"))
if time<0:
     print("time can't be less than zero:")
while rate<0:
     print=float(input("Enter your intrest rate:"))
if rate >0:
    print("Intrest rate can't be less than zero:")
total=Principle*pow((1+rate/100),time)
print(f"Balance after{time}years/s:${total:.2f}")"""


# for loop = execute a block of code a fixed number of times you can iterate over a range,string,sequence etc.
"""for x in range (1,9):   to print number 1 to 8
    print(x)"""
#          or 
#for continue and break the code.
"""for x in range(1,14):
    if x ==10:
        break
    else:
        print(x)"""


# create a digital watch
"""import time
my_time=int(input("Enter your time in second:"))
for x in range (my_time,0,-1):
 seconds=x%60
 minutes=int(x/60)%60
 hours=int(x%3600)%24
 print(f"{hours:02},{minutes:02},{seconds:02}")
 time.sleep(1)
 print("please wake up")"""


# Nested loop = It means putting one loop inside another loop.
"""for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()"""


#for write rows and column
"""rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

for i in range(rows):
    for j in range(columns):
        print("*", end=" ")
    print()"""


# Collectioin = sngle "variable" used to store multiple value .
# List[]=oredred and changable .Duplicate ok.
# Tuple()=oredred and unchangable .Duplicate ok. faster
# set{}= unordered and immutable .but add/remove element ok. no duplicate.

"""Fruits=["apple","banana","orange","chery"]
print(len(Fruits))
for fruit in Fruits:
    print(fruit)
print("apple"in Fruits)  to check fruits are avilable or not(boolean)
Fruits [0]="pineapple"   for change the value
for Fruit in Fruits:
Fruits.append("chery")   to add any element
Fruits.remove("apple")
Fruits.sort()      for sort the list means in order.
print(Fruits)
print(Fruits.index("apple")) to find index.
print(Fruits.count("apple")) to find the apple."""



#combine code of list,set,tuple
# LIST
"""Fruits = ["apple", "banana", "orange", "cherry"]

print("List:", Fruits)
print("First fruit:", Fruits[0])
print("Number of fruits:", len(Fruits))

# SET
Fruits_set = {"apple", "banana", "orange", "cherry"}

print("Set:", Fruits_set)
print("Number of fruits:", len(Fruits_set))

# TUPLE
Fruits_tuple = ("apple", "banana", "orange", "cherry")

print("Tuple:", Fruits_tuple)
print("First fruit:", Fruits_tuple[0])
print("Number of fruits:", len(Fruits_tuple))"""


#A 2D list (two-dimensional list) in Python is basically a list inside another list.Think of it like a table with rows and columns
#=> Create a 2D keypad
"""keypad = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["*", "0", "#"]
]

for row in keypad:
    for key in row:
        print(key, end=" ")
    print()"""


#Dictionary= A Collection of {Key:Value} pairs ordered and changable . No Duplicate
#=> concession Stand program

"""
menu = {
    "pizza": 3.00,
    "burger": 4.50,
    "chips": 10.30
}

cart = []
total = 0

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

while True:
    food = input("Select an item (q to quit): ").lower()

    if food == "q":
        break

    elif menu.get(food) is not None:
        cart.append(food)

    else:
        print("Item not available!")

for food in cart:
    total += menu.get(food)

print("Your cart:", end=" ")

for food in cart:
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")"""


#=> Code for random number
"""import random
number=random .randint(1,7)
print(number)"""


#=> code for play rock,paper,scissor
"""
import random

option = ("rock", "paper", "scissor")

player = None

while player not in option:
    player = input("Enter a choice (rock, paper, scissor): ").lower()

    Computer = random.choice(option)

    print(f"Player: {player}")
    print(f"Computer: {Computer}")

    if player == Computer:
        print("It's a tie")

    elif player == "rock" and Computer == "scissor":
        print("You win")

    elif player == "paper" and Computer == "rock":
        print("You win")

    elif player == "scissor" and Computer == "paper":
        print("You win")

    else:
        print("You lose")"""


# Dice rolling program.
"""
num = int(input("Enter dice number (1-6): "))

if num == 1:
    print("+-------+")
    print("|       |")
    print("|   *   |")
    print("|       |")
    print("+-------+")

elif num == 2:
    print("+-------+")
    print("| *     |")
    print("|       |")
    print("|     * |")
    print("+-------+")

elif num == 3:
    print("+-------+")
    print("| *     |")
    print("|   *   |")
    print("|     * |")
    print("+-------+")

elif num == 4:
    print("+-------+")
    print("| *   * |")
    print("|       |")
    print("| *   * |")
    print("+-------+")

elif num == 5:
    print("+-------+")
    print("| *   * |")
    print("|   *   |")
    print("| *   * |")
    print("+-------+")

elif num == 6:
    print("+-------+")
    print("| *   * |")
    print("| *   * |")
    print("| *   * |")
    print("+-------+")

else:
    print("Please enter a number from 1 to 6."""


    # FUnction= a block of reusable code place() after the function name to invoke it.
"""
def happy_birthday(name, age):
    print(f"Happy Birthday {name}")
    print(f"You are {age} years old")
    print("Many many returns of the day")
    print()

happy_birthday("Bhanu", 20)
happy_birthday("Prabhat", 21)
happy_birthday("Saksham", 21)"""


#Return =Statement used to end a function and sent a result back to the caller.
"""

def create_name(first, last):

    first = first.capitalize()
    last = last.capitalize()

    return first + " " + last


full_name = create_name("bhanu", "pratap")

print(full_name)"""


# Default Argument = A default argument is a value that pyton uses automatically if you don't provide an argument when calling a function.
"""
import time

def count(end, start=0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)

    print("Done!")

count(10, 2)  2 is used if you start from 2"""


# keyword argument= It means passing an argument to a function by using the parameter name.
"""
def student(name, age):
    print(name)
    print(age)

student(name="Bhanu", age=20)"""


# *args= It collects extra positional arguments into a tuple.
#**kwargs handles keyword arguments. It is a dictionary.
"""
def information(*args, **kwargs):
    print("Subjects:")

    for subject in args:
        print(subject)

    print("Student Information:")

    for key, value in kwargs.items():
        print(key, ":", value)


information(
    "Python",
    "SQL",
    "DSA",
    name="Bhanu",
    age=20
)"""


#List comprehension = is a short and easy way to create a new list from an existing list.
"""
numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]

print(squares)"""


#Match Case Statement= match-case in Python is used when you want to compare one value with multiple possible values.
"""
day = input("Enter your day:")

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case _:
        print("Invalid day")"""


#Module= It is a file containing python code-such as function ,variable and classes-that you reuse in another program.
# variable Scope = Where a variable is visible and accessible.
# scope resolution = (LEGB) Local->Enclosed->Global->Built-in.


#  -->  Create a banking program
def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")


def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount <= 0:
        print("That is not a valid amount")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn: "))

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount <= 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("\nBanking Program")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)

        elif choice == '2':
            balance += deposit()

        elif choice == '3':
            balance -= withdraw(balance)

        elif choice == '4':
            is_running = False

        else:
            print("That is not a valid choice")

    print("Thank you! Have a good day")


main()
















