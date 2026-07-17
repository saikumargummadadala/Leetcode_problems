class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        result=[]
        ans=[]
        def hcf(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                ans.append(hcf(nums[x],nums[y]))
        ans.sort()
        for i in queries:
            result.append(ans[i])
        return result        
nums = [2,3,4]
queries = [0,2,2]
print(Solution().gcdValues(nums, queries))