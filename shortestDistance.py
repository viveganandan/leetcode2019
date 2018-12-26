class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        j, k = float('inf'), float('inf')
        d = float('inf')
        for i in range(len(words)):
            if words[i] == word1:
                j = i
            elif words[i] == word2:
                k = i
            if abs(j - k) <= d:
                d = abs(j - k)
        return d
