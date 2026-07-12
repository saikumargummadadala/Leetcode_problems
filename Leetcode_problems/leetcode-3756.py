class Solution:
    def sumAndMultiply(self,s,queries):
        simplify = 10**9 + 7
        m = len(s)
        ans = [0] * len(queries)
        Sum = [0] * (m + 1)
        q = [0] * (m + 1)
        x = [0] * (m + 1)
        power = [1] * (m + 1)

        for i in range(1, m + 1):
            power[i] = (power[i - 1] * 10) % simplify

        for i in range(m):
            digit = int(s[i])
            Sum[i + 1] = Sum[i] + digit
            x[i + 1] = x[i] + (1 if digit != 0 else 0)
            if digit == 0:
                q[i + 1] = q[i]
            else:
                q[i + 1] = (q[i] * 10 + digit) % simplify

        for n in range(len(queries)):
            l, r = queries[n]
            length = x[r + 1] - x[l]
            start = q[l]
            end = q[r + 1]
            number = (end - (start * power[length]) % simplify + simplify) % simplify
            total = Sum[r + 1] - Sum[l]
            ans[n] = (number * total) % simplify

        return ans
s = "10203004"
queries = [[0,7],[1,3],[4,6]]
print(Solution().sumAndMultiply(s,queries))