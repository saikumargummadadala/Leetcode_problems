from bisect import bisect_left
class Solution:
    def arrayRankTransform(self, arr): 
        s = sorted(arr)
        unique = []
        for x in s:
            if not unique or unique[-1] != x:
                unique.append(x)
        for i in range(len(arr)):
            arr[i] = bisect_left(unique, arr[i]) + 1
        return arr
arr=[40,10,20,30,20]
print(Solution().arrayRankTransform(arr))
