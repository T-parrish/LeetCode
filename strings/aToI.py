# Solution 1 beats 99%
# Regex solution -> crawl past empty space to find the first group
# of numbers preceded by a + or - sign. If words or letters are first,
# This will not produce a match. If no match, return 0
# if there is a match, return whichever is smaller between 
# the 32 bit integer and the matched number group if the number is positive
# or return whichever is larger between -2^31 and the matched number if negative

import re
matcher = re.compile('^ *([-\+]?\d+)')

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        match = matcher.match(str)

        if not match:
            return 0
        else:
            num = int(match.group(1))
            if num > 0:
                return min(num, 2**31 - 1)
            elif num < 0:
                return max(num, -2**31)
            else:
                return 0