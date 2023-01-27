'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
https://leetcode.com/problems/add-two-numbers/
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        pointer = res
        carry = 0
        while l1 or l2 or carry:
            fnum = l1.val if l1 else 0
            snum = l2.val if l2 else 0
            sum = fnum + snum + carry
            num = sum % 10
            carry = sum // 10
            pointer.next = ListNode(num)
            pointer = pointer.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
        return res.next



