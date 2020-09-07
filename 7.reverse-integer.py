#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.81%)
# Likes:    3641
# Dislikes: 5725
# Total Accepted:    1.2M
# Total Submissions: 4.6M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        is_negative = True if x < 0 else False
        if is_negative:
            x = x * -1
        num_string = str(x)
        num_string = num_string[::-1]
        if int(num_string) > 2**31:
            return 0
        return int(num_string) * -1 if is_negative else int(num_string)

        
# @lc code=end

