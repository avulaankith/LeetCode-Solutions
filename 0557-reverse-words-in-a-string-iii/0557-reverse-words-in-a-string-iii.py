class Solution:
    def reverseWords(self, s: str) -> str:
        st = ""
        l = s.split(" ")

        l2 = []
        for i in l:
            l2.append(i[::-1])
        
        for i in l2:
            st += i
            st += " "
        
        return st[:-1]
