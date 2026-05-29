class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen = set()
        res = 0
        if len(s) == 0:
            return 0
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

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen = set()
        res = 0
        
        if len(s) == 0:
            return 0
            
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1 
            seen.add(s[r])
            res = max(res, len(seen)) 
            
            r += 1
            
        return res