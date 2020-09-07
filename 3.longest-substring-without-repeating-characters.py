#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (30.50%)
# Likes:    10437
# Dislikes: 605
# Total Accepted:    1.7M
# Total Submissions: 5.5M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
#
# Example 2:
#
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
#
# Example 3:
#
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
#
#
#
#
#
#

# @lc code=start
class Solution:
    def __init__(self):
        self.max_val = 0

    def update_max_length(self, letter_count):
        if self.max_val < len(letter_count.keys()):
            self.max_val = len(letter_count.keys())

    def lengthOfLongestSubstring(self, s: str) -> int:
        for i in range(len(s)):
            letter_count = {}
            for j in range(i, len(s)):
                if letter_count.get(s[j], 0) > 0:
                    break
                letter_count[s[j]] = letter_count.setdefault(s[j], 0) + 1
            self.update_max_length(letter_count)
        return self.max_val


# @lc code=end
