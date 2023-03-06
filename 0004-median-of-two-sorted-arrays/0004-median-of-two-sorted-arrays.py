class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findmedian(arr):
            median = 0
            n = len(arr)
            if n == 0:
                return 0
            if n == 1:
                return arr[0]
            if len(arr)%2 == 0:
                median = (arr[(n - 1)//2] + arr[n//2])/2
            else:
                median = arr[n//2]
            return median
        if len(nums1) == 0:
            return findmedian(nums2)
        elif len(nums2) == 0:
            return findmedian(nums1)
        lis = []
        def merge(a, b):
            lis = []
            n = len(a)
            m = len(b)
            i = 0
            j = 0
            while(i < n and j < m):
                if a[i] < b[j]:
                    lis.append(a[i])
                    i += 1
                else:
                    lis.append(b[j])
                    j += 1
            if i < n:
                lis.extend(a[i:])
            elif j < m:
                lis.extend(b[j:])

            return lis

        lis = merge(nums1,nums2)
        print(lis)
        # lis = [i for i in nums1]
        # for i in nums2:
        #     lis.append(i)
        # lis = sorted(lis)
        return findmedian(lis)
        # medlist = []
        # med1 = findmedian(nums1)
        # med2 = findmedian(nums2)
        # medlist.append(med1)
        # medlist.append(med2)
        # finalans = findmedian(medlist)
        # return finalans
