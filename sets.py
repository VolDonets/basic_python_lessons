# Sets: unordered, mutable, no duplicates
myset = {1, 2, 3, 4, 4, 2}
print(myset)

myset = set("Hello World")
print(myset)

# creating an empty set:
myset = set()

# add elements
myset.add(1)
myset.add(2)
myset.add(3)
myset.add(4)
myset.add(5)
print(myset)

# remove element
myset.remove(2)
print(myset)
myset.discard(7)
print(myset)
myset.discard(1)
print(myset)

print(myset.pop())
print(myset)

myset.clear()
print(myset)

# iterate over set
myset = {1, 2, 3, 4, 5}
for x in myset:
    print(x)

if 1 in myset:
    print("yes")

# union and intersection
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

union = odds.union(evens)
print("union:", union)
intersection = odds.intersection(evens)
print("intersection:", intersection)
intersection = odds.intersection(primes)
print("intersection:", intersection)
intersection = evens.intersection(primes)
print("intersection:", intersection)

# calculate the difference of two sets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff)
diff = setB.difference(setA)
print(diff)

diff = setB.symmetric_difference(setA)
print(diff)
diff = setA.symmetric_difference(setB)
print(diff)

setA_copy = setA.copy()
setA_copy.update(setB)
print(setA_copy)

setA_copy = setA.copy()
setA_copy.intersection_update(setB)
print(setA_copy)

setA_copy = setA.copy()
setA_copy.difference_update(setB)
print(setA_copy)

setA_copy = setA.copy()
setA_copy.symmetric_difference_update(setB)
print(setA_copy)

# superset subset
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}

print(setA.issubset(setB))
print(setB.issubset(setA))

print(setA.issuperset(setB))
print(setB.issuperset(setA))

print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))
