class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = []
        maxval = amount+1
        for i in range(maxval):
            res.append(maxval)
        res[0] = 0

        for i in range(1,maxval):
            for j in range(len(coins)):
                if (coins[j] <= i):
                    res[i] = min(res[i],(res[i-coins[j]])+1)
        
        print(res)

        if res[amount] > amount:
            return -1
        else:
            return res[amount]