class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        first_max = second_max = third_max = float("-inf")
        first_min = second_min = float("inf")
        for i in nums:
            if i > first_max:
                third_max = second_max
                second_max = first_max
                first_max = i
            elif i > second_max:
                third_max = second_max
                second_max = i
            elif i > third_max:
                third_max = i
            if i < first_min:
                second_min = first_min
                first_min = i
            elif i < second_min:
                second_min = i
        return max(first_max * second_max * third_max, first_max * first_min * second_min)
print(Solution().maximumProduct([-10,-10,5,2]))