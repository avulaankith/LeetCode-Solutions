class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}

        for i in string.ascii_lowercase:
            dic[i] = -1
        
        for i in range(len(s)):
            char = s[i]
            if dic[char] == -1:
                dic[char] = i
            elif dic[char] > -1:
                dic[char] = -2
        # print(dic)
        minimum = 999999999
        for i in dic:
            if dic[i] > -1:
                minimum = min(minimum, dic[i])
        if minimum == 999999999:
            return -1
        return minimum