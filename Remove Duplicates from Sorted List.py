'''Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p != None:
            if p.next == None:
                break
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p =p.next
        return head