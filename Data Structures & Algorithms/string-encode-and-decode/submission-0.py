class Solution:

    def encode(self, strs):
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + "#" + s)
        return "".join(encoded)

    def decode(self, s):
        res = []
        i = 0
        
        while i < len(s):
            # Find the delimiter '#'
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])   # extract length
            j += 1                 # move past '#'
            
            # Extract the string of that length
            res.append(s[j : j + length])
            
            i = j + length         # move pointer forward
        
        return res
