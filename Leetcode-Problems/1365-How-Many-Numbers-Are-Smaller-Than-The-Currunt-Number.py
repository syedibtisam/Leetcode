from typing import List
def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    sorted_num = sorted(nums)

    freq: dict [int, int] = {}

    for index, value in enumerate(sorted_num):
        if value not in freq:
            freq[value] = index

    for index, value in enumerate(nums):
        nums[index] = freq[nums[index]]
    
    return nums