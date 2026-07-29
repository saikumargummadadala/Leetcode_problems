class Solution:
    def minMoves(self, nums: List[int]) -> int:
        b=max(nums)
        count=0
        for i  in nums:
            if i==b:
                pass
            else:
                count+=b-i
        return count
nums=list(map(int,input().split(",")))
#nums=[2,1,3]
print(Solution().minMoves(nums))