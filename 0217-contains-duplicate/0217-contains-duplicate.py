class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        sl = len(s)

        if sl < len(nums):
            return True
        else:
            return False