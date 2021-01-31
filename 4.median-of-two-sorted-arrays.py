#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (29.78%)
# Likes:    7720
# Dislikes: 1215
# Total Accepted:    731.1K
# Total Submissions: 2.5M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Return the median of the two sorted arrays.
#
# Follow up: The overall run time complexity should be O(log (m+n)).
#
#
# Example 1:
#
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
#
# Example 2:
#
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
# Example 3:
#
#
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
#
#
# Example 4:
#
#
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
#
#
# Example 5:
#
#
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
#
#
#
# Constraints:
#
#
# nums1,length == m
# nums2,length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
#
#
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num1_len = len(nums1)
        num2_len = len(nums2)
        median_index, is_odd = divmod(num1_len + num2_len, 2)
        # nums3 = []
        # num1_index = num2_index = 0
        # for i in range(median_index + 1):
        #     if num1_index == num1_len:
        #         nums3.append(nums2[num2_index])
        #         num2_index += 1
        #     elif num2_index == num2_len:
        #         nums3.append(nums1[num1_index])
        #         num1_index += 1
        #     elif nums1[num1_index] < nums2[num2_index]:
        #         nums3.append(nums1[num1_index])
        #         num1_index += 1
        #     else:
        #         nums3.append(nums2[num2_index])
        #         num2_index += 1
        nums3 = nums1 + nums2
        nums3.sort()
        if is_odd:
            return float(nums3[median_index])
        else:
            return (nums3[median_index] + nums3[median_index - 1]) / 2


# @lc code=end
