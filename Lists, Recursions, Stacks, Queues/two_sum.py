# let's implement the two sum problem

# brute force solution

def twoSum_brute_force(nums, target):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums[i+1:]):
            if x + y == target:
                return list((i, j+i+1))

# Two-pass Hash Table solution

def twoSum_two_pass(nums, target):
    hash_table = {}
    for i, x in enumerate(nums):
        hash_table[x] = i
    for i, x in enumerate(nums):
        y = target - x
        if y in hash_table and hash_table[y] != i:
            return list((i, hash_table[y]))

# One-pass Hash Table solution

def twoSum_one_pass(nums, target):
    hash_table = {}
    for i, x in enumerate(nums):
        y = target - x
        if y in hash_table:
            return list((i, hash_table[y]))
        hash_table[x] = i

# compare the time complexity of the three solutions

import time

def timeit(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start

# we make a long list of numbers and a target

nums = list(range(1000000))
target = 999999

print(timeit(twoSum_brute_force, nums, target))
print(timeit(twoSum_two_pass, nums, target))
print(timeit(twoSum_one_pass, nums, target))