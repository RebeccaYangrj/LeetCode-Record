# linked list: link next: cur.next = xxx
# move one step forward: head = cur.next
# calculate val: cur.val
# when adding 2 number need carry, just renew carry 
# 3 cases: 1. both l1 and l2 2. only l1, 3. only l2 ---> while l1 or l2 or carry: if l1; if l2




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        
        carry = 0
        # 在建立结果的时候不大记得了 linked list数据结构不大记得
        dummy = head = ListNode(None)
        
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry = v1+v2+carry
            head.next = ListNode(carry%10)
            carry //=10
            head = head.next
        return dummy.next
        # time : O(n)
        # space: O(n)
            
            
        
