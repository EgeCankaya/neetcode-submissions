class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(c for c in s if c.isalnum())
        clean = clean.lower()
        size = len(clean)
        isOdd = (size % 2 == 1)
        palindrome = True

        if isOdd:
            for x in range(size // 2):
                if clean[x] != clean[size - 1 - x]:
                    palindrome = False
        else:
            for x in range(size / 2):
                if clean[x] != clean[size - x]:
                    palindrome = False
        return palindrome

        