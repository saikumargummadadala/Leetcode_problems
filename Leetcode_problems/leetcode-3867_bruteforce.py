class Solution(object):
    def gcdSum(self, nums):
      #it got time limit excedded error in leetcode
        prefixGcd=[]
        mx=[]
        ans=0
        def hcf(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        for i in nums:
            mx.append(i)
            prefixGcd.append(hcf(i,max(mx)))
        prefixGcd.sort()
        for i in range(len(prefixGcd)//2):
            ans+=(hcf(prefixGcd[i],prefixGcd[(len(prefixGcd)-1)-i]))
        return ans
nums=[2,6,4]
print(Solution().gcdSum(nums))