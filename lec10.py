def add(a: int, b: int) -> int:
  return a+b

def multiply(a: int, b: int)->int:
  return a*b

def both(a:int, b:int) -> int:
  ab_sum = add(a, b)
  ab_prod = multiply(a, b)

  print(ab_sum, ab_prod)

# both(2, 18)

# Recursion
def factorial(x: int) -> int:
  if x == 1:
    return 1
  return x * factorial(x-1)

def binary_search(query: int, l_index: int, r_index: int, corpus: list) -> int:
  """
  Return the index of the requested query in the list corpus, or -1 if it doesn't exist
  """
  mid = (l_index + r_index) // 2

  if l_index > r_index:
    return -1
  if corpus[mid] == query:
    return mid
  elif corpus[mid] > query:
    return binary_search(query, l_index, mid-1, corpus)
  elif corpus[mid] < query:
    return binary_search(query, mid+1, r_index, corpus)

# arr: list = [1, 5, 8, 32, 45, 99, 100, 108]
# print(binary_search(45, 0, len(arr)-1, arr))

# 0 1 1 2 3 5 8 13 21 34
def fib(n: int)-> int:
  if n <= 1:
    return n
  else:
    return fib(n-1) + fib(n-2)

def tower_of_hanoi(n: int, from_rod: str, to_rod: str, aux_rod: str):
  if n == 1:
    print(f"Move disk {n} from rod {from_rod} to rod {to_rod}")
    input()
    return
  tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
  print(f"Move disk {n} from rod {from_rod} to {to_rod}")
  input()
  tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)

tower_of_hanoi(4, "A", "C", "B")