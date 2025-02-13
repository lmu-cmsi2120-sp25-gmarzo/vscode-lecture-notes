def f(x): # T(n) = c_1 + c_2
  print(x) #c_1
  loc_var = "bob" #c_2

def g(x: int) -> None: #T(n) = n(c_1 + c_2) + 5(c_3)
  for num in range(x): #c_1 * n
    print(num) #c_2 * n
  
  print("hi") #c_3
  print("my")
  print("name")
  print("is")
  print("peanut butter and jelly sandwich")

def pairs(y: int) -> None: # T(n) = 2n^2 + 3n^1 + 2n^0
  for i in range(y): #c_1 * n
    for j in range(y): #c_2 * n^2
      print(i, j) #c_3 * n^2
  
  for num in range(y): #c_4 * n
    print(num + 6) #c_5 * n
  
  a = 6 #c_6
  c = a ** 2 #c_7

# O(f(n)) = O(1)
# O(g(n)) = O(n)
# O(pairs(n)) = O(n^2)


g(7239)