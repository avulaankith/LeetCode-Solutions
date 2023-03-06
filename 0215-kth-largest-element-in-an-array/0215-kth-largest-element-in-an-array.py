class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums2 = [-1*i for i in nums]
        heapq.heapify(nums2)
        
        for i in range(k-1):
            heapq.heappop(nums2)
        pop = heapq.heappop(nums2)
        return pop*-1
        