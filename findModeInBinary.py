# 501. Find Mode in Binary Search Tree

# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        countHash = {}
        stack = [root]
        maxCount = 0

        while len(stack) > 0:
            currNode = stack.pop()
            currVal = currNode.val

            if currVal in countHash:
                countHash[currVal] += 1
            else: countHash[currVal] = 1

            if countHash[currVal] > maxCount:
                maxCount = countHash[currVal]
            
            if currNode.left != None:
                stack.append(currNode.left)
            if currNode.right != None:
                stack.append(currNode.right)

        modes = []
        for nodeVal in countHash:
            if countHash[nodeVal] == maxCount:
                modes.append(nodeVal)

        return modes
