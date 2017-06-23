# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums: #if not is NOT the same as if nums is None
        # use if not, when checking input is any kind of zero or empty container, or False
            return 0

        count = 0

        for i in range(1,len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]

        return count + 1
