class Solution:
    def sequentialDigits(self, start, end):
        result = []
        for length in range(len(str(start)), len(str(end)) + 1):
            for i in range(1, 10 - length + 1):
                num = 0
                for j in range(length):
                    num = num * 10 + (i + j)
                if start <= num <= end:
                    result.append(num)
        return result