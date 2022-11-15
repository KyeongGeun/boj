# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        cnt = 0
        temp = l1
        while temp:
            num += temp.val * (10 ** cnt)
            cnt += 1
            temp = temp.next

        cnt = 0
        temp = l2
        while temp:
            num += temp.val * (10 ** cnt)
            cnt += 1
            temp = temp.next

        s = str(num)
        ans = ListNode(int(s[-1]))
        temp = ans
        for i in range(len(s) - 2, -1, -1):
            temp.next = ListNode(int(s[i]))
            temp = temp.next

        return ans
