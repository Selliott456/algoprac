# You are given a two-digit integer n. Return the sum of its digits.
def addTwo(n):
  string = str(n)
  nums = []
  total = 0
  for i in string:
    nums.append(i)

  for i in nums:
    total += int(i)
  print(total)

addTwo(89)