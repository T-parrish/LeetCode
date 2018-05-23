# Solution 1: beats 14%
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        stock = []
        liquid = []
        
        stock = [prices[i] for i in range(len(prices)-1) if prices[i] > prices[i+1]]
        liquid = [prices[i+1] - prices[i] for i in range(len(prices)-1) if prices[i] < prices[i+1]]
        
        return sum(liquid)

# Solution 2: beats 84%
# Realized that the stock and liquid containers weren't necessary
# Creating them for each test case was the main factor for slow runspeed in #1
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        stock = [prices[i] for i in range(len(prices)-1) if prices[i] > prices[i+1]]
        liquid = [prices[i+1] - prices[i] for i in range(len(prices)-1) if prices[i] < prices[i+1]]
        
        return sum(liquid)

# Solution 3: beats 98%
# Realized that the stock container wasn't actually doing anything, as all
# The calculations were accounted for in the liquid container.
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        liquid = [prices[i+1] - prices[i] for i in range(len(prices)-1) if prices[i] < prices[i+1]]
        
        return sum(liquid)
                


