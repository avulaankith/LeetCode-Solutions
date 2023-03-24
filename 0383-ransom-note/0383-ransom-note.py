from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic_ransom, dic_magazine = Counter(ransomNote), Counter(magazine)

        for i in dic_ransom:
            if i not in dic_magazine:
                return False
            else:
                dic_magazine[i] -= dic_ransom[i]
                if dic_magazine[i] < 0:
                    return False
        return True