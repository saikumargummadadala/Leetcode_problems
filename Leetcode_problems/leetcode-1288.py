class Solution:
    #checking if the 2d array is bigger than its nextnode if not it is removed from list then prints the lenght of 2d array
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans = []
        x = 0  
        for y in range(len(intervals)):
            if intervals[y][1] > x:
                ans.append(intervals[y])
                x = intervals[y][1]       
            else:
                pass
        return len(ans)
print(Solution().removeCoveredIntervals([[1,4],[3,6],[2,8]]))