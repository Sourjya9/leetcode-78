class Solution:
    def subsets(self, nums):
        result = [[]]
        [result.extend([curr + [num] for curr in result[:]]) for num in nums]
        return result