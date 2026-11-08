class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)

        for j in range(9):
            seen = set()
            for i in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)

        for boxRow in range(3):
            for boxCol in range(3):
                seen = set()
                for i in range(boxRow * 3, boxRow * 3 + 3):
                    for j in range(boxCol * 3, boxCol * 3 + 3):
                        val = board[i][j]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)

        return True

        