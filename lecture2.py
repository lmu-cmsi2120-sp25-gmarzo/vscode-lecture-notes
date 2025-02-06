import random

my_str: str = "a string"
my_int: int = 24
my_float: float = 25.0
my_bool: bool = True

breakfast: list[str] = ["Nothing", "Coffee", "Cereal", "Captain Crunch", "Fried Rice"]
# immutable_breakfast: tuple[str] = ("Nothing", "Coffee", "Cereal", "Captain Crunch", "Fried Rice")
# my_dict: dict[str,str] = {"one":"ha na", "two": 2, (0, 0): False}


my_set: set = {"item 1", "item 2", 3, 4}
my_set2: set = {"item 1", "item 2", 3, 4}

# COnditionals
if "a":
  pass
elif "b":
  pass
else:
  pass

# Loops
# for _ in range(3):
  # print("beetle juice")



def mult_two(num: int|float) -> int|float:
  """
  Takes an input num and returns num multiplied by 2

  Parameters:
  - num: int|float

  Returns:
  - num multiplied by 2
  """
  return num * 3


