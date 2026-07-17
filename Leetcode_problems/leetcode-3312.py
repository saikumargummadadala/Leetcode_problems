class Solution:
    def gcdValues(self, nums, queries):
        mx = 0
        for x in nums:
            if x > mx:
                mx = x
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1
        cnt_g = [0] * (mx + 1)
        for i in range(mx, 0, -1):
            multiples_count = 0
            for j in range(i, mx + 1, i):
                multiples_count += freq[j]
            pairs = (multiples_count * (multiples_count - 1)) // 2
            for j in range(2 * i, mx + 1, i):
                pairs -= cnt_g[j]
            cnt_g[i] = pairs
        prefix_sums = []
        gcd_values = []
        current_sum = 0
        for i in range(1, mx + 1):
            if cnt_g[i] > 0:
                current_sum += cnt_g[i]
                prefix_sums.append(current_sum)
                gcd_values.append(i)
        result = []
        for q in queries:
            low = 0
            high = len(prefix_sums) - 1
            ans_idx = 0
            while low <= high:
                mid = (low + high) // 2
                if prefix_sums[mid] > q:
                    ans_idx = mid
                    high = mid - 1
                else:
                    low = mid + 1
            result.append(gcd_values[ans_idx])
            
        return result