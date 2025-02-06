from pyarray import PyArray

class IntArrayList:
  def __init__(self) -> None:
    self.__START_SIZE: int = 8

    self.__items: PyArray = PyArray(int, self.__START_SIZE)
    self.__size: int = 0
  
  def get_at(self, index: int) -> int:
    if index < 0 or index >= self.__size:
      raise ValueError("Requested index out of range")
    return self.__items[index]
  
  def append(self, to_add: int) -> None:
    self.__check_and_grow()
    self.__items[self.__size] = to_add
    self.__size += 1 
  
  def insert_at(self, to_add: int, index: int) -> None:
    if index < 0 or index >= self.__size:
      raise ValueError("Requested index out of range")
    self.__check_and_grow()
    self.__shift_right(index)
    self.__items[index] = to_add
    self.__size += 1
  
  def remove_at(self, index: int) -> None:
    if index < 0 or index >= self.__size:
      raise ValueError("Requested index out of range")
    self.__shift_left(index)
    self.__size -= 1
  
  def prepend(self, to_add: int) -> None:
    self.insert_at(to_add, 0)
  
  def __check_and_grow(self) -> None:
    """
    Expand the size of this list whenever
    it is at capacity
    """
    if self.__size < len(self.__items):
      return
    
    new_items: PyArray = PyArray(int, len(self.__items) * 2)

    for i in range(len(self.__items)):
      new_items[i] = self.__items[i]
    
    self.__items = new_items
  
  def __shift_left(self, index: int) -> None:
    for i in range(index, self.__size-1):
      self.__items[i] = self.__items[i+1]
  
  def __shift_right(self, index: int) -> None:
    for i in reversed(range(index, self.__size + 1)):
      self.__items[i] = self.__items[i-1]



test: IntArrayList = IntArrayList()
test2: IntArrayList = IntArrayList()
# test.append(2)
# test.append(4)
# test.append(8)
# print(test.get_at(1))
# test.remove_at(1)
# print(test.get_at(1))
# for i in range(5):
#   test.append(i)
# print("Done")
test2.append(1)
for i in range(100):
  test2.prepend(i)
  # test2.append(i)
print("Done")

# test.append(15)
# test.append(7)
# test.append(8)
# test.append(9)
# test.append(12)
# test.append(3)
# test.append(1)

# test.prepend(25)
# test.prepend(9)