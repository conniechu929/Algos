# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # area = 0
        # current = 0

        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         # current = height[i] * height[j]
        #         if height[i] < height[j]:
        #             current = height[i]*(height[j]-height[i])
        #         elif height[i] > height[j]:
        #             current = height[i]*(height[i] - height[j])
        #         else:
        #             current = height[i] * height[j]
        #     if current > area:
        #         area = current

        # return area

        left = 0
        right = len(height)-1
        area = 0
        current = 0

        while left != right:
            current = min(height[left], height[right]) * (right - left)
            if current > area:
                area = current
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return area
