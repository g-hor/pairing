# 141. Linked List Cycle

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use a set to keep track of visited nodes
        # travel through the linked list and append new nodes to the set
        # if node is already in set, return false
        # if we reach the end of the linked list, return true

        visited_nodes = set()
        current = head

        while current:
            if current in visited_nodes:
                return True
            else:
                visited_nodes.add(current)

            current = current.next

        return False