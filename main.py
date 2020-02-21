# Definition for a binary tree node.
class Node:

  def __init__(self, x, left=None, right=None):
    self.val = x
    self.left = left
    self.right = right


class Solution:

  def findDepth(self, root: Node, level: int = 0) -> int:
    maxLeft = level
    maxRight = level
    if root != None and root.val != None:
      maxLeft = self.findDepth(root.left, level + 1)
      maxRight = self.findDepth(root.right, level + 1)

    return maxLeft if maxLeft > maxRight else maxRight

  def maxDepth(self, root: Node) -> int:
    print('hello')
    return self.findDepth(root)


my = Solution()

t0 = Node(1, Node(2, Node(3)), Node(4, Node(5, Node(6))))
ans = my.maxDepth(t0)

print('ans = %s' % str(ans))