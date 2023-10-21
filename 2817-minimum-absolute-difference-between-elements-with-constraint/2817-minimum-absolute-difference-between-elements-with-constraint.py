class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        from sortedcontainers import SortedList
        if x == 0:
            return 0

        n,sl,min_diff = len(nums),SortedList(),10000000000

        for i in range(x,n):
            sl.add(nums[i-x])

            idx = sl.bisect_left(nums[i])
            print(idx)
            if idx < len(sl):
                min_diff = min(min_diff, abs(nums[i]-sl[idx]))
            if idx > 0:
                min_diff = min(min_diff,abs(nums[i]-sl[idx-1]))
            
        return min_diff
