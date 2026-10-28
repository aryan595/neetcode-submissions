class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        #find correct row using BS
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = top + ((bot - top) // 2)

            if target > matrix[row][-1]:
                top = row + 1
            
            elif target < matrix[row][0]:
                bot = row - 1

            else:
                break

        if not (top <= bot):
            return False
        
        #Find element on that correct row using BS
        l, r = 0, COLS - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if target > matrix[row][mid]:
                l = mid + 1
            
            elif target < matrix[row][mid]:
                r = mid - 1
            
            else:
                return True
        
        return False