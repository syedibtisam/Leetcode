from typing import List
def moveZeroes(nums: List[int]) -> None:
    left = right = 0
    length = len(nums)
    
    while right < length:
        
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

        right += 1

       


nums = [0,0]
moveZeroes(nums)
print(nums)