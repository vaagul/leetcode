#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (39.79%)
# Likes:    6696
# Dislikes: 270
# Total Accepted:    1.3M
# Total Submissions: 3.2M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: s = "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: s = "{[]}"
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            l = len(s)
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
            if l == len(s):
                return False
        return True
        
# @lc code=end

