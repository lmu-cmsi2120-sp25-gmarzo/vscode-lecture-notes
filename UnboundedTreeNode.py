class UnboundedTreeNode:
  data: int
  children: list

  def __init__(self, data: int):
    self.data = data
    self.children = []
  
  def add_child(self, to_add: int) -> None:
    self.children.append(UnboundedTreeNode(to_add))
  
  def get_child(self, index: int) -> "UnboundedTreeNode":
    if not 0 <= index < len(self.children):
      raise IndexError("Requested index out of range")
    return self.children[index]
  
  def get_data(self) -> int:
    return self.data

root = UnboundedTreeNode(5)
root.add_child(4)
root.add_child(2)
root.add_child(-3)

it = root.get_child(1)
it.add_child(2)
it.add_child(6)