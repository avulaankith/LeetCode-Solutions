class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st = ""
        for i in digits:
            st = st + str(i)
            
        sti = int(st) + 1
        sti = str(sti)
        # sti = sti.split()
        digits2 = []
        # print(sti)
        for i in range(len(sti)):
            digits2.append(int(sti[i]))
        return digits2