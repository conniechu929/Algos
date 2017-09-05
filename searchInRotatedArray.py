# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        high = len(nums) - 1
        low = 0

        while low <= high:
            middle = (high + low) / 2
            if target == nums[middle]:
                return middle
            if nums[low] <= nums[middle]:
                if nums[low] <= target and target <= nums[middle]:
                    high = middle - 1
                else:
                    low = middle + 1
            else:
                if nums[high] >= target and target >= nums[middle]:
                    low = middle + 1
                else:
                    high = middle - 1
        return -1
