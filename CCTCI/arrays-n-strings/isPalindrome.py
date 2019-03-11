# given a string, determine if it is a permutation of a palindrome
# Example -> tact coa -> taco cat || atco cta, etc etc

# if each letter occurs 2x with max 1 letter occuring 1x
# you can assume that the input is a palindrome permutation
def isPalindrome(string):
  dict = {}
  count = 0
  cleanString = string.lower().strip()
  # Tally the letter counts in a dictionary
  for i in range(len(cleanString)):
    if cleanString[i] not in dict:
      dict[cleanString[i]] = 1
    else:
      dict[cleanString[i]] += 1
  
  # Mod each value in the dictionary to count evens
  # if mod 2 != 0 -> the letter occurs an odd number of times
  for i in range(len(dict.items())):
    if dict.items()[i][1] % 2 != 0:
      count +=1

  # If we have more than 1 odd letter occurrence, it cannot 
  # be a permutation of a palindrome. return false
  if count > 1:
    return False
  else: 
    return True
  
  