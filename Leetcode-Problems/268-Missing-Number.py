from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        unique_values = set()
        for i in range(len(nums) + 1):
            unique_values.add(i)
        
        for value in nums:
            unique_values.remove(value)
        
        return unique_values.pop()
        # Solution two
        # return sum(range(len(nums) + 1)) - sum(nums)