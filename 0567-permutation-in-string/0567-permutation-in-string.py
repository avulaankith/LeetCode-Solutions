class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1, c2 = Counter(s1), Counter()
        left, right = 0, 0
        while right < len(s2):
            char = s2[right]
            right += 1
            c2[char] += 1
            while c2[char] > c1[char]:
                c2[s2[left]] -= 1
                left += 1
            if right - left == len(s1):
                return True
        return False
       
