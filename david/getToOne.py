class GetToOne(self, int):
  def __init__(self, int):
    self.int = int

  buffer = set()
  allUniqueNodes = set()
  counter = 0
  
  def parseTree(self, int):
    if int % 3 === 0:
      buffer.add(int/3)
      allUniqueNodes.add(int/3)
    if int % 2 === 0:
      buffer.add(int/2)
      allUniqueNodes.add(int/2)

    buffer.add(int+1)
    allUniqueNodes.add(int+1)

    self.counter +=1
    if 1 in self.buffer:
      return counter

    for i in range(len(buffer)):
      parseTree(buffer[i])

    
