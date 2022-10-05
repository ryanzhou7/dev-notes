# Practical Python

- [site](https://practical.learnpython.dev/)
- [course](https://frontendmasters.com/courses/practical-python/)

<br/>

## [Setup](https://practical.learnpython.dev/001_prerequisites/20_requirements/10_install_python_mac_linux/)

- Vscode - installed pylance, pylint, python extensions all by microsoft
- `python3 -m venv env`
- `python3 -m pip install --upgrade pip`
- command + shift + P: python: select interpreter
  - All new iTerm tabs should have activated env
- Or, activate the env, then `code .` Vscode should auto-activate
- `>python run python file in terminal`

<br/>

## Why Python

- [standard lib](https://docs.python.org/3/library/)
- [packages](https://pypi.org/)
- [pep 8 style guide](https://pep8.org/)

<br/>

## Data types

- python is dynamic in that variable types don't need to be declared, ex. `x = 42`
- [Naming practices](https://www.youtube.com/watch?v=YklKUuDpX5c)
- all lowercase, start with letter/underscore, snake case (words separated by underscores)
- integers and other simple data types are just objects under the hood

```python
type(42) # <class 'int'>
dir("str") # show all methods on string
help("".isupper) # docs, q to quit
```

### Numbers: int, float, complex

```python
int('4')
type(2/1) # <class 'float'>
type(2//1) # <class 'int'>
True == 1 # True
False == 0 # False
```

### Strings

```python
"OK"
'Also ok'
"""
Greetings and salutations, dear Nina.
I'm superfluous with my words,
"""
# white space will be part of this string

print("October is month", 10) # October is month 10, note the space separator
repr() # display unambiguous output to developers, for debugging purposes.
print("str" + " concat")
greeting = f"Hello, {name}" # f string
strip() # remove lead / trail whitespace
rstrip() # trailing
lstrip() # leading

"Hello, world!".replace("world!", "Dog")
```

<br/>

## Data structures

### LISTS

```python
[]
my_list.index(i) # throws ValueError if not found hence use "in" operator first
i in my_list # search
len(my_list), append(i) insert(index, i), pop()
my_list.sort(), my_list.sort(reverse=True) # in place sort
sorted(my_list) # creates new list
my_list.reverse()
my_list.extend(list_to_add_to_my_list)
my_list.count("how many elements like this")
my_list.remove(first_item_instance_to_remove)
```

- [cheat sheet](https://practical.learnpython.dev/02_data_types/30_lists/#adding-removing-changing-and-finding-items-in-list-s-cheat-sheet)

### SETS, TUPLES, AND DICTIONARIES

- **tuple**: immutable

```python
() # creation
(1, ) # note need the trailing ,
name, age = ("Joe", 12) # unpacking
```

-[tuple cheat sheet](https://practical.learnpython.dev/03_sets_tuples_dicts/10_tuples/#tuple-cheat-sheet)

- **Set**: mutable datatype that allows you to store immutable types (cannot store list, sets, dicts) in an unsorted way
- [cheat sheet](https://practical.learnpython.dev/03_sets_tuples_dicts/20_sets/#set-cheat-sheet)

```python
set()
{} # makes empty dict
{1, 2, 3}
my_set.add(e)
my_set.discard(e)
my_set.update(other_set)
s.union(t) # creates new set with items from both set s and t
s.intersection(t) # creates new set with only items both in set s and t
```

- **dictionary**: keys can only be immutable types

```python
d[key] # throws KeyError if missing
d.get(key) # silent fail
d.items()
d.keys()
d.values()
d = {1: 2, 3: 4}
d.get(4, "default")
d.update(other_dict_to_update_this_with)

```

## FUNCTIONS, LOOPS, AND LOGIC

- functions without return implicitly returns `None`
- positional arguments are required and must be given in the order declared
- all required arguments first, followed by optional keyword arguments
- keyword arguments don't need order and are optional
- Never use mutable types as default argument as these are evaluated only once, thus the same type will be reused each time the function is called
- The effect of changes to variables defined outside of a function by a function only occur during that function call
- all containers with no items are `False`, for int only `0` is True

```python
bool("") # False, any other True
a = [1, 2]
b = [1, 2]
a == b # True
a is b # False as is means "the same object in memory", only use this for bool / None
or, and, not # operators
if a > 10:
  pass
elif a == 11:
  pass
else:
  pass
for color in colors:
for num in range(5): # 0...5
for num in range(1, 5): # 1...5
for num in range(2, 5, 2): # 2, 4
for index, item in enumerate(colors):
  print(f"Item: {item} is at index: {index}.")
for key in my_dict: # only gets keys
```

- [Transforming Code into Beautiful, Idiomatic Python](https://www.youtube.com/watch?time_continue=1855&v=OSGv2VnC0go)

<br/>

## Practical Applications

### List comprehensions

```python
my_list = [len(name) for name in names] # len of each name in names
[(name, len(name)) for name in names] # name, len tuple for each name
[len(name) for name in names if len(name) % 2 == 0]
my_data.split(",") # string to list
":".join(my_data) # : between everything my_data
sum, min, max # functions

# Dict comprehensions
{num:num * num for num in range(10)} # num -> square

# Set comprehensions
{num for num in [1, 2, 1, 0, 3]}

# Generator expression - emit elements on demand, exhausted once end reached
gen = (x ** 2 for x in range(10) if x % 2 == 0)
for e in gen:

my_string[:] # copy entire
my_string[:2] # start to next 2
my_string[3:] # 3 from the end
"Hello, world!"[-6:] # world! - on left side: will around to other side of your list
"Hello, world!"[-10:-4] # lo, wo - on right side: is length minus number
"abc"[-1] # c
my_list[::2] # skip every other index
my_list[::-1] # reverse list

for name, score in zip(names, scores): # iterate until shortest reached
```

### Working with files

- ‘r’ open for reading (default)
- ‘w’ open for writing, truncating the file first
- ‘x’ open for exclusive creation, failing if the file already exists
- ‘a’ open for writing, appending to the end of the file if it exists
- ‘b’ binary mode
- ’t’ text mode (default)
- ’+’ open a disk file for updating (reading and writing)

```python
my_file = open("my_file.txt", "w")

# Context manager, wrapper around code that depends on some resource
with open("my_file.text") as my_file:
    contents = my_file.read() # no need to remember to call "close"
```

<br/>

## Object oriented python

- all objects in python are instances of an class (ex. 42, str)

```python
class Car:
    runs = True
    number_of_wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    @classmethod # shared between all instances
    def get_number_of_wheels(cls):
        return cls.number_of_wheels

    def start(self):
        if self.runs:
            print("Car is started. Vroom vroom!")
        else:
            print("Car is broken :(")

my_car = Car("Toyota", "Pruis")
print(f"Cars have {Car.get_number_of_wheels()} wheels.")

# Of course, we can override this in our instance:
my_car.number_of_wheels = 6

# And when we access our new instance variable:
print(f"My car has {my_car.number_of_wheels} wheels.") # 6 wheels

# But, when we call our class method on our instance:
print(f"My car has {my_car.get_number_of_wheels()} wheels.") # 4 wheels

my_car.__str__() # user readable
my_car.__repr__() # for debugging


isinstance(42, int) # True
issubclass(bool, int) # True
issubclass(bool, object) # All things are object

# vehicle.py
class Vehicle:
    number_of_wheels = 4 # class variable

    def __init__(self, make, model, fuel="gas"):
        self.make = make # instance vars
        self.model = model
        self.fuel = fuel

class Car(Vehicle):

    def __init__(self, make, model, fuel="gas"):
        super().__init__(make, model, fuel)

class Truck(Vehicle):
    number_of_wheels = 6 # overriding

    def __init__(self, make, model, fuel="diesel"):
        super().__init__(make, model, fuel)

class Motorcycle(Vehicle):
    number_of_wheels = 2
```

- python has multiple inheritance
- **Mixin**: classes that tend to be used to quickly and easily add additional properties and methods into a class, enourages composable architecture

```python
try:
    int("a")
except ValueError as error: # as keyword to name the exception
    print(f"Something went wrong. Message: {error}")
except TypeError:
    pass
finally:
    print("Always run")

class MyException(Exception):
  pass
raise MyException()
```

- [Type of exceptions](https://practical.learnpython.dev/06_object_oriented_python/50_exceptions/)
- best practice: catch more specific exceptions first, don't catch Exception / BaseException

<br/>

## Libraries and Modules

```python

# name_lib.py
def lower_case_name(name):
    return name.lower()

# dunder prevents could calls on "import name_lib" from other files
if __name__ == "__main__":
    name = "Nina"
    length = name_length(name)

    print(f"The length is {length} and the uppercase version is: {upper_case}")
```

`pip freeze > requirements.txt`
`pip install -r requirements.txt`
`python -m pip install requests`

```python
from random import randint # import specific into program name space,
randint(0, 100)
random.randint(0, 100) #otherwise

from math import * # don't do
import my_math_functions as mmf # good
```

- Any directory with file named `__init__.py` is a python module but no longer needed for python 3 modules
- Don't use `assert` for production checks, only for tests

```python
# $ python test_divisible.py --verbose
# test_multiply.py

import unittest

def multiply(x, y):
    return x * x

class TestMultiply(unittest.TestCase):

    # must begin with "test_" prefix or won't be run
    def test_multiply(self):
        test_x = 5
        test_y = 10
        self.assertEqual(multiply(test_x, test_y), 50, "Should be 50")

if __name__ == "__main__":
    unittest.main()
```

- [test case assertions](https://practical.learnpython.dev/07_programs_libraries_modules/55_tests/)

<br/>

## [Web frameworks](https://practical.learnpython.dev/08_web_frameworks/)

<br/>

## [Next steps](https://practical.learnpython.dev/09_wrapping_up/00_next_steps/)
