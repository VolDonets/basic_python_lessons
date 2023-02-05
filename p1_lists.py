# lists: ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = list()
print(mylist2)

mylist3 = [5, True, "apple", "apple"]
print(mylist3)

# get element by index
item = mylist[0]
print(item)

# iteration throw list
for x in mylist:
    print(x)

# check is element in the list
if "banana" in mylist:
    print("yes")
else:
    print("no")

# check length of the list
print(len(mylist))

# add new elements to the list
mylist.append("lemon")
print(mylist)

mylist.insert(1, "blueberry")
print(mylist)

# removing last list element
item = mylist.pop()
print(item)
print(mylist)

# clear list
print(mylist3)
mylist3.clear()
print(mylist3)

# sort list
print(mylist)
mylist.sort()
print(mylist)

# reverse list
mylist.reverse()
print(mylist)

# multiple elements
mylist = [0] * 5
print(mylist)

# adding lists
mylist2 = [1, 2, 3, 4, 5]
new_list = mylist + mylist2
print(new_list)

# slicing
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1:5]
print(a)
print(mylist[1:])
print(mylist[:5])
print(mylist[::2])
print(mylist[::-1])

# list coping
list_orig = ["banana", "cherry", "apple"]
list_cpy = list_orig[:]
# or
list_cpy = list_orig.copy()
# 04
list_cpy = list_orig[::1]

list_cpy.append("lemon")
print(list_orig)
print(list_cpy)

# list comprehension
a = [1, 2, 4, 5, 6, 7]
b = [i * i for i in a]
print(a)
print(b)
