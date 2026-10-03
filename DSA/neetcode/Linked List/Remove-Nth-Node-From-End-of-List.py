#copy-paste by ai...
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left = dummy
        right = head

        # Move right n positions ahead
        for _ in range(n):
            right = right.next

        # Move both until right reaches the end
        while right:
            left = left.next
            right = right.next

        # Remove the node
        left.next = left.next.next

        return dummy.next
