class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l , r = 0, 0
        count = {}
        mx = 0
        res = 0

        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            mx = max(mx, count[s[r]]) 
            total = mx + (r - l) + 1

            if total <= k:
                res = max(res, total)
            else:
                count[s[l]] -= 1
                l += 1

            r += 1
        
        return res