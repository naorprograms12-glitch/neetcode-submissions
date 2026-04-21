class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_l = [prices[0] for i in range(n)]
        for i in range(1,n):
            min_l[i] = min(min_l[i-1], prices[i])
        print(min_l)
        rev_prices = prices[::-1]

        max_r = [rev_prices[0] for i in range(n)]
        for i in range(1,n):
            max_r[i] = max(max_r[i-1], rev_prices[i])

        max_r.reverse()
        print(max_r)
        max_v =0

        for i in range(n-1):
            delta = max_r[i+1] - min_l[i]
            if delta > max_v:
                max_v = delta
        
        return max_v
            