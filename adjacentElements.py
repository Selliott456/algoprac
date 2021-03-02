# Given an array of integers, find the pair of adjacent elements that has the 
# largest product and return that product.

def adjacent(numbers):
  highest = 0
  for i in range(len(numbers)-1):
    num1 = numbers[i] 
    num2 = numbers[i+1]
    if highest < num1 * num2:
      highest = num1*num2
  print(highest)

adjacent([3, 6, -2, -5, 7, 3])