class Solution(object):
    def gcdOfOddEvenSums(self, n):
        def hcf(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        even=n*(n+1)#sum of n even natural numbers 
        odd=n**2#sum of n odd natural numbers 
        return (hcf(even,odd))#gcd/hcf of those two numbers(sum of even and sum of odd)
n=int(input())
#n=4(should be a natural number)
print(Solution().gcdOfOddEvenSums(n))