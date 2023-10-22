from sortedcontainers import SortedList
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        s = SortedList()
        for i in range(1,len(nums)-1):
            val = nums[i]
            
            minleft = 999999
            leftidx = -1
            minright = 99999
            rightidx = -1
            
            leftsa = nums[:i]
            rightsa = nums[i+1:]
            
            for j in range(len(leftsa)):
                if minleft > leftsa[j]:
                    minleft = leftsa[j]
                    leftidx = j
            for j in range(len(rightsa)):
                if minright > rightsa[j]:
                    minright = rightsa[j]
                    rightidx = j+i+1
            
            if val > minleft and val > minright:
                s.add(minleft+val+minright)
        
        if len(s) > 0:
            return s[0]
        
        return -1