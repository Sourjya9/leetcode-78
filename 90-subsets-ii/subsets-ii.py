class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        result = [[]]
        start = 0
        
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                candidates = result[start:]
            else:
                candidates = result
            
            start = len(result)
            result += [curr + [num] for curr in candidates]
        
        return result