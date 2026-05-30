class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        
        bot, top = 0, r
        m = 0

        while bot <= top:
            m = (bot + top) //2
            if target > matrix[m][-1]:
                bot = m + 1
            elif target < matrix[m][0]:
                top = m - 1
            else:
                break

        while l <= r:
            mid = (l + r) // 2
            
            if matrix[m][mid] == target:
                return True 
            elif matrix[m][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False




