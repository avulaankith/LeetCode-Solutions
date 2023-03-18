class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        hash = {}

        for i in range(len(numbers)):
            target2 = target - numbers[i]
            if target2 in numbers[i+1:]:
                idx = numbers[i+1:].index(target2)
                return [i+1,idx+2+i]