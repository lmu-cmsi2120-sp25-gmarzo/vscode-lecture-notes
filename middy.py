class NerdCat:
  def __init__(self, name):
    self.name = name

name = "bob" 
bob = NerdCat(name) 

# print(bob)
# print(bob.name) 


def count_to_nfinity(n: int) -> None: 
  
  var = "a"
  sum = 200000314134 + 61241342543 #c_1
  print("Hello")

  for i in range(n): # n
    for j in range(n): # n * n
      print(i+1, j+1) #c_1 * N^2

# count_to_nfinity(7)

# Constant: O(1)
# Logarithmic: O(log(n))
# Linear: O(n)
# Linearithmic: O(n * log(n))
# Quadratic: O(n^2)

def cookies(kids: int): # n + n^2(1 + c_1 + c_2) => O(n^2)
  for kid in range(kids):#n
    for _ in range(5): #n * 5
      print("Have a cookie!") #c_1 * (n+5)
      print("He need some milk") #c_2 * (n+5)

# Logarithmic: O(log(n))

def count_down(n: int):
  for i in range(n): #n
    while i > 0: #log(n)
      print(i)
      i = i // 2

count_down(10000000) 

#O(n)
#O(nlog(n))
# n