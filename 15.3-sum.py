#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (27.87%)
# Likes:    9305
# Dislikes: 963
# Total Accepted:    1.2M
# Total Submissions: 4.2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Notice that the solution set must not contain duplicate triplets.
# 
# 
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
# Input: nums = []
# Output: []
# Example 3:
# Input: nums = [0]
# Output: []
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

# @lc code=end

