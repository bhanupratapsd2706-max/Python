# object = A "bundle" of related attributes (variable) and methods (function)
#         Ex. phone, cup, book
#         you need a "class" to create many objects

# Class = (blueprint) used to design the structure and layout of an object.
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Bhanu", 20)

print(s1.name)
print(s1.age)"""


# Variable = Shared among all instances of a class.
#            Define outside the constrtutor
#            Allow you to share data among all object created from the class.
"""
class Student:

    class_year = 2025
    num_student = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1


student1 = Student("SpongeBob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

print(f"My graduating class of {Student.class_year} has {Student.num_student} students")

print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)"""


# Inheritance = inheritance is an object-oriented programming (OOP) feature where one class can reuse and extend the attributes and methods of another class.
"""
class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Woof!")


dog = Dog()

dog.speak()  # inherited from Animal
dog.bark()   # defined in Dog"""


# Multiple Inheritance = inheritance from more than one parent class. 
#           Mother+father=son

# Multilevel Inheritance = A class inherits from another class, and a third class inherits from that child class.
 #EX=>  grandfather->father->son
"""
class Animal:
    def eat(self):
        print("This animal is eating")


class Prey(Animal):
    def flee(self):
        print("This animal is fleeing")


class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.eat()
rabbit.flee()

hawk.eat()
hawk.hunt()

fish.eat()
fish.flee()
fish.hunt()"""


# Super() = super() is used in inheritance to call a method or __init__() from the parent class.
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Animal:", self.name)


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        self.show()
        print("Age:", self.age)


dog = Dog("Tommy", 3)
dog.display()"""


# Polymorphism = The same method/function name can perform different actions depending on the object
# poly=Many  ,  morphe=Form
"""
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        super().__init__()  # Calls the parent class constructor
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):

    def __init__(self, side):
        super().__init__()  # Calls the parent class constructor
        self.side = side

    def area(self):
        return self.side ** 2


circle = Circle(5)
square = Square(4)

print("Circle area:", circle.area())
print("Square area:", square.area()) """


# ducktyping = Duck typing is a concept in Python where the type of an object is less important than what the object can do.
"""
class Dog:
    def speak(self):
        print("Dog says Woof")


class Cat:
    def speak(self):
        print("Cat says Meow")


def animal_sound(animal):
    animal.speak()


dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)"""


# Class method = A class method is a method that is bound to the class and uses cls as its first parameter. It is created using the @classmethod decorator.
"""
class Student:

    school = "ABC College"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


print(Student.school)

Student.change_school("XYZ College")

print(Student.school)"""


# Magic method = Magic methods are special methods in Python that are automatically called when certain operations are performed on an object.
"""
class Student:

    # Class variable
    school = "ABC College"
    total_students = 0

    # 1. __init__() → called when object is created
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

        Student.total_students += 1

    # 2. __str__() → called when print(object) is used
    def __str__(self):
        return f"Student(Name={self.name}, Age={self.age}, Marks={self.marks})"

    # 3. __len__() → called when len(object) is used
    def __len__(self):
        return len(self.name)

    # 4. __eq__() → called when == is used
    def __eq__(self, other):
        return self.marks == other.marks

    # 5. __gt__() → called when > is used
    def __gt__(self, other):
        return self.marks > other.marks

    # 6. __lt__() → called when < is used
    def __lt__(self, other):
        return self.marks < other.marks

    # 7. __add__() → called when + is used
    def __add__(self, other):
        return self.marks + other.marks

    # 8. __sub__() → called when - is used
    def __sub__(self, other):
        return self.marks - other.marks

    # 9. __mul__() → called when * is used
    def __mul__(self, other):
        return self.marks * other.marks

    # 10. __contains__() → called with "in"
    def __contains__(self, item):
        return item.lower() in self.name.lower()

    # 11. __call__() → allows object to behave like a function
    def __call__(self):
        print(f"{self.name} is called like a function!")

    # Class method
    @classmethod
    def show_total_students(cls):
        print("Total students:", cls.total_students)

    # Normal method
    def show_details(self):
        print("Name  :", self.name)
        print("Age   :", self.age)
        print("Marks :", self.marks)


