from typing import Optional

class BinaryTreeNode:
  data: int
  left: Optional["BinaryTreeNode"]
  right: Optional["BinaryTreeNode"]

  def __init__(self, data: int):
    self.data = data
    self.left = None
    self.right = None
  
  def invert_tree(self):
    if not self.left and not self.right:
      return
    if self.left:
      self.left.invert_tree()
    if self.right:
      self.right.invert_tree()
    
    temp = self.left
    self.left = self.right
    self.right = temp
  
  def sum_even_nodes(self) -> int:
    total = 0

    if not self.left and not self.right:
      if self.data % 2 == 0:
        return self.data
      else:
        return 0
    
    if self.left:
      total += self.left.sum_even_nodes()
    if self.right:
      total += self.right.sum_even_nodes()
    
    return total
  
root = BinaryTreeNode(0)
root.left = BinaryTreeNode(1)
root.right = BinaryTreeNode(6)

root.left.right = BinaryTreeNode(24)

# l_child = root.left
# l_child.left = BinaryTreeNode(2)
# lcr = l_child.right = BinaryTreeNode(9)

# lcr.left = BinaryTreeNode(5)
# lcr.left.right = BinaryTreeNode(4)

# r_child = root.right
# r_child.right = BinaryTreeNode(3)

# rl_child = r_child.right
# rl_child.left = BinaryTreeNode(8)
# rl_child.right = BinaryTreeNode(7)

def pre_order_print(node: Optional[BinaryTreeNode]) -> None:
  if node is None:
    return
  print(node.data)
  pre_order_print(node.left)
  pre_order_print(node.right)

def post_order_print(node: Optional[BinaryTreeNode]) -> None:
  if node is None:
    return
  post_order_print(node.left)
  post_order_print(node.right)
  print(node.data)

def in_order_print(node: Optional[BinaryTreeNode]) -> None:
  if node is None:
    return
  in_order_print(node.left)
  print(node.data)
  in_order_print(node.right)
  

# pre_order_print(root)
# 0 1 2 9 5 4 6 3 8 7

# post_order_print(root)
# 2 4 5 9 1 8 7 3 6 0
# print("Pre-invert")
# pre_order_print(root)

# root.invert_tree()

# print("Post-invert")
# pre_order_print(root)
# 2 1 5 4 9 0 6 8 3 7
print(root.sum_even_nodes())

