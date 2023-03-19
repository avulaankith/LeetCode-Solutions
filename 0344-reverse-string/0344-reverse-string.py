class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        n = len(s)-1
        for i in range(len(s)//2):
            j = n - i
            temp = s[j]
            s[j] = s[i]
            s[i] = temp
        