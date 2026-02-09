from typing import List

def findDisappearedNumbers(nums: List[int]) -> List[int]:
    result = []
    for value in nums:
        index = abs(value) - 1
        nums[index] = -abs(nums[index])

    for index,value in enumerate(nums):
        if value > 0:
            result.append(index+1)
    return result


nums = [4, 3, 2, 7, 8, 2, 3, 1]

print(findDisappearedNumbers(nums))