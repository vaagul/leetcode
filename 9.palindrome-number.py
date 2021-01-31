#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (48.60%)
# Likes:    2990
# Dislikes: 1693
# Total Accepted:    1.1M
# Total Submissions: 2.3M
# Testcase Example:  '121'
#
# Given an integer x, return true if x is palindrome integer.
# 
# An integer is a palindrome when it reads the same backward as forward. For
# example, 121 is palindrome while 123 is not.
# 
# 
# Example 1:
# 
# 
# Input: x = 121
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# 
# Example 4:
# 
# 
# Input: x = -101
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= x <= 2^31 - 1
# 
# 
# 
# Follow up: Could you solve it without converting the integer to a string?
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        length = 1
        while x // length > 9:
            length *= 10
        while x:
            left = x // length
            right = x % 10
            if left != right:
                return False
            
            x = (x % length) // 10
            length //= 100

        return True
            
# @lc code=end

