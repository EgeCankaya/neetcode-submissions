class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        unique = set()
        best = 0

        while r < len(s):
            while s[r] in unique:
                unique.remove(s[l])
                l += 1

            if s[r] not in unique:
                unique.add(s[r])
                best = max(best, r - l + 1)
            r += 1
        return best
        
        