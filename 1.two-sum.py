#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reduced_target_list = [target-x for x in nums]
        return_list = []
        for x in reduced_target_list:
            try:
                return_list.append(nums.index(x))
                return_list.append(reduced_target_list.index(x))
            except Exception as e:
                continue
            if len(return_list) > 1:
                return return_list
# @lc code=end
