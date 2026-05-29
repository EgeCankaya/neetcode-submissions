class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hsh_map = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            hsh_map[tuple(count)].append(s)
        return list(hsh_map.values())
            
