from IntLinkedList import *

class IntStack:
  def __init__(self) -> None:
    self.__list = IntLinkedList()
  
  def push(self, to_push: int) -> None:
    self.__list.prepend(to_push)
   
  def pop(self) -> None:
    self.__list.remove_at(0)
   
  def peek(self) -> int:
    return self.__list.__getitem__(0)

  
stacky: IntStack = IntStack()

stacky.push(1)
stacky.push(2)
stacky.push(3)

stacky.pop()


print(stacky.peek())