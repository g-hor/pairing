# 19. Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create dummy head in case the head itself is removed
        # create position variable to keep track of our position in the linked list
        # traverse the linked list, keeping track of curr node and the position
        # once our position reaches n, we start updating the value of our nth node

        dummy = ListNode(None, head)
        position = 0
        skippedPrev = dummy 

        while head:
            if position >= n:
                skippedPrev = skippedPrev.next

            position += 1
            head = head.next

        if skippedPrev.next:
            skippedPrev.next = skippedPrev.next.next
        else:
            dummy.next = None

        return dummy.next