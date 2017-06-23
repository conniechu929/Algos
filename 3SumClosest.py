# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()

        if len(nums) < 3:
            return False
        if len(nums) == 3:
            return sum(nums)
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i + 1
            end = len(nums) - 1
            while start < end:
                current = nums[i] + nums[start] + nums[end]
                if abs(current - target) < abs(result - target):
                    result = current
                if current == target:
                    return current
                if current < target:
                    start += 1
                elif current > target:
                    end -= 1
        return result