# ------------------------------------------------
# Creating objects
# ------------------------------------------------

student1 = Student("Bhanu", 20, 85)
student2 = Student("Prabhat", 21, 75)
student3 = Student("Rahul", 20, 85)


# ------------------------------------------------
# __str__()
# ------------------------------------------------

print(student1)

print()


# ------------------------------------------------
# Normal method
# ------------------------------------------------

student1.show_details()

print()


# ------------------------------------------------
# __len__()
# ------------------------------------------------

print("Length of name:", len(student1))

print()


# ------------------------------------------------
# __eq__()
# ------------------------------------------------

print("Student 1 == Student 2:", student1 == student2)
print("Student 1 == Student 3:", student1 == student3)

print()


# ------------------------------------------------
# __gt__()
# ------------------------------------------------

print("Student 1 > Student 2:", student1 > student2)

print()


# ------------------------------------------------
# __lt__()
# ------------------------------------------------

print("Student 1 < Student 2:", student1 < student2)

print()


# ------------------------------------------------
# __add__()
# ------------------------------------------------

print("Total marks:", student1 + student2)

print()


# ------------------------------------------------
# __sub__()
# ------------------------------------------------

print("Difference in marks:", student1 - student2)

print()


# ------------------------------------------------
# __mul__()
# ------------------------------------------------

print("Multiplication of marks:", student1 * student2)

print()


# ------------------------------------------------
# __contains__()
# ------------------------------------------------

print("'Bhanu' in student1:", "Bhanu" in student1)
print("'xyz' in student1:", "xyz" in student1)

print()


# ------------------------------------------------
# __call__()
# ------------------------------------------------

student1()

print()


# ------------------------------------------------
# Class Method
# ------------------------------------------------

Student.show_total_students()"""


# Decorator = A decorator is a function that takes another function as an argument and extends or modifies its behavior without changing its source code.
"""
def decorator_function(func):

    def wrapper():
        print("Before the function")

        func()

        print("After the function")

    return wrapper


@decorator_function
def hello():
    print("Hello Bhanu!")


hello()"""


# Exception = An event that interrupts the flow of a program
#              (Zerodivision error , typeError , ValueError)
#            1.try, 2.except, 3.finally
"""
try:
    number = int(input("Enter a number:"))

    print(1 / number)

except ZeroDivisionError:
    print("You can't divide by zero!")

except ValueError:
    print("Enter only a number please!")

except Exception:
    print("Something went wrong!")

finally:
    print("Do some cleanup here")"""


# => Python alarm 
"""
import time
from datetime import datetime

alarm_time = input("Enter alarm time (HH:MM:SS): ")

print(f"Alarm set for {alarm_time}")

while True:
    current_time = datetime.now().strftime("%H:%M:%S")

    if current_time == alarm_time:
        print("⏰ ALARM! WAKE UP!")
        break

    time.sleep(1)"""


# Multithreading = Multithreading is a feature in Python that allows a program to perform multiple tasks at the same time by using multiple threads.
"""
import threading
import time


def walk_dog():
    time.sleep(8)
    print("You finish walking the dog")


def take_out_trash():
    time.sleep(2)
    print("You take out the trash")


def get_mail():
    time.sleep(4)
    print("You get the mail")


# Create threads
thread1 = threading.Thread(target=walk_dog)
thread2 = threading.Thread(target=take_out_trash)
thread3 = threading.Thread(target=get_mail)

# Start threads
thread1.start()
thread2.start()
thread3.start()

# Wait for all threads to finish
thread1.join()
thread2.join()
thread3.join()

print("All tasks are complete!")"""


# How to connect to an API
"""
import requests

# API URL
url = "https://pokeapi.co/api/v2/pokemon/pikachu"

# Send GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:

    # Convert JSON response into Python dictionary
    data = response.json()

    # Display information
    print("Pokemon Information")
    print("--------------------")
    print("Name:", data["name"])
    print("Height:", data["height"])
    print("Weight:", data["weight"])
    print("Base Experience:", data["base_experience"])

else:
    print("Failed to retrieve data")
    print("Status Code:", response.status_code)"""


#  PyQt5  Introduction
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("My First PyQt5 App")
window.setGeometry(500, 200, 400, 300)

label = QLabel("Hello World!", window)
label.move(150, 100)

window.show()

sys.exit(app.exec_())"""


