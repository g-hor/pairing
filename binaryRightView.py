# 199. Binary Tree Right Side View

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.


from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS approach:
        # create output array with root's val
        #   > contain node values
        #   > output's length indicates amount of levels traversed
        # traverse right side first
        #   > append to output only if level is greater than the length of output

        if not root: return []

        output = []
        queue = deque([(root, 0)])
    
        while queue:
            node, level = queue.popleft()

            # level should be same as length of output. otherwise, we have already added a node for that level
            if level is len(output):
                output.append(node.val)

            # if a right exists, append it first so we can search it
            if node.right: 
                queue.append((node.right, level + 1))

            # otherwise, we can search the left branch
            if node.left: 
                queue.append((node.left, level + 1))

        return output