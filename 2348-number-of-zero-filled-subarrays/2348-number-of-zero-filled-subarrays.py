class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0

        zerosum = 0
        count = 0
        for i in nums:
            if i == 0:
                count += 1
                zerosum += count
            else:
                count = 0
        
        
        return zerosum