# pyqt5 Qlqbel
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Color Example")
window.setGeometry(500, 200, 400, 300)

label = QLabel("Hello Bhanu!", window)
label.move(120, 100)

# Add color and font size
label.setStyleSheet(
    color: red;
    font-size: 30px;
    font-weight: bold;
)

window.show()

sys.exit(app.exec_())"""


# Pyqt5 image
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap

app = QApplication(sys.argv)

# Create window
window = QWidget()
window.setWindowTitle("Image Example")
window.setGeometry(500, 200, 500, 400)

# Create label
label = QLabel(window)

# Load image
pixmap = QPixmap("myphoto.jpg")

# Set image
label.setPixmap(pixmap)

# Resize image
label.setScaledContents(True)
label.resize(300, 200)

# Position image
label.move(100, 80)

# Show window
window.show()

sys.exit(app.exec_())"""


# Pyqt5 Layouts
#Main PyQt5 layouts
#QVBoxLayout → widgets arranged vertically
#QHBoxLayout → widgets arranged horizontally
#QGridLayout → widgets arranged in rows and columns
"""
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit, QVBoxLayout
)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PyQt5 Layout")
window.resize(400, 300)

# Create widgets
label = QLabel("Enter your name:")

textbox = QLineEdit()
textbox.setPlaceholderText("Your name")

button = QPushButton("Submit")

# Create vertical layout
layout = QVBoxLayout()

# Add widgets to layout
layout.addWidget(label)
layout.addWidget(textbox)
layout.addWidget(button)

# Set layout on window
window.setLayout(layout)

window.show()

sys.exit(app.exec_())"""


# PuQt5 Checkboxes = A QCheckBox is a PyQt5 widget that lets the user select or unselect an option
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QVBoxLayout


def checkbox_changed():
    selected = []

    if python_checkbox.isChecked():
        selected.append("Python")

    if java_checkbox.isChecked():
        selected.append("Java")

    if cpp_checkbox.isChecked():
        selected.append("C++")

    if selected:
        result.setText("Selected: " + ", ".join(selected))
    else:
        result.setText("Nothing selected")


# Create application
app = QApplication(sys.argv)

# Create window
window = QWidget()
window.setWindowTitle("QCheckBox Example")
window.resize(400, 300)

# Create label
title = QLabel("Select your programming languages:")

# Create checkboxes
python_checkbox = QCheckBox("Python")
java_checkbox = QCheckBox("Java")
cpp_checkbox = QCheckBox("C++")

# Create result label
result = QLabel("Nothing selected")

# Connect checkboxes
python_checkbox.stateChanged.connect(checkbox_changed)
java_checkbox.stateChanged.connect(checkbox_changed)
cpp_checkbox.stateChanged.connect(checkbox_changed)

# Create layout
layout = QVBoxLayout()

layout.addWidget(title)
layout.addWidget(python_checkbox)
layout.addWidget(java_checkbox)
layout.addWidget(cpp_checkbox)
layout.addWidget(result)

# Set layout
window.setLayout(layout)

# Show window
window.show()

# Run application
sys.exit(app.exec_())"""


# setStyleSheet() in PyQt5, it is used to change the appearance/design of widgets such as buttons, labels, checkboxes, and windows.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Checkbox Style")
window.resize(400, 300)

python = QCheckBox("Python")
java = QCheckBox("Java")
cpp = QCheckBox("C++")

# Style checkboxes
python.setStyleSheet("""
    QCheckBox {
        color: blue;
        font-size: 20px;
        font-weight: bold;
    }
    QCheckBox::indicator {
        width: 20px;
        height: 20px;
    }
""")

java.setStyleSheet("""
    QCheckBox {
        color: green;
        font-size: 20px;
    }
""")

cpp.setStyleSheet("""
    QCheckBox {
        color: red;
        font-size: 20px;
    }
""")

# Layout
layout = QVBoxLayout()

layout.addWidget(python)
layout.addWidget(java)
layout.addWidget(cpp)

window.setLayout(layout)

window.show()

sys.exit(app.exec_())