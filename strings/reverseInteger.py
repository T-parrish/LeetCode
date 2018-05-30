# Solution #1 beats 97%
# Lots of conditional logic, not a very pretty solution
# but hey, it works.
temp = abs(x)
        cont = str(x)
        overflow = 2**31
        
        if x < 0 and str(temp)[-1] != 0:
            res = int(str(temp)[::-1])
            if res > overflow:
                return 0
            else:
                return res * -1
            
        
        elif x < 0 and str(temp)[-1] == 0:
            temp.pop()
            res = int(str(temp)[::-1])
            if res > overflow:
                return 0
            else:
                return res * -1
        
        if str(temp)[-1] == 0:
            temp.pop()
            res = int(str(temp)[::-1])
            if res > overflow:
                return 0
            else:
                return res
        
        else:
            res = int(str(temp)[::-1])
            if res > overflow:
                return 0
            else:
                return res