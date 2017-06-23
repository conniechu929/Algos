# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# My solution for twoSums:
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    List = []

    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            value1 = nums[i]
            value2 = nums[j]
            total = nums[i] + nums[j]
            if total == target:
                List.append(i)
                List.append(j)
    return List


# More efficient solution:
# Time complexity of O(n) for finding sum by returning an array of two indices
# num = [2,3,4], target = 6
# output = [0,2]
def twoSum(self, nums, target):
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], i]
        else:
            buff_dict[target - nums[i]] = i
