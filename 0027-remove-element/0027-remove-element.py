class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        count = 0
        for i in nums:
            if i == val:
                count+=1
        # if count == 1:
        #     return l
        
        for i in range(count):
            nums.remove(val)
        
        return len(nums)