class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = 0
        cm, cn = len(matrix) - 1, len(matrix[0]) - 1
        fixed = False

        while not fixed:
            if m > cm:
                return False
            if matrix[m][0] <= target <= matrix[m][cn]:
                fixed = True
            else:
                m += 1
        
        l, r = 0, cn 

        while l <= r:
            mid = (r + l) // 2

            if matrix[m][mid] == target:
                return True
            elif matrix[m][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
 
