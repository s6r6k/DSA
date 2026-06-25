class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #Track:
        #Min price rn, and once i sell my min price becomes the sell price
        #Total profit running sum
        minPrice = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            currPrice = prices[i]
            currProfit = currPrice - minPrice
            if (profit + currProfit) > profit:
                #then i can sell at current price
                minPrice = currPrice
                profit += currProfit
            else:
                if currPrice < minPrice:
                    minPrice = currPrice
        return profit
        