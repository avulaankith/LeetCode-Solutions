class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        hasht = {}
        for i in range(len(nums)):
            s = target - nums[i]
            if s in hasht:
                result.append(i)
                result.append(hasht[s])
                break
            else:
                hasht[nums[i]] = i
        return result

        # result = []
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             result.append(i)
        #             result.append(j)
        #             break
        # return result