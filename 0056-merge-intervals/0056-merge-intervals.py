class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals = sorted(intervals)
        for i in range(len(intervals)):
            if (len(merged) == 0) or (merged[-1][1] < intervals[i][0]):
                l = [intervals[i][0],intervals[i][1]]
                merged.append(l)
            else:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
        return merged