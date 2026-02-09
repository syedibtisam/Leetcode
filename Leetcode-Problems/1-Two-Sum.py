from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    freq = {}

    for index, value in enumerate(nums):
        missing_value = target - value
        if missing_value in freq:
            return [freq[missing_value], index] 
        freq[value] = index