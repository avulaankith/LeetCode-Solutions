class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        min_index = 0
        max_index = 0
        for i in range(indexDifference,len(nums)):
            if nums[i-indexDifference] < nums[min_index]:
                min_index = i-indexDifference
            if nums[i-indexDifference] > nums[max_index]:
                max_index = i- indexDifference
            
            if abs(nums[i] - nums[min_index]) >= valueDifference:
                return [min_index,i]
            if abs(nums[i] - nums[max_index]) >= valueDifference:
                return [max_index,i]
            
        return [-1,-1]
            