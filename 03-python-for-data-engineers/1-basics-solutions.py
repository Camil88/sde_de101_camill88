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




