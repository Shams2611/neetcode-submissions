class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)

            else:
                l = r

            r += 1


        return max_profit


        





# thought process 
# go through each number in the array starting an L pointer and a right pointer 
# initialize the profit as zero 
# starting 1st one l compared to L + 1 then get the absolute value of it and make that the max for now
# then compare l to l + 1 and see the absolute value 