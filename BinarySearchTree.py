from typing import Optional

class BSTNode:
  data: int
  left: Optional["BSTNode"]
  right: Optional["BSTNode"]

  def __init__(self, data: int):
    self.data = data
    self.left = None
    self.right = None

class BST:
  root: Optional["BSTNode"]
  size: int

  def __init__(self):
    self.root = None
    self.size = 0
  
  def add(self, to_add: int) -> bool:
    """
    Adds in a number to the BST by finding its proper location
    and then creating a new node containing the int at that spot.

    Returns True if the addition was successful, and False if the tree already
    contains the requested value.
    """
    # Case: Tree is empty
    if self.root is None:
      self.root = BSTNode(to_add)
      self.size += 1
      return True 
    
    current: BSTNode = self.root
    while current is not None:
      # Case: to_add is already in the tree
      if current.data == to_add:
        return False
      
      # Case: to_add is less than current
      if to_add < current.data:
        # Case: OK to insert left
        if current.left is None:
          current.left = BSTNode(to_add)
          self.size += 1
          return True
        # Case: left child exists
        current = current.left
      
      #Case: to_add is greater than current
      else:
        # Case: OK to insert right
        if current.right is None:
          current.right = BSTNode(to_add)
          self.size += 1
          return True
        # Case: right child exists
        current = current.right

  def contains(self, query: int) -> bool:
    """
    Determines whether or not the given int query exists
    """
    current: Optional[BSTNode] = self.root
    while current is not None:
      # Case: found the query
      if current.data == query:
        return True
      
      # Case: not the query, keep looking
      if query < current.data:
        current = current.left
      elif query > current.data:
        current = current.right
    return False
  
  def get_sorted_list(self) -> list[int]:
    sorted_list = []
    self.__sorted_helper(sorted_list, self.root)
    return sorted_list

  def __sorted_helper(self, lst: list, node: BSTNode) -> None:
    if node is None:
      return
    self.__sorted_helper(lst, node.left)
    lst.append(node.data)
    self.__sorted_helper(lst, node.right)

    
tree = BST()
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(10)
tree.add(11)
tree.add(12)
# print(tree.contains(10)) # True
# print(tree.contains(3)) # True
# print(tree.contains(14)) # False
# print(tree.contains(1)) # False

print(tree.get_sorted_list())

