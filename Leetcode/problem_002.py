#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


 

l3 = ListNode(0) 
l2 = ListNode(1)

print( l3.val + int(None) )

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
#         l3 = ListNode(0)
             
#         while l1 and l2:
#             l3.val = (l3.val + l1.val + l2.val)%10
#             l3.next = ListNode((l1.val + l2.val)/10) 

#             l2 = l2.next 
#             l1 = l1.next
#             l3 = l3.next
        