class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp build table
        # dp[i] the smallest number of coins used to build amount i
        # base case
        # dp[0] =0
        dp = [0]+[float(inf) for i in range(amount)]
        
        # induction rule
        # dp[i] = min(dp[i-coin]+1)
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin>=0:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        # return check is max or num     
        if dp[-1]==float(inf):
            return -1
        else:
            return dp[-1]
