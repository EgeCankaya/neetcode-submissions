class Solution:
    def isValid(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == "[" and s[r] == "]":
                l += 1
                r-=1
            elif s[l] == "(" and s[r] == ")":
                l += 1
                r-=1
            elif s[l] == "{" and s[r] == "}":
                l += 1
                r-=1
            else:
                return False
        return True
        