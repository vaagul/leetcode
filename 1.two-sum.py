#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reduced_dict = {}
        for i in range(len(nums)):
            if reduced_dict.get(nums[i]) is not None:
                # print(reduced_dict)
                return [reduced_dict[nums[i]], i]
            else:
                reduced_dict[target-nums[i]] = i
# @lc code=end
