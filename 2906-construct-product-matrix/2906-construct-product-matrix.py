class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        final_grid = grid.copy()
        flat_list = []
        num_cols = len(grid[0])
        
        product = 1
        zero_count = 0
        for row in grid:
            for ele in row:
                if(ele % 12345 == 0):
                    zero_count+=1

                flat_list.append(ele)
                product *= ele
    
        if zero_count > 1:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    ele = grid[i][j]
                    # flat_list_ele = flat_list[i * num_cols + j]
                    final_grid[i][j] = 0
            return final_grid
        elif zero_count == 1:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    ele = grid[i][j]
                    if ele%12345 != 0:
                    # flat_list_ele = flat_list[i * num_cols + j]
                        final_grid[i][j] = 0
                    else:
                        final_grid[i][j] = int((product//ele) % 12345)
            return final_grid
        
        else:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    ele = grid[i][j]
                    final_grid[i][j] = int((product//ele) % 12345)
            return final_grid
        
        return final_grid
                