/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun oddEvenList(head: ListNode?): ListNode? {
        var curOdd = head
        var curEven = head?.next

        val firstEven = curEven
        var cur = firstEven?.next

        var idx = 0
        while (cur != null) {
            if (idx == 0) {
                curOdd!!.next = cur
                curOdd = cur
                idx += 1
            } else {
                curEven!!.next = cur
                curEven = cur
                idx -= 1
            }
            cur = cur.next
        }

        curOdd?.next = firstEven
        curEven?.next = null

        return head
    }
}