class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        queue = [root]
        currLevel = 1
        minLevel = 1
        maxSum = root.val

        while queue:
            currSum = 0
            newQueue = []

            for node in queue:
                currSum += node.val
                if node.left:
                    newQueue.append(node.left)
                if node.right:
                    newQueue.append(node.right)
            
            if currSum > maxSum:
                minLevel = currLevel
                maxSum = currSum
            
            currLevel += 1
            queue = newQueue


        return minLevel