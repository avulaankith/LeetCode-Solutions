class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumval = 0
        maxi = nums[0]
        n = len(nums)
        for i in range(0,n):
            sumval += nums[i]
            maxi = max(sumval,maxi)
            if sumval < 0:
                sumval = 0
        return maxi