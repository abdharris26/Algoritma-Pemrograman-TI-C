#bubble sort
# mylist = [64, 34, 25, 12, 22, 11, 90, 5]

# n = len(mylist)
# for i in range(n-1):
#   for j in range(n-i-1):
#     if mylist[j] > mylist[j+1]:
#       mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

# print(mylist)


mylist = [7, 3, 9, 12, 11]

n = len(mylist)
for i in range(n-1):
  swapped = False
  for j in range(n-i-1):
    if mylist[j] > mylist[j+1]:
      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
      swapped = True
  if not swapped:
    break

print(mylist)

#selection sort

mylist = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(mylist)
for i in range(n-1):
  min_index = i
  for j in range(i+1, n):
     if mylist[j] < mylist[min_index]:
       min_index = j
  min_value = mylist.pop(min_index)
  mylist.insert(i, min_value)

print(mylist)