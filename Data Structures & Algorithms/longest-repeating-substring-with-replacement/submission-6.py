class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l , r = 0, 0
        count = {}
        mx = 0
        res = 0

        while r < len(s):
            count[s[r]] = 1 + count.get(0, s[r])
            mx = max(count.values()) 
            total = mx + (r - l)

            if total <= k:
                res = max(res, total)
            else:
                count[s[l]] -= 1
                l += 1

            r += 1
        
        return res