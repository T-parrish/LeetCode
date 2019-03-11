# There are three types of edits that can be performed
# on strings: insert, delete, replace. Write a function
# to check if two strings are one edit away from each other.

def isOneAway(a, b):
  # if the length diff > 1, can't be one edit away
  if abs(len(a) - len(b)) > 1:
    return False
  
  minLength = min(len(a), len(b))
  # track number of differences
  counter = 0
  i = 0
    
  while i < minLength:
    if a[i] != b[i]:
      counter +=1
      if counter > 1:
        return False
        break
    i+=1

  print(counter)
  # One edit away if same string length and 1 counter inc
  if len(a) == len(b) and counter <=1:
    return True
  
  # One edit away if not same length and counter = 0
  # function already returns false if distance between
  # two string lengths exceeds 1, so this catches
  # cases where the length of one string is only 1 more 
  # than the other string
  if len(a) != len(b) and counter == 0:
    return True



