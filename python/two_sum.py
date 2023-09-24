def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums) - 1):
        x = nums[i]
        y = target - x
        rest = nums[i+1:]
        if y in rest:
            index = i + 1 + rest.index(y)
            return list((i, index))

# test case
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))