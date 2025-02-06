# Greatest common denominator

def gcd(x: int, y: int) -> int:
  if y > x:
    temp = x
    x = y
    y = temp
  
  if x == y or x % y == 0:
    return y
  
  current_greatest: int = 1
  for i in range(1, y):
    if x % i == 0 and y % i == 0:
      current_greatest = i
  
  return current_greatest


# print(gcd(2, 4)) # => 2
# print(gcd(21, 49)) # => 7
# print(gcd(13, 53)) # => 1

# print(gcd(1578692, 1578691)) # => ?

# Euclid's Algorithm
# x = q * y + r
# gcd(y, r)

"""
gcd(48, 20)

48 = 2 * 20 + 8

gcd(20, 8)

20 = 2 * 8 + 4

gcd(8, 4)

8 = 2 * 4 + 0

return 4

"""

def better_gcd(x: int, y: int) -> int:
  if y > x:
    temp = x
    x = y
    y = temp
  
  if x == y or x % y == 0:
    return y
  
  return better_gcd(y, x % y)

# print(better_gcd(157864492, 157864491)) # => ?


def nearest_ints(num: int) -> int: # T(n) = c_1 + c_2
  print(num - 1) #c_1
  print(num + 1) #c_2

# nearest_ints(1)
# nearest_ints(10000000000000000000000000000)

def count_up(n: int) -> int: # T(n) = n * (c_1 + c_2)
  for i in range(n): # c_1 * n
    print(i) # c_2 * n

# count_up(1)
# count_up(10000000000000000000000000000)

def heat_death_of_the_universe(n: int) -> int: # T(n) = n^2 * (c_2 + c_3) + n * c_1
  for i in range(n): # c_1 * n
    for j in range(n): # c_2 * n^2
      print(i, j) # c_3 * n^2

# heat_death_of_the_universe(10000)


def g(arr: list, c: int) -> None: # T(n) = n(c_1 + c_2)
  for i in range(len(arr)): # c_1 * n
    print(c + i) # c_2 * n

def f(arr: list) -> None: # T(n) = c_1 * n + n^2(c_1 + c_2)
  for i in range(len(arr)): #c_1 * n
    g(arr, i) #g(T(n)) * n


f([x for x in range(20)])