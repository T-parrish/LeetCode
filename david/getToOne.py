class GetToOne:
    def __init__(self, number):
        self.number = number
        self.buffer = [[number]]
    
    counter = 0
    switch = False

    
    def parseTree(self):
        cache=[] 
        
        while self.switch == False:
            window = self.buffer[self.counter]
            for i in window:
                if i %3 == 0:
                    cache.append(int(i / 3))
                if i %2 == 0:
                    cache.append(int(i / 2))
                cache.append(i + 1)
                
            self.buffer.append(cache)
                    
            if 1 in self.buffer[self.counter]:
                self.switch = True
                return self.counter
                break
                
            self.counter+=1
            cache=[]
            
        return self.counter
        
    
            
            
            
        

        
