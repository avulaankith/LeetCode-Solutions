class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l2 = [i**2 for i in nums]
        return sorted(l2)