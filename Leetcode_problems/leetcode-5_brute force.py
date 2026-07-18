class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest=s[0]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j]==s[i:j][::-1]:
                    if len(s[i:j])>len(longest):
                        longest=s[i:j]
                    else:
                        pass
                else:
                    pass   
        return longest