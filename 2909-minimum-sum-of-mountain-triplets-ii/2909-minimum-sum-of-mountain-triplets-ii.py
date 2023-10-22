from sortedcontainers import SortedList
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        s = SortedList()
        left = [0 for i in range(len(nums))]
        left[0] = nums[0]
        right = [0 for i in range(len(nums))]
        right[len(nums)-1] = nums[len(nums)-1]
        for i in range(1,len(nums)):
            left[i] = min(left[i-1],nums[i])
        for i in range(len(nums)-2,-1,-1):
            right[i] = min(right[i+1],nums[i])

        for i in range(1,len(nums)-1):
            minleft = left[i]
            minright = right[i]
            val = nums[i]
            
            if val > minleft and val > minright:
                s.add(minleft+val+minright)
        
        if len(s) > 0:
            return s[0]
        
        return -1