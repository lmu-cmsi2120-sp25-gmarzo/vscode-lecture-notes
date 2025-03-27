from BinaryMaxHeap import *

class PriorityQueue:

  __queue: BinaryMaxHeap

  def __init__(self) -> None:
    self.__queue = BinaryMaxHeap()
  
  def add(self, to_add: int) -> None:
    self.__queue.add(to_add)
  
  def peek(self) -> int:
    return self.__queue.heap[0]
  
  def poll(self) -> int:
    return self.__queue.poll()

  def __len__(self) -> int:
    return len(self.__queue.heap)