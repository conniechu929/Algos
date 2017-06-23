# my solution for twoSums
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

# ---------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        value1 = value2 = ''
        # value2 = ''
        current1 = l1
        current2 = l2
        while current1 or current2:
            if current1:
                value1 = str(current1.val) + value1
                current1 = current1.next

        # while current2:
            if current2:
                value2 = str(current2.val) + value2
                current2 = current2.next

        total = str(int(value1) + int(value2))

        myNode = runner = ListNode(total[len(total)-1])

        # runner = myNode

        for i in range(len(total) - 2, - 1, -1):
            runner.next = ListNode(total[i])
            runner = runner.next

        return myNode

class Solution:
# @return a ListNode
def addTwoNumbers(self, l1, l2):
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next

# ---------------------------------------------------------------------------------

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_dict = {}
        sub_str = ''
        max_length = 0

        for i in range(len(s)):
            if s[i] not in sub_str:
                sub_str = sub_str + s[i]
            else:
                sub_str = sub_str[sub_str.index(s[i])+1:] + s[i]
            # str_dict[len(sub_str)] = sub_str
            if max_length < len(sub_str):
                max_length = len(sub_str)

        # return max(str_dict) if str_dict else 0
        return max_length


# ---------------------------------------------------------------------------------
# Find the median in with two sorted arrays with overall run complexity of O(log (m+n))
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

# ---------------------------------------------------------------------------------
# Return the zigzag version of the string
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        pattern_str = ['' for i in range(len(s))]
        count = 0
        x = 1

        for i in s:
            pattern_str[count] += i
            count += x
            if count == 0 or count == numRows - 1:
                x = -x

        return "".join(pattern_str)

# ---------------------------------------------------------------------------------
# Reverse integer
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x.bit_length() > 32:
            return 0
        elif len(str(x)) == 1:
            return x
        elif x > 0 and int(str(x)[::-1]).bit_length() >= 32:
            return 0
        elif x < 0:
            if int(str(x)[1:][::-1]).bit_length() >= 32:
                return 0
            else:
                return int(str(x)[0] + str(x)[1:][::-1])
        else:
            return int(str(x)[::-1])

# ---------------------------------------------------------------------------------
# String to Integer (atoi)
class Solution(object):

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        if len(str) == 0:
            return 0
        elif str == '+' or str.isalpha() == True or str == '-':
            return 0
        else:
            num =''
            stop = len(str)
            for i in str:
                if i.isdigit():
                    num = i
                if num.isdigit() and i.isdigit() == False:
                    stop = str.index(i)
                    break
            try:
                x = float(str[0:stop])
                max = 2147483647
                min = -2147483648
                if x < min:
                    return min
                elif x > max:
                    return max
                else:
                    return int(x)
            except:
                return 0

# ---------------------------------------------------------------------------------
# Palindrom Number
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if str(x)[::1] == str(x)[::-1]:
            return True
        else:
            return False

# ---------------------------------------------------------------------------------
