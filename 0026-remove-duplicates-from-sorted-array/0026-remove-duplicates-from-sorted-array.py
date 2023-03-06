class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        # print(l)
#         j = 0
#         for i in range(len(nums)):
            
#             j+=1
            
#             if i == j and (i == len(nums) - 1):
#                 break
            
#             if j > len(nums)-1:
#                 break
#             if nums[j] == nums[i]:
#                 nums.pop(j)
#                 j = i
#                 continue
        s = set(nums)
        s = list(s)
        s = sorted(s)
        # print(s)
        i = 0
        while(l!=0):
            nums.pop(i)
            l = len(nums)
        # print(nums)
        for i in s:
            nums.append(i)
        # print(nums)
        # print(len(nums))
        return len(nums)