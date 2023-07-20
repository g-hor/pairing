# 129. Sum Root to Leaf Numbers

# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children.


def sum_numbers(root, num = 0)
  return 0 if !root
  num = num * 10 + root.val
  return num if (!root.left && !root.right)
  
  left = sum_numbers(root.left, num)
  right = sum_numbers(root.right, num)

  return left + right
end