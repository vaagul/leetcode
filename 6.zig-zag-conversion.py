#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (36.54%)
# Likes:    1806
# Dislikes: 4855
# Total Accepted:    482.9K
# Total Submissions: 1.3M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string s, int numRows);
# 
# Example 1:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# 
# Example 2:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# 
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        _dict = {}
        zigzag_string = []
        row = 1
        is_down = True
        for i in range(len(s)):
            _dict.setdefault(row, [])
            _dict[row].append(s[i])
            if row == numRows:
                is_down = False
            if row == 1:
                is_down = True
            row = row + 1 if is_down else row - 1
        for _row, _list in _dict.items():
            zigzag_string.extend(_list)
        return "".join(zigzag_string)
# @lc code=end

