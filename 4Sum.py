# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note: The solution set must not contain duplicate quadruplets.
#
# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []

        for i in range(len(nums)-3):
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3] > target:
                break
            for x in range(i + 1, len(nums)-2):
                start = x + 1
                end = len(nums) - 1
                while start < end:
                    total = nums[i] + nums[x] + nums[start] + nums[end]
                    if total == target:
                        current = [nums[i],nums[x],nums[start],nums[end]]
                        current.sort()
                        start = start + 1
                        end = end - 1
                        if current not in result:
                            result.append(current)
                        while start < end and nums[start] == nums[start-1]:
                            start += 1
                        while start < end and nums[end] == nums[end+1]:
                            end -= 1
                    elif total > target:
                        end -= 1
                    else:
                        start += 1

        return result
