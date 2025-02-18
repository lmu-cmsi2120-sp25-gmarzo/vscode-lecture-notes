from pyarray import PyArray

class IntArrayList:
  def __init__(self) -> None: #O(1)
    self.__START_SIZE: int = 8 #O(1)

    self.__items: PyArray = PyArray(int, self.__START_SIZE) #O(1)
    self.__size: int = 0 #O(1)
  
  def get_at(self, index: int) -> int: #O(1)
    if index < 0 or index >= self.__size: #O(1)
      raise ValueError("Requested index out of range")
    return self.__items[index] #O(1)
  
  def append(self, to_add: int) -> None: #O(n)
    self.__check_and_grow() #O(n)
    self.__items[self.__size] = to_add #O(1)
    self.__size += 1 #O(1)
  
  def insert_at(self, to_add: int, index: int) -> None: #O(n)
    if index < 0 or index >= self.__size:
      raise ValueError("Requested index out of range")
    self.__check_and_grow() #O(n)
    self.__shift_right(index) #O(n)
    self.__items[index] = to_add
    self.__size += 1
  
  def remove_at(self, index: int) -> None:
    if index < 0 or index >= self.__size:
      raise ValueError("Requested index out of range")
    self.__shift_left(index)
    self.__size -= 1
  
  def prepend(self, to_add: int) -> None:
    self.insert_at(to_add, 0)
  
  def __check_and_grow(self) -> None: #O(n)
    """
    Expand the size of this list whenever
    it is at capacity
    """
    if self.__size < len(self.__items): 
      return
    
    new_items: PyArray = PyArray(int, len(self.__items) * 2) 

    for i in range(len(self.__items)): #O(n)
      new_items[i] = self.__items[i]
    
    self.__items = new_items #O(1)
  
  def __shift_left(self, index: int) -> None:
    for i in range(index, self.__size-1):
      self.__items[i] = self.__items[i+1]
  
  def __shift_right(self, index: int) -> None:
    for i in reversed(range(index, self.__size + 1)):
      self.__items[i] = self.__items[i-1]
    
  def __str__(self) -> str:
    return str(self.__items)

  """
  for each element i in array, start with i = 1:

      for each element k = i down to k = 1 where arr[k] < arr[k-1]:
        swap arr[k] and arr[k-1] 
  """

  def swap_ints_at(self, index1: int, index2: int) -> None:
    temp: int = self.__items[index1]
    self.__items[index1] = self.__items[index2]
    self.__items[index2] = temp
  
  def insertion_sort(self) -> None:
    # Starting from the second item, sort the array
    for i in range(1, self.__size):
      # Check if item to the left is larger, and if so swap them 
      while i > 0 and self.__items[i] < self.__items[i-1]:
        self.swap_ints_at(i, i-1)
        i -= 1


# test: IntArrayList = IntArrayList()
# test2: IntArrayList = IntArrayList()
# test.append(2)
# test.append(4)
# test.append(8)
# print(test.get_at(1))
# test.remove_at(1)
# print(test.get_at(1))
# for i in range(5):
#   test.append(i)
# print("Done")
# test2.append(1)
# for i in range(100000): #O(n^2)
#   test2.prepend(i) #O(n)
#   # test2.append(i)
# print("Done")

# test.append(15)
# test.append(7)
# test.append(8)
# test.append(9)
# test.append(12)
# test.append(3)
# test.append(1)
# test.append(-9)
# test.append(6)
# test.append(-234789561245123678)

# print(f"Pre-sort: {test}")
# test.insertion_sort()
# print(f"Post-sort: {test}")

# test.prepend(25)
# test.prepend(9)