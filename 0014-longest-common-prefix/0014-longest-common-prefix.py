class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = len(strs)
        n = size
        if size == 0:
            return ""
        elif size == 1:
            return strs[0]

        result = ""

        short = 999999999999999999999999
        for i in strs:
            short = min(short,len(i))

        for i in range(short):

            currentChar = strs[0][i]

            for j in range(1,n):
                if strs[j][i] != currentChar:
                    return result
                
            result += currentChar
        
        return result