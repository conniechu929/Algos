# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
#
# Try to solve it in linear time/space.
#
# Return 0 if the array contains less than 2 elements.
#
# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # This solution is O(n*log(n)) time complexity and constant space complexity
        nums.sort()

        if len(nums) < 2:
            return 0

        max_num = 0
        for i in range(len(nums)-1):
            if max_num < (nums[i+1]-nums[i]):
                max_num = nums[i+1]-nums[i]

        return max_num
