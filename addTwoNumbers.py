# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# pseudocode
# simple addition coded out

# int val=0
# int cur=0
# while (l1&&l2)
#     val+=cur
#     cur=l1.val+l2.val
#     val+=cur%10
#     cur/=10
#     l1=l1.next
#     l2=l2.next
# return val

    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
            

