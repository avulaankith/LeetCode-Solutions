class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        cntList = []
        serial = 0
        for i in nums:
            # print("The serial number is {}".format(serial))
            serial += 1
            if i == 1:
                cnt += 1
            else:
                cntList.append(cnt)
                cnt = 0
            # print(cnt)
        cntList.append(cnt)
        # print(cntList)

        # print("Printing the final result")
        return max(cntList)