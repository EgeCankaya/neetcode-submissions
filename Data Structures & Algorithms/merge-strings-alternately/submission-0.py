class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        s1, s2 = len(word1), len(word2)
        word3 = ""

        while i < s1 or i < s2:
            if i < s1:
                word3 += word1[i]
            if i < s2:
                word3 += word2[i]
            i += 1

        return word3




        