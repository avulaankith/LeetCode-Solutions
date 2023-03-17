class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        l = l[::-1]
        st = ""
        for i in l:
            st += i+" "
        
        st = st[:-1]
        return st
        
        

