nums = [1, -1, 2, 3, 4, 5]
k=2
ans=[]
for i in range(0,len(nums),k):
    ans.extend(nums[i:i+k][::-1])
print(ans)    