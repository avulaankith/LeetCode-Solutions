class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # naive Solution
        # if not nums:
        #     return 0
        # nums.sort()
        # ans = 1
        # prev = nums[0]
        # cur = 1
        # for i in range(1, len(nums)):
        #     if nums[i] == prev + 1:
        #         cur += 1
        #     elif nums[i] != prev:
        #         cur = 1
        #     prev = nums[i]
        #     ans = max(ans, cur)
        # return ans

        # Optimized Solution
        if not nums:
            return 0
        hashset = set()
        ans =  1
        
        for i in nums:
            hashset.add(i)
            
        for num in nums:
            if (num-1) not in hashset:
                currNum = num
                curr = 1
                while(currNum+1) in hashset:
                    currNum+=1
                    curr+=1
                ans = max(curr,ans)
        return ans
