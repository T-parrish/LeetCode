# Takes an array of tuples, where times[0] is start
# and times[1] is end time - can be any number
# overlapped time does compound between guards / times
# return total time worked in a 24 hour day
# times must be between 0 and 24

# Solution: O(nLogn) for sort + O(n) for iteration
# reduces to O(n + nLogn) => O(nLogn) time & O(1) space
def getHours(times):
  times.sort(key=lambda)
  base = times[0][0]
  buffer = 0
  for i in range(len(times)):
    if times[i][0] <= base <= times[i][1]:
      buffer += times[i][1] - base
      base = times[i][1]
    if times[i][0] >= base:
      buffer += times[i][1] - times[i][0]
      base = times[i][1]
  
  return buffer