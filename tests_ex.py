from lecture2 import mult_two
import unittest

class multiplyTests(unittest.TestCase):

  def test_mult(self) -> None:
    self.assertTrue(mult_two(6) == 12)


if __name__ == "__main__":
  unittest.main()