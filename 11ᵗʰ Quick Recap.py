'''
IDLE Integrated devalopment learning environment

tokens-Punctuators Identifiers Constant Keyword Operators

escape sequence- \n (next line) \a (bell sound) () \t (tab space)

priority for operators
__________________________________________________
|            ()             |         bracket     |
|            **             |        exponents    |
|         * / // %          |      multi and divi |    the ones is same level, should be done
| < > <= >= != == is is not |      comparisions   |       left to right in the sum
|             not           |       boolean not   |
|             and           |       boolean and   |
|             or            |       boolean or    |
|_________________________________________________|

AND both to be true
OR either of one be true
NOT opposites

membership - in, not in
identity - is, is not

             MUTABLE                         IMMUTABLE
                |                                |
      ____________________            _________________________
      |                  |           |       |       |        |    
    list            dictionary      int    string  tuple   boolean

while - initialisation, condition, iteration
range - (start,stop,step)

break - it breaks the loop (comes out of the loop)
continue - it skips the current condition in a loop
pass - does nothing
______________________________________________________________________________

string function
slicing    - [start,stop,step]
length     - len()                    returns the length of the string
capitalize - x.capitalise()           caps the first letter of the string
title      - x.title()                caps every first letter of words
upper,lower- x.upper()                caps the entire string
count      - x.count('')              counts the given character
find       - x.find('',start)         prints the index value of the chr
split      - x.split('')              splits the string wherever the chr appears
partition  - x.partition('')          splits 3 parts, 1)before 2)the chr 3)after
replace    - x.replace(old,new,count) replaces the old string with new given times
______________________________________________________________________________
list function
eval       - eval('')                 takes one input which is a str, evaluates
length     - len()                    returns the length of the list
index      - x.index()                1 argument, elements, returns its index value
min & max  - min() max()              returns maximum/minimum value from the list
append     - x.append()               1 argument, adds as last element in list
extend     - x.extend()               1 argument, a variable (for multi values)
insert     - x.insert(index,value)    2 arguments to add element, pushes the old to next index
pop        - x.pop()                  default-last element, removes given index
remove     - x.remove()               1 argument, removes given Value
clear      - x.clear()                removes all elements, list still exist
delete     - del(x)                   deletes the entire list from memory
count      - x.count('')              counts the given character
sort       - x.sort()                 no argument, increase or decrease-> x.sort(reverse=True)
reverse    - x.reverse()              no argument, reverses the list
______________________________________________________________________________
tuple function
tuple      - tuple()                  change data type to tuple
length     - len()                    returns the length of the tuple
min & max  - min() max()              returns maximum/minimum value from the tuple
index      - x.index()                1 argument, elements, returns its index value
count      - x.count('')              counts the given character
delete     - del(x)                   deletes the entire tuple from memory
______________________________________________________________________________
dictionary function
assigning  - x[<key>]=<value>         used to add elements (key value pair) in a dictionary
pop        - x.pop()                  1 argument, <key> removes and returns given key & its value
clear      - x.clear()                removes all elements, dictionary still exist
delete     - del x[<key>]             deletes the given key value, does not return
get        - x.get()                  1 argument, <key> gets the value of that key
items      - x.items()                returns key value in tuple, and in a list as whole [(a,1),(b,1)]
keys       - x.keys()                 returns all keys of the dictionary in a list
values     - x.values()               returns all values of the dictionary in a list
update     - x.update(<other dict>)   updates value if same keys, if not adds as a new element
set defalt - dict.setdefault(,)       same as update, doesnt update if same keys, but adds
fromkeys   - dict.fromkeys(,)         2 arguments, list/tuple of keys and list/tuple of values *variable
______________________________________________________________________________

Matrix
basically nested list

|_______columns j
|
|
|
rows i

1
4 5      if (i>=j):
7 8 9

1 2 3
  5 6    if (i<=j):
    9

    3
  5 6    if (i+j>=m-1):
7 8 7

1 2 3
4 5      if (i+j<=m-1):
7
______________________________________________________________________________

Boolean algebra
or  +    diagram arrow pointing right
and .    diagram dome pointing right
not      diagram a small triangle pointing right attatched to a small circle
______________________________________________________________________________

'''
