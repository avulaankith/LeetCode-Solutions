class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        for _ in range(numRows-2):
            nl = [1]
            for i in range(len(l[-1])-1):
                s=l[-1][i]+l[-1][i+1]
                nl.append(s)
            nl.append(1)
            l.append(nl)
        return l