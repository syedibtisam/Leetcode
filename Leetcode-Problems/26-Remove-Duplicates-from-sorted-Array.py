from typing import List
def removeDuplicates(nums: List[int]) -> int:
    index = 0
    unique_values = set()

    for value in nums:
        if value not in unique_values:
            nums[index] = value
            index += 1
        unique_values.add(value)
    
    return index
