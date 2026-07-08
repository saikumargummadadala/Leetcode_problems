s='10203004'
m=len(s)
x=[]
ans=[]
queries=[[0,7],[1,3],[4,6]]
for n in range(len(queries)):
    t=(s[queries[n][0]:(queries[n][1])+1])
    for i in range(len(t)):
        if t[i]!='0':
            x.append(int(t[i]))
        else:
            pass
    Sum=sum(x)
    q=int(''.join(map(str, x)))
    ans.append(Sum*q)
    x=[]
print(ans)