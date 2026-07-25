class Solution:
    def maxProduct(self, n: int) -> int:
        ans=[]
        result=[]
        for  i in str(n):
            ans.append(int(i))
        for x in range(len(ans)):
            for y in range(x+1,len(ans)):
                result.append(ans[x]*ans[y])
        return max(result)