def check_arm(n):
    n=str(n)
    power=len(n)
    m=0
    for i in range(power):
        m+=int(n[i])**power
    return m
n=int(input("Enter the upper limit:"))
#m=1000
m=int(input("Enter the lower limit:"))
#n=10
ans=[]
for i in range(m,n+1):
    if i==check_arm(i):
        ans.append(i)
    else:
        pass
print(ans)
