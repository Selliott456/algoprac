# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

def addBorder(picture):
  star_num = len(picture[0])+2
  st = ""
  new_array = []
  
  for word in picture:
    new_array.append("*" + word + "*")
  for i in range(star_num):
    st = "*"*star_num

  new_array.append(st)
  new_array.insert(0, st)
  for i in new_array:
    print(i)


addBorder(["abcd",
           "efgh"])