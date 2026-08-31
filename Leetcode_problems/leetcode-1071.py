class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        repeat=len(str1)//len(str2)
        if str2*repeat in str1:
            return str1[len(str2)*repeat:]
        else:
            return str2[repeat:]
str1 = "ABABAB"
str2 = "ABAB"
print(Solution().gcdOfStrings(str1, str2))