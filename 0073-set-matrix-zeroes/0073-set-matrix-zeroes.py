class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowList = []
        colList = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowList.append(i)
                    colList.append(j)
        rlist = set(rowList)
        clist = set(colList)
        rowList = list(rlist)
        colList = list(clist)
        
        for i in rowList:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for j in colList:
            for i in range(len(matrix)):
                matrix[i][j] = 0
        
        
        
        


