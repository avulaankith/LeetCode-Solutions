class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = [0 for i in range(len(nums))]
        for i in nums:
            l[i-1] += 1
        idx = -1
        
        for i in l:
            if i > 1:
                return l.index(i)+1