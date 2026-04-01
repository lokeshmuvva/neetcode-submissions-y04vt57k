# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if curr is None or curr.next is None:
            return curr
        new_head = self.reverseList(curr.next)
        curr.next.next = curr
        curr.next = None
        return new_head
