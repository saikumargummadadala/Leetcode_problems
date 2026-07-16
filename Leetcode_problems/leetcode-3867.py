class Solution(object):
    def gcdSum(self, nums):
        
        prefixGcd=[]
        mx=[]
        ans=0
        def hcf(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        current_max = 0
        for i in nums:
            current_max = max(current_max, i)
            prefixGcd.append(hcf(i, current_max))
        prefixGcd.sort()
        for i in range(len(prefixGcd)//2):
            ans+=(hcf(prefixGcd[i],prefixGcd[(len(prefixGcd)-1)-i]))
        return ans
nums=list(map(int,input().split(",")))
#nums = [3,6,2,8]
print(Solution().gcdSum(nums))