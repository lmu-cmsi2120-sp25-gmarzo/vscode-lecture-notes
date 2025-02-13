from typing import Optional

class _Node: #O(1)
  def __init__(self, data: int) -> None:
    self.data: int = data
    self.next: Optional[_Node] = None

class Iterator: #O(1)
  def __init__(self, host: Optional[_Node]) -> None:
    self.__current = host
  
  def has_next(self) -> bool:
    return self.__current is not None and self.__current.next is not None
  
  def next(self) -> None:
    if self.__current is None:
      return
    self.__current = self.__current.next
  
  def get_current_int(self) -> int:
    if self.__current is not None:
      return self.__current.data
    else:
      raise ValueError("Iterator is currently pointing to nothing.")

class IntLinkedList:
  def __init__(self) -> None:
    self.__head: Optional[_Node] = None
    self.__size: int = 0
  
  def append(self, to_add: int) -> None:
    to_append: _Node = _Node(to_add) #O(1)
    self.__size += 1

    # List is currently empty
  
    if self.__head is None:
      self.__head = to_append
      return
    
    # List has elements
    current = self.__head
    while current.next is not None: #O(n)
      current = current.next
    current.next = to_append
  
  def prepend(self, to_add: int) -> None: #O(1)
    to_prepend: _Node = _Node(to_add)
    self.__size += 1

    prev_head = self.__head
    self.__head = to_prepend
    self.__head.next = prev_head
  
  def insert_at(self, to_add: int, index: int) -> None:
    raise NotImplementedError

  def remove_at(self, index: int) -> None:
    if index >= self.__size or index < 0:
      raise IndexError("Requested index out of range")

    current = self.__head
    prev: Optional[_Node] = None

    while current is not None and index > 0:
      prev = current
      current = current.next
      index -= 1
    
    if current is None:
      return
    
    if current is self.__head:
      self.__head = current.next
    if prev is not None:
      prev.next = current.next
    
    self.__size -= 1
  
  def __len__(self) -> int:
    return self.__size
  
  def __getitem__(self, key: int) -> int:
    if not self.__head:
      raise ValueError("List is empty")
    if key >= self.__size or key < 0:
      raise IndexError("Requested index out of range")
    
    current = self.__head
    while key > 0 and isinstance(current.next, _Node): #O(n)
      current = current.next
      key -= 1
    
    return current.data

  def get_iterator(self) -> Iterator:
    return Iterator(self.__head)
  
  def __iter__(self) -> "IntLinkedList":
    self.__current = self.__head
    return self
  
  def __next__(self) -> int:
    return_data = 0
    if self.__current is not None:
      return_data = self.__current.data
      self.__current = self.__current.next
    else:
      raise StopIteration
    return return_data
  

link: IntLinkedList = IntLinkedList()

# link.prepend(3)
# link.prepend(2)
# link.prepend(1)

# it: Iterator = link.get_iterator()
# print(it.get_current_int())
# it.next()
# print(it.get_current_int())
# it.next()
# print(it.get_current_int())

# print(it.has_next())
