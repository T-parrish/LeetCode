class GetToOne:
    def __init__(self, number):
        self.number = number
        self.buffer = [[number]]
    
    counter = 0
    
    def parseTree(self):
        cache=[] 
        
        while True:
            window = self.buffer[self.counter]
            for i in window:
                if i %3 == 0:
                    cache.append(int(i / 3))
                if i %2 == 0:
                    cache.append(int(i / 2))
                cache.append(i + 1)
                
            self.buffer.append(cache)
                    
            if 1 in self.buffer[self.counter]:
                return self.counter
                
            self.counter+=1
            cache=[]