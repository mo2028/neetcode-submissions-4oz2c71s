class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low an sell high
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            print(prices[l], prices[r])
            if prices[l] >= prices[r]:
                # print('loss')
                
                l = r
                r+=1
            else:
                maxProfit = max(maxProfit, (prices[r]-prices[l]))
                r+=1
                # l+=1
            print(maxProfit)
        return maxProfit


        