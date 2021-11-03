# one argument lambda
add10 = lambda x: x + 10
print(add10(5))

# multiple arguments lambda
mult = lambda x, y: x * y
print(mult(10, 4))

# lambda arguments: expression
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])

print(points2D)
print(points2D_sorted)

# lambda function in maps
a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x * 2, a)

print(a)
print(list(b))

# list comprehension
c = [x * 2 for x in a]
print(c)

# filter function
d = filter(lambda x: x % 2 == 0, a)
print(list(d))

# reduce function
from functools import reduce

product_a = reduce(lambda x, y: x * y, a)
print(product_a)
