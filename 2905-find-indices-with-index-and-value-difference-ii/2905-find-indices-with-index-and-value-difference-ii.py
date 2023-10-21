from sortedcontainers import SortedList
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        # min_index = 0
        # max_index = 0
        # for i in range(indexDifference,len(nums)):
        #     if nums[i-indexDifference] < nums[min_index]:
        #         min_index = i-indexDifference
        #     if nums[i-indexDifference] > nums[max_index]:
        #         max_index = i- indexDifference
            
        #     if abs(nums[i] - nums[min_index]) >= valueDifference:
        #         return [min_index,i]
        #     if abs(nums[i] - nums[max_index]) >= valueDifference:
        #         return [max_index,i]
            
        # return [-1,-1]
        sl = SortedList()
        min_index = 0
        max_index = 0
        for i in range(indexDifference,len(nums)):
            sl.add([nums[i-indexDifference],i-indexDifference])

            minval = sl[0]
            maxval = sl[-1]

            if abs(nums[i]-minval[0]) >= valueDifference:
                return [minval[1],i]
            if abs(nums[i]-maxval[0]) >= valueDifference:
                return [maxval[1],i]
        return [-1,-1]            