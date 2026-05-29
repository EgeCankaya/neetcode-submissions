class Solution:
    def isAnagram(self,s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # 2. O(1) Space: Fixed-size array for 'a' through 'z'
        count = [0] * 26
        
        # 3. O(n + m) Time: Single pass through the strings
        for i in range(len(s)):
            # Increment for string s
            count[ord(s[i]) - ord('a')] += 1
            # Decrement for string t
            count[ord(t[i]) - ord('a')] -= 1
            
        for val in count:
            if val != 0:
                return False
                
        return True
                