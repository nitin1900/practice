#submited first wrote my code then i converted into this pattern:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Extract values from linked lists
        l1_vals = []
        while l1:
            l1_vals.append(l1.val)
            l1 = l1.next

        l2_vals = []
        while l2:
            l2_vals.append(l2.val)
            l2 = l2.next

        # Your approach: join → reverse → add → reverse → split
        new1 = ''.join(str(i) for i in l1_vals)
        new1 = new1[::-1]
        new2 = ''.join(str(i) for i in l2_vals)
        new2 = new2[::-1]

        total = str(int(new1) + int(new2))
        total = total[::-1]

        # Build result linked list
        dummy = ListNode(0)
        curr = dummy
        for d in total:
            curr.next = ListNode(int(d))
            curr = curr.next

        return dummy.next

#my code with little help like how to join array to string like that questions asked to ai:
l1 = [2,4,3]
new1 = ''.join(str(i) for i in l1)
new1=new1[::-1]
l2 = [5,6,4]
new2=''.join(str(i) for i in l2)
new2=new2[::-1]
sum=int(new1)+int(new2)
sum=str(sum)
sum=sum[::-1]
final=list(map(int,sum))
