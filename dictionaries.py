# dictionary: key-value pairs, unordered, mutable
mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)
mydict2 = dict(name="Mary", age=28, city="New York", email="max@xyz.com", penis_lenght_sm=3.1)
print(mydict2)

# add a new value
mydict["email"] = "max@xyz.com"
print(mydict)

# how to delete value
del mydict2["name"]
print(mydict2)
mydict2.pop("age")
print(mydict2)
mydict2.popitem()
print(mydict2)

# check key in dictionary
if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["name"])
except:
    print("Error")

# loop throw dict
for key in mydict:
    print(key)
for key in mydict.keys():
    print(key)
for value in mydict.values():
    print(value)
for key, value in mydict.items():
    print(key, value)

# copy dictionaries
mydict_copy = mydict.copy()
# or
mydict_copy = dict(mydict)
mydict_copy["penis length sm"] = 3.1
print(mydict)
print(mydict_copy)

# merge dictionaries
my_dict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
my_dict_2 = {"name": "Mary", "age": 27, "city": "Boston"}

my_dict.update(my_dict_2)
print(my_dict)
