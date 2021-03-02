# 1. Write a function that returns the sum of two numbers.
# 2. Write a function that returns the sum of all numbers regardless of # of params.
def add(a, b):
  print(a + b)
  

def add_all(*arguments):
  result = 0
  for i in arguments:
    result += i
  print(result)
  

add(10, 20)
add_all (10, 10, 10, 10)