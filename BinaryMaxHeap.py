class BinaryMaxHeap:

  heap: list

  def __init__(self):
    self.heap = []

  def add(self, to_add: int) -> None:
    # Add it to the bottom-most, right-most leaf spot
    self.heap.append(to_add)

    # Reheapify: bubble-up this value until it is <= its parent
    self.__bubble_up(len(self.heap)-1)
  
  def __get_parent_index(self, child_index: int) -> int:
    return (child_index - 1) // 2
  
  def __bubble_up(self, index: int) -> None:

    if index == 0:
      return
    
    parent_index: int = self.__get_parent_index(index)
    parent_value: int = self.heap[parent_index]
    current_value: int = self.heap[index]

    if parent_value < current_value:
      self.heap[index] = parent_value
      self.heap[parent_index] = current_value

      self.__bubble_up(parent_index)


  def poll(self) -> int:
    popped_value = self.heap[0]

    self.heap[0] = self.heap.pop(-1)
    self.__trickle_down(0)
    return popped_value
  
  def __get_child_index(self, parent_index: int, right_child: bool = False) -> int:
    result = (parent_index * 2) + 1

    if right_child:
      result += 1
    return result
  
  def __trickle_down(self, parent_index: int) -> None:

    left_child_index: int = self.__get_child_index(parent_index)
    right_child_index: int = self.__get_child_index(parent_index, True)

    parent_value: int = self.heap[parent_index]
    lc_value: int = self.heap[left_child_index] if left_child_index < len(self.heap) else -1
    rc_value: int = self.heap[right_child_index] if right_child_index < len(self.heap) else -1

    if parent_value < lc_value and lc_value > rc_value:
      self.heap[parent_index] = lc_value
      self.heap[left_child_index] = parent_value
      self.__trickle_down(left_child_index)
    elif parent_value < rc_value:
      self.heap[parent_index] = rc_value
      self.heap[right_child_index] = parent_value
      self.__trickle_down(right_child_index)

  def __str__(self) -> str:
    return self.heap.__str__()
  
heapy = BinaryMaxHeap()
heapy.add(25)
heapy.add(10)
heapy.add(20)
heapy.add(8)

print(heapy)

heapy.add(99)

print(heapy)

heapy.poll()

print(heapy)