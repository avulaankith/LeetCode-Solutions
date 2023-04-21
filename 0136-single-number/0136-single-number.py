class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}

        for i in set(nums):
            dic[i]=0
        
        for i in nums:
            dic[i] += 1

        for i in dic:
            if dic[i] == 1:
                return i