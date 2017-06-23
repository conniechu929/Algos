# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5

# Find the median in with two sorted arrays with overall run complexity of O(log (m+n))

# My solution:
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        sortedArray = []
        i = 0
        j = 0

        while length > 0:
            if i >= len(nums1):
                sortedArray.append(nums2[j])
                j += 1
            elif j >= len(nums2):
                sortedArray.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                sortedArray.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                sortedArray.append(nums2[j])
                j = j + 1
            elif nums1[i] == nums2[j]:
                sortedArray.append(nums1[i])
                j += 1
            length -= 1

        if len(sortedArray) == 1:
            median = sortedArray[0]
        elif len(sortedArray) % 2 == 0:
            med = (sortedArray[len(sortedArray)/2-1] + sortedArray[len(sortedArray)/2])/2.0
            print med
            median = float((sortedArray[len(sortedArray)/2-1] + sortedArray[len(sortedArray)/2])/2.0)
        else:
            median = sortedArray[len(sortedArray)/2]

        return median
