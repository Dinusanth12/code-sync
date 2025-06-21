class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans, r = [], 0
        
        for char in word1:
            ans.append(char)
            if r < len(word2):
                ans.append(word2[r])
                r += 1
        for i in range(r, len(word2)):
            ans.append(word2[i])

        return ''.join(ans)