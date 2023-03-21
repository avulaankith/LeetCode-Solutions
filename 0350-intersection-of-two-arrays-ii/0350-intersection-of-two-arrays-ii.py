from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        # if len(nums2) < len(nums1):
        #     nums1, nums2 = nums2, nums1
        count = Counter(nums1)
        l = []
        for i in nums2:
            if count[i] > 0:
                count[i]-=1
                l.append(i)
        return l
        