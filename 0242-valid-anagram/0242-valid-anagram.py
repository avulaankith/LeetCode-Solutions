from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic_s, dict_t = Counter(s), Counter(t)

        if dic_s == dict_t:
            return True
        else:
            return False
