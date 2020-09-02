#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (34.03%)
# Likes:    9030
# Dislikes: 2273
# Total Accepted:    1.5M
# Total Submissions: 4.5M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Example:
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addNumbersRecursive(self, l1, l2, remainder=0):
        sum = l1.val + l2.val + remainder
        response_digit = ListNode(val=sum % 10)
        if not l1.next and not l2.next and not sum//10 :
            return response_digit
        response_digit.next = self.addNumbersRecursive(
            l1.next if l1.next else ListNode(),
            l2.next if l2.next else ListNode(),
            sum // 10,
        )
        return response_digit

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.addNumbersRecursive(l1, l2, 0)


# @lc code=end
