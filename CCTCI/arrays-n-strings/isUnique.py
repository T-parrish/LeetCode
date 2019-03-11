# Implement an algorithm to determine if a 
# string has all unique characters

tests = ['foo', 'bar', '', 'Ice cream', 'ShaZzam', '']

# Best case time complexity: O(nLogn)
# Sorting algorithm is O(nLogn), + O(n) for the sliding window
# Which reduces to O(nLogn + n) or O(nLogn)
# Best case space complexity: O(n)
# Since we're storing the string in a list, we're using O(n) space
def sortUnique(string):
  # Make string lowercase to account for cap edge cases
  letterArray = list(string.lower())
  # Sort so all like characters are clumped
  letterArray.sort()

  # Set counter / range for sliding window
  i = 0
  n = len(letterArray)
  while i < n-1:
    # if two letters are clumped, return false and break
    if letterArray[i] == letterArray[i+1]:
      return False
      break
    i += 1

  return True
    
# Solution using a dictionary / hashmap
# Worst case space: O(n)
# if the function doesn't break, will store entire
# string in hashmap / dictionary
# Worst case time: O(n)
# if the function doesn't break, will iterate
# over the entire string
def dictUnique(string):
  dict = {}
  # clean the string
  cleanString = string.lower()

  for i in range(len(cleanString)):
    if cleanString[i] not in dict:
      dict[cleanString[i]] = 1
    else:
      dict[cleanString[i]] -=1

    if dict[cleanString[i]] <= 0:
      return False
      break
  
  return True


def bruteUnique(string):
  cleanString = string.lower()

  for i in range(len(cleanString)- 1):
    for j in range(len(cleanString)):
      print('i output: {}').format(i)
      print('j output: {}').format(j)
  