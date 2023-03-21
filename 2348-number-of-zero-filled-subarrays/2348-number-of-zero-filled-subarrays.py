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
        
        # Naive solution
        # def sub_lists (l):
        #     lists = [[]]
        #     for i in range(len(l) + 1):
        #         for j in range(i):
        #             lists.append(l[j: i])
        #     return lists
        # lists = sub_lists(nums)
        # for i in lists:
        #     if len(set(i))==1 and 0 in i:
        #         zerosum+=1
        # return zerosum