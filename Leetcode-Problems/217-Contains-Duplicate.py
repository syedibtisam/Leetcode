from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_values = set()

        for value in nums:
            if value in unique_values:
                return True
            unique_values.add(value)
        return False
    
        # Solution two
        # if len(set(nums)) == len(nums):
        #     return False
        # else:
        #     return True