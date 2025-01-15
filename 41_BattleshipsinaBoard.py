class Solution:
    def countBattleships(self, grid: List[List[str]]) -> int:
        ans = 0
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                left = grid[row][col-1] if col - 1 >= 0 else '.' 
                top  = grid[row-1][col] if row - 1 >= 0 else '.' 
                if(grid[row][col] == "X" and left != 'X' and top != 'X'):
                    ans +=1

        return ans