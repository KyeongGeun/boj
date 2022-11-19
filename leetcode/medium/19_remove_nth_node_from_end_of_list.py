# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        temp = head
        while temp:
            temp = temp.next
            l += 1

        temp = head
        for _ in range(l - n - 1):
            temp = temp.next

        if l - n == 0:
            return head.next

        temp.next = temp.next.next

        return head
