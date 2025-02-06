from pyarray import *
from lecture3 import *

my_int_arr: PyArray = PyArray(int, [1, 2, 3, 4, 5])

my_str_arr: PyArray = PyArray(str, 4)
my_str_arr[1] = "Hello World!"

my_saalmon_arr: PyArray = PyArray(Saalmon, [Burnymon("Pickahu"), Dampymon("Bucky")])


# for num in my_int_arr:
#   print(num)


def i4in12(arr: PyArray):
  arr[4] = 12

# print(my_int_arr)
# i4in12(my_int_arr)
# print(my_int_arr)

test_arr: PyArray = PyArray(int, 8)
test_arr[0] = 4
test_arr[1] = 10

print(test_arr)