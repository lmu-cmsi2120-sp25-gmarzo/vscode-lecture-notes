from BinaryTreeNode import *
import unittest

class TreeTests(unittest.TestCase):

  def setUp(self) -> None:
    self.root = BinaryTreeNode(0)
    lc = root.left = BinaryTreeNode(1)
    rc = root.right = BinaryTreeNode(6)

    lc.left = BinaryTreeNode(2)
    lcr = lc.right = BinaryTreeNode(9)

    lcr.left = BinaryTreeNode(5)
    lcr.left.right = BinaryTreeNode(4)

    rcl = rc.left = BinaryTreeNode(3)
    rcl.left = BinaryTreeNode(8)
    rcl.right = BinaryTreeNode(7)


  def test_invert(self) -> None:
        self.root.invert_tree()
        self.assertEqual(self.root.left.data, 6)
        self.assertEqual(self.root.right.data, 1)

  def test_is_bst(self) -> None:
      self.assertFalse(self.root.is_binary_search_tree())
  
  def test_sum_even(self) -> None:
      self.assertEqual(self.root.sum_even_nodes(), 0 + 2 + 6 + 8 + 4)


if __name__ == "__main__":
  unittest.main()