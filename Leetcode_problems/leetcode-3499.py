class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        zeros = list(map(len, filter(None, s.split("1"))))
        maxzeros = max((a + b for a, b in zip(zeros, zeros[1:])), default=0)
        return s.count("1") + maxzeros
s=input()
#s=0100
print(Solution().maxActiveSectionsAfterTrade(s))