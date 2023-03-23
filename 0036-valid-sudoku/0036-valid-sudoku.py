class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        blocks = [[set() for i in range(3)] for j in range(3)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                ele = board[i][j]
                if ele == ".":
                    continue
                else:
                    if (ele not in rows[i]) and (ele not in cols[j]) and (ele not in blocks[i//3][j//3]):
                        rows[i].add(ele)
                        cols[j].add(ele)
                        blocks[i//3][j//3].add(ele)
                        continue
                    else:
                        return False
        
        return True