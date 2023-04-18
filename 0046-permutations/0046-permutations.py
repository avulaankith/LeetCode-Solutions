class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from collections import deque
        q = deque()
        q.append((nums, []))  # -- nums, path (or perms)
        res = []
        while q:
            nums, path = q.popleft()
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                newNums = nums[:i] + nums[i+1:]
                q.append((newNums, path+[nums[i]]))
        return res