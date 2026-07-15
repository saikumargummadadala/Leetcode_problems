class Solution(object):
    def gcdOfOddEvenSums(self, n):
        def hcf(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        even=n*(n+1)
        odd=n**2
        return (hcf(even,odd))
print(Solution().gcdOfOddEvenSums(int(input())))