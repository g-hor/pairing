# 226. Invert Binary Tree

# Given the root of a binary tree, invert the tree, and return its root.


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = [root]

        while stack:
            curr = stack.pop()
            
            left = curr.left
            right = curr.right
            curr.left = right
            curr.right = left

            if curr.left:
                stack.append(curr.left)
            
            if curr.right:
                stack.append(curr.right)

        return root