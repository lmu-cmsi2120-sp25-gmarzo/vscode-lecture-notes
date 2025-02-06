def f(a: int) -> int:
  return a + 2

def g(a: int, b: int) -> int:
  return f(a) * b

def main() -> None:
  bob = 7
  billy = 9

  print(g(bob, billy))