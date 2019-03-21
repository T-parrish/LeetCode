# Find shortest path to 1 given an int
# You can divide by 3 if int is divisible by 3
# You can divide by 2 if int is divisible by 2
# You can add 1

class GetToOne(self, int):
  def __init__(self, int):
    self.int = int

  buffer = [[int]]
  allUniqueNodes = set([i for sub in buffer for i in sub])
  counter = 0
  
  def parseTree(self, int):
    cache = []
    while true:
      for i in self.buffer[self.counter]:
        if int % 3 === 0:
          cache.push(int/3)
        if int % 2 === 0:
          cache.push(int/2)
        cache.push(int + 1)

      self.buffer.push(cache)
      self.counter += 1
      cache = []

      if 1 in self.buffer[self.counter]:
        return self.counter
        break

    
