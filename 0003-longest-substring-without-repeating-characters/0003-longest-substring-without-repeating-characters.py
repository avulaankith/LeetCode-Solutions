class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def checkUnique(string):
            return len(set(string)) == len(string)
        
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        l = 0
        maxLength = -1

        charset = set()

        for r in range(len(s)):
            if s[r] in charset:
                while(l < r and s[r] in charset):
                    charset.remove(s[l])
                    l += 1
            charset.add(s[r])
            maxLength = max(maxLength,r-l+1)
        return maxLength
        

        # Optimized Solution 2
        # string = ""
        # maxLength = 0

        # for c in list(s):
        #     current = "".join(c)

        #     if current in string:
        #         string = string[string.index(current)+1:]

        #     string += c
        #     maxLength = max(maxLength,len(string))
        # return maxLength

        # Naive Solution
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         substr = s[i:j+1]

        #         if checkUnique(substr):
        #             maxLength = max(len(substr),maxLength)

        # return maxLength

                