from IntLinkedList import *

class IntQueue:
  def __init__(self) -> None:
    self.__list = IntLinkedList()
  
  def push(self, to_push: int) -> None:
    self.__list.append(to_push)
  
  def poll(self) -> None:
    self.__list.remove_at(0)
  
  def peek(self) -> int:
    return self.__list.__getitem__(0)

queueie: IntQueue = IntQueue()

queueie.push(1)
queueie.push(2)
queueie.push(3)

print(queueie.peek())
queueie.poll()


print(queueie.peek())