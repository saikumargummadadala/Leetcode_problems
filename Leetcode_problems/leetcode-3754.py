class Solution:
    def sumAndMultiply(self, n: int) -> int:
       if n!=0:
        Sum = sum(int(digit) for digit in str(n))
        n=list(str(n))
        ans=[]
        for i in n:
            if i!='0':
                ans.append(int(i))
            else:
                pass
        
        result = int("".join(map(str,ans)))
        return result*Sum
       else:
        return 0 
print(Solution().sumAndMultiply(int(input("enter the number:"))))