# Variable: A storage location identified by its name, containing some value.
# Question: Assign a value of 10 to variable a and 20 to variable b
# Question: Store the result of a + b in a variable c and print it. What is the result of a + b?
a = 10
b = 20
c = a + b
c
30

s = '  Some string '
# Question: How do you remove the empty spaces in front of and behind the string s?
s = '  Some string '
trimmed = s.strip()
print(trimmed)
Some string
print(len(trimmed))
11

# Data Structures are ways of representing data, each has its own pros and cons and places that they are the right fit.
## List: A collection of elements that can be accessed by knowing the location (aka index) of the element
l = [1, 2, 3, 4]
l[0]
1
l[3]
4

## Dictionary: A collection of key-value pairs, where each key is mapped to a value using a hash function. Provides fast data retrieval based on keys.
d = {'a': 1, 'b': 2}
# Question: How do you access the values associated with keys 'a' and 'b'?
## NOTE: The dictionary cannot have duplicate keys
d['a']
1
d['b']
2
d.get('a')
1
d.get('b')
2

## Set: A collection of unique elements that do not allow duplicates
my_set = set()
my_set.add(10)
my_set.add(10)
my_set.add(10)
# Question: What will be the output of my_set?
# ANSWER: the output will be one element - 10
print(my_set)
{10}

## Tuple: A collection of immutable (non-changeable) elements, tuples retain their order once created.
my_tuple = (1, 'hello', 3.14)
# Question: What is the value of my_tuple?
# ANSWER: the value is 3 elements
# Question: How do you access the elements in index 0 and 1 of my_tuple?
my_tuple[0]
1
my_tuple[1]
'hello'

# Counting occurrences of an element
count_tuple = (1, 2, 3, 1, 1, 2)
# Question: How many times does the number 1 appear in count_tuple?
count = 0
for i in count_tuple:
  if i == 1:
    count += 1

count
3

# OR
count_tuple.count(1)
3
# ANSWER: 1 appears 3 times

# Finding the index of an element
# Question: What is the index of the first occurrence of the number 2 in count_tuple?
count_tuple.index(2)
1
# ANSWER: the index number is 1

# We can loop through our data structures as shown below
# Question: How do you loop through a list and print its elements?
l = [1, 2, 3, 4]
for i in l:
  print(i)

# Dictionary loop
# Question: How do you loop through a dictionary and print its keys and values?
d = {'a': 1, 'b': 2}
for i in d:
  print(i, d[i])
a 1
b 2

for i, k in d.items():
  print(i, k)
a 1
b 2

# Comprehension is a shorthand way of writing a loop
# Question: Multiply every element in list l with 2 and print the result
doubled = [num * 2 for num in l]
doubled
[2, 4, 6, 8]

# Functions: A block of code that can be re-used as needed. This allows for us to have logic defined in one place, making it easy to maintain and use.
## For example, let's create a simple function that takes a list as an input and returns another list whose values are greater than 3
def gt_three(input_list):
    return [elt for elt in input_list if elt > 3]
## NOTE: we use list comprehension with filtering in the above function

list_1 = [1, 2, 3, 4, 5, 6]
# Question: How do you use the gt_three function to filter elements greater than 3 from list_1?
gt_three(list_1)
[4, 5, 6]

list_2 = [1, 2, 3, 1, 1, 1]
# Question: What will be the output of gt_three(list_2)?
# ANSWER: empty list
gt_three(list_2)
[]

# Classes and Objects
# Think of a class as a blueprint and objects as things created based on that blueprint
# You can define classes in Python as shown below
class DataExtractor:
    def __init__(self, some_value):
        self.some_value = some_value

    def get_connection(self):
        # Some logic
        # some_value is accessible using self.some_value
        pass

    def close_connection(self):
        # Some logic
        # some_value is accessible using self.some_value
        pass

# Question: How do you create a DataExtractor object and print its some_value attribute?
new_obj = DataExtractor(2)
print(new_obj.some_value)
2

from datetime import datetime  # You can import library or your code from another file with the import statement
# Question: How do you print the current date in the format 'YYYY MM DD'? Hint: Google strftime
now = datetime.now()
formatted = now.strftime('%Y %m %d')
print(formatted)

# Exception handling: When an error occurs, we need our code to gracefully handle it without just stopping. 
# Here is how we can handle errors when the program is running
try:
    # Code that might raise an exception
    pass
except Exception as e: 
    # Code that runs if the exception occurs
    pass
else:
    # Code that runs if no exception occurs
    pass
finally:
    # Code that always runs, regardless of exceptions
    pass

# For example, let's consider exception handling on accessing an element that is not present in a list l
l = [1, 2, 3, 4, 5]
# Question: How do you handle an IndexError when accessing an invalid index in a list?
try:
  print(l[5])
except IndexError:
  print('Index is out of scope')
else:
  print(f'Index value is {l[5]}')

Index is out of scope


