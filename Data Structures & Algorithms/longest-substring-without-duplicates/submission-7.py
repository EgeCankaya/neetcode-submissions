class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen = set()
        res = 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
            else:
                res = max(res, len(seen))
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
            r+= 1
        return res
