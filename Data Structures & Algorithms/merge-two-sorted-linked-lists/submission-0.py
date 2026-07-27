# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i,j = list1,list2
        head = ListNode(0)
        curr = head

        while i and j:
            if i.val<j.val:
                curr.next = i
                i = i.next
            else:
                curr.next = j
                j = j.next
            curr = curr.next
            

        while i:
            curr.next = i
            i = i.next
            curr = curr.next

        while j:
            curr.next = j
            j = j.next
            curr = curr.next
        return head.next


        