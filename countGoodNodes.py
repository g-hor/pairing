# 1448. Count Good Nodes in Binary Tree

# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Create a helper method that we call recursively on the root node
        # If root is None, return 0
        # Initialize a maximum variable to keep track of current maximum val
        # If current node's value is > current max, reassign maximum

        max = root.val

        def findGoodNodes(root, max):
            if not root:
                return 0

            if root.val > max:
                max = root.val

            left = findGoodNodes(root.left, max)
            right = findGoodNodes(root.right, max)

            if root.val >= max:
                return 1 + left + right
            else:
                return left + right

        return findGoodNodes(root, max)