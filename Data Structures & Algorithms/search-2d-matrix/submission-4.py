class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1. Initialize with the number of ROWS (len(matrix))
        bot, top = 0, len(matrix) - 1
        m = 0

        while bot <= top:
            m = (bot + top) // 2
            if target > matrix[m][-1]:
                bot = m + 1
            elif target < matrix[m][0]:
                top = m - 1
            else:
                break
                
        if bot > top:
            return False

        l, r = 0, len(matrix[0]) - 1

        # Second Binary Search: Find the target in row 'm'
        while l <= r:
            mid = (l + r) // 2
            if matrix[m][mid] == target:
                return True 
            elif matrix[m][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False