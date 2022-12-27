# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def insertionSortList(self, head):
        curr = head
        dummy = ListNode()

        while curr:
            # we start from psuedo head at every iteration
            prev = dummy

            # iterate till we find position to insert
            while prev.next and curr.val >= prev.next.val:
                prev = prev.next

            # insert element
            next = curr.next
            curr.next = prev.next
            prev.next = curr

            # move ahead in original list
            curr = next

        return dummy.next
