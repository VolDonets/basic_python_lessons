# tuple: ordered, immutable, allows duplicate elements
mytuple = ("Max", 28, "Boston")
print(mytuple)

# warning:
this_str = ("Max")
this_tuple = ("Max", )
print(type(this_str))
print(type(this_tuple))

# tuple from list
mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)

# get element from tuple
item = mytuple[0]
print(item)
item = mytuple[-1]
print(item)

# iterate over tuple
for x in mytuple:
    print(x)

# check is element in tuple
if "Max" in mytuple:
    print("yes")
else:
    print("no")

# some counting
mytuple = ('a', 'p', 'p', 'l', 'e')
print(len(mytuple))
print(mytuple.count('p'))
print(mytuple.count('o'))

# get index
print(mytuple.index('p'))

# convert to list
mylist = list(mytuple)
print(mylist)

# slicing in tuples
a = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
print(a)
print(b)
print(a[:5])
print(a[1:])
print(a[::2])
print(a[1:5:2])

# unpicking
mytuple = "Max", 28, "Boston"
name, age, city = mytuple
print(name, age, city)

mytuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = mytuple
print(i1, i2, i3)

# compare efficiency: tuple Vs list
# tuple is more effective in iterations
import sys

mylist = [0, 1, 2, "hello", True]
mytuple = (0, 1, 2, "hello", True)

print(sys.getsizeof(mylist), "bytes")
print(sys.getsizeof(mytuple), "bytes")

import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5, 6]", number=1_000_000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5, 6)", number=1_000_000))
