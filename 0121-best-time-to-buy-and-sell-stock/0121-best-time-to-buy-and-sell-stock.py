class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            priceTdy = prices[i]
            if priceTdy < minPrice:
                minPrice = priceTdy
            else:
                profitTdy = priceTdy - minPrice
                maxProfit = max(maxProfit, profitTdy)
        return maxProfit
        