# 2816. Double a Number Represented as a Linked List

# You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

# Return the head of the linked list after doubling it.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # first approach that stores values in array and reassigns values after doubling

        # curr = head
        # values = []

        # while curr:
        #     values.append(str(curr.val))
        #     curr = curr.next

        # valuesString = ('').join(values)
        # valuesNum = int(valuesString)
        # doubledVal = valuesNum * 2
        # doubledStr = str(doubledVal)
        # doubledStr = str(2 * int(('').join(values)))    # one-liner 
        # doubledHead = ListNode()
        # prev = doubledHead

        # for idx, num in enumerate(doubledStr):
        #     prev.next = ListNode(num)
        #     prev = prev.next

        # return doubledHead.next


        # SECOND APPROACH: O(N) time and O(1) space
        # initialize a dummy head with 'val' of 0, which may change to 1 if doubled values result in an additional digit
        # save previous node to a variable
        # previous node's value is incremented if current node doubled results in two digits
        # current node's value is reassigned to the remainder of doubled val modded by 10

        curr = head
        newHead = ListNode(0, head)
        prev = newHead

        while curr:
            if curr.val >= 5:
                prev.val += 1
                curr.val = (curr.val * 2) % 10
            else:
                curr.val *= 2

            prev = curr
            curr = curr.next

        if newHead.val:
            return newHead
        else:
            return newHead.next