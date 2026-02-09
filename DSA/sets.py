s = set() # time complexity 1

arr = [1,2,3,4,5,6,6,7,7,7,7,7]

s = set(arr) # time complexity n

s.add(11) # time complexity 1

s.remove(11) # keyerror is missing # time complexity 1

s.discard(11) # safe is missing # time complexity 1

t = 11 in s # time complexity 1