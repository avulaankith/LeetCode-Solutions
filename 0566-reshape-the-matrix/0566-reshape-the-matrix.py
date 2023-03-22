class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat

        l = []
        flat = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                flat.append(mat[i][j])
        count = 0
        for i in range(r):
            nl = []
            for j in range(c):
                var = flat[count]
                nl.append(var)
                count += 1
            l.append(nl)
        return l