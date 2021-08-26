# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2: return None
        dummy = cur = ListNode(None) #制造cur 把dummy放在cur头上
        
        # 不知道该连到哪里
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next#忘了移动cur了，我们是需要制备cur这条linkedlist
        if l1:
            cur.next = l1  
        if l2:
            cur.next = l2
        return dummy.next
    
    # time O(n)
    # space O(1)

            
        
