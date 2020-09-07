#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (29.54%)
# Likes:    7747
# Dislikes: 565
# Total Accepted:    1M
# Total Submissions: 3.4M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
#
# Example 1:
#
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: "cbbd"
# Output: "bb"
#
#
#

# @lc code=start
class Solution:
    def outward_comparator(self, s, left, right):
        while (0 <= left <= right < len(s)) and (s[left] == s[right]):
            left -= 1
            right += 1
        return s[left + 1 : right]

    def longestPalindrome(self, s: str) -> str:
        max_str = ""
        for i in range(len(s)):
            pstr = self.outward_comparator(s, i, i)
            if len(max_str) < len(pstr):
                max_str = pstr
            pstr = self.outward_comparator(s, i, i + 1)
            if len(max_str) < len(pstr):
                max_str = pstr
        return max_str

# @lc code=end
