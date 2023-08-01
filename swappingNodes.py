# 1721. Swapping Nodes in a Linked List

# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # iterate through the entire linked list
        # create an index counter variable to match with k in the forward direction
        # create a length variable to determine length of linked list
        # first loop: 
        # > match index with k in fwd direction
        #   > save node at matching index
        # > increment length variable
        # second loop:
        # > match for length - k 
        #   > save node at matching index
        # swap the two values 
        # return head

        if not head: return head

        idx = 1
        length = 1
        first_node = None
        second_node = None
        current_node = head

        while current_node:
            if idx == k:
                first_node = current_node
            idx += 1
            length += 1
            current_node = current_node.next

        idx = 1
        back_idx = length - k
        current_node = head

        while current_node:
            if idx == back_idx:
                second_node = current_node
            idx += 1
            current_node = current_node.next

        first_node.val, second_node.val = second_node.val, first_node.val

        return head