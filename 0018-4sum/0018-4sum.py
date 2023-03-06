class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # naive Solution
        # nums = sorted(nums)
        # myset = set()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             s = target - nums[i] - nums[j] - nums[k]
        #             if s in nums[k+1:]:
        #                 v = [nums[i],nums[j],nums[k],s]
        #                 v.sort()
        #                 myset.add(tuple(v))
        # return list(myset)

        # Optimized Solution
        nums = sorted(nums)
        myset = set()
        n = len(nums)
        for i in range(n):
            target3 = target - nums[i]
            for j in range(i+1,n):
                left = j+1
                right = n-1
                target2 = target3-nums[j]
                ijsum = nums[i]+nums[j]
                while(left < right):
                    s = nums[left]+nums[right]
                    if s < target2:
                        left += 1
                    elif s > target2:
                        right -= 1
                    else:
                        quad = [nums[i],nums[j],nums[left],nums[right]]
                        myset.add(tuple(quad))

                        while left < right and nums[left] == quad[2]:
                            left += 1
                        while left < right and nums[right] == quad[3]:
                            right -= 1
                while j+1 < n and nums[j] == nums[j+1]:
                    j += 1
            while i+1 < n and nums[i] == nums[i+1]:
                i += 1
        return list(myset)
        