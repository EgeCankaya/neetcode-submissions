class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(c for c in s if c.isalnum())
        clean = clean.lower()
        size = len(clean)
        for x in range(size // 2):
            if clean[x] != clean[size - 1 - x]:
                return False
        return